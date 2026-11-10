# Z01: FruitStack-Host-Capture – Anschluss und Beweisgrenzen

**Stand: 10. November 2026.** Implementierung: [zombie_fruitstack_capture.py](../zombie_fruitstack_capture.py). Manuskript: [Revision 1.5](Project_ZOMBIE_Wissenschaftliche_Arbeit_v1.5_2026-11-10.md).

## Implementierte Beobachtungspunkte

| Tatsächliche Host-Grenze | Adapter | Nachweis | Nicht nachgewiesen |
| --- | --- | --- | --- |
| PeachMe nach ToolGateway.invoke | HostCapture.observe_peachme / invoke_peachme | Receipt-ID, Status, Policy-Outcome, Work-/Tool-/Argumentbindung und SHA-256 des Toolresultats | Wahrheit der Quelle |
| CherryMe nach GatewaySearchBackend.search | observe_web_search / observe_cherryme | Ursprungsreceipt, Source-URL-Digest, Original-/Excerpt-Digest und Transformationsverweis | Dass das Modell die Quelle sah |
| Letzter Modellclient-Callback | submit_model | Hash des übergebenen Requestobjekts, Beobachtung des inerten Canarys im Request | Bestätigter Provider-Eingang oder interne Verarbeitung |
| Separater Evidence-Store | PrivateJSONLSink | HMAC-Signatur pro Ereignis, private JSONL-Datei (0600), append und fsync | Kryptografisch unveränderliche Archivierung |

Damit wird die bisherige künstliche Hash-Gleichsetzung zwischen Roh-Tool-Ergebnis und verarbeitetem Excerpt aufgelöst. Der Provenienzgraph verbindet **unterschiedliche, jeweils überprüfte Digests**.

## Quellcode-Abhängigkeit: PeachMe und CherryMe

Der echte PeachMe ToolGateway liefert die verschachtelte Struktur (Status, Decision-Objekt, Receipt-Objekt, Result). CherryMes Gateway-Adapter auf main erwartet dagegen den vereinfachten Legacy-Vertrag (Decision-String und flache Receipt-ID). Hinzu kommt: PeachMe ruft asynchron auf, CherryMes GatewaySearchBackend verwendet derzeit eine synchrone Invoke-Schnittstelle.

Beides muss im realen Host berücksichtigt werden. Für die Formatnormalisierung und die Rückweisung inkonsistenter Receipts wurde [CherryMe PR #16](https://github.com/tonnestate/CherryMe/pull/16) geöffnet. Die eigentliche Host-Integration ist mit dem PR noch nicht bereitgestellt.

## Konkrete Staging-Verdrahtung

Eine FruitStack-Instanz muss ein bereits autorisiertes PeachMe-Gateway und den tatsächlichen Modellclient besitzen. Die folgende Funktion ist eine vollständige Host-Routine zum Einhängen. Sie nimmt die bestehenden Instanzen ausdrücklich als Parameter entgegen; sie baut keinen Fake-Tool-Service und keinen Fake-Provider.

~~~python
import asyncio
import os
from pathlib import Path

from cherryme.web_research import GatewaySearchBackend
from zombie_fruitstack_capture import HostCapture, PrivateJSONLSink


async def z01_single_host_run(
    *,
    gateway,
    send_model_request,
    provider_payload,
    research_query,
    work_ref,
    model_id,
    trace_id,
):
    """Authorized staging only, with host-owned credentials and private evidence."""
    keys = {
        name: os.environ[f"ZOMBIE_AUDIT_KEY_{name.upper()}"].encode("utf-8")
        for name in ("peachme", "cherryme", "plumme")
    }
    capture = HostCapture(
        trace_id, work_ref, keys=keys,
        event_sink=PrivateJSONLSink(
            Path("/var/lib/zombie-private/z01-evidence.jsonl")
        ),
    )
    observations = []

    def host_gateway_invoke(server, tool, arguments, invoked_work_ref):
        response, observed = asyncio.run(
            capture.invoke_peachme(
                gateway, server=server, tool=tool,
                arguments=arguments, work_ref=invoked_work_ref,
            )
        )
        observations.append(observed)
        return response

    backend = GatewaySearchBackend(host_gateway_invoke, work_ref=work_ref)
    search = await asyncio.to_thread(backend.search, research_query)
    if not observations or search.status != "SOURCES":
        return {"search_status": search.status, "model_called": False}

    source_event_ids = capture.observe_web_search(search, observations[-1])
    if not source_event_ids:
        return {"search_status": search.status, "model_called": False}

    # provider_payload comes from the host's REAL context compiler,
    # assembled using the above observed sources.
    result, event_id = await capture.submit_model(
        sender=send_model_request,
        payload=provider_payload,
        source_event_ids=source_event_ids,
        model_id=model_id,
    )
    return {"search_status": search.status, "model_called": True,
            "client_event_id": event_id, "response_received": result is not None}
~~~

Die synchrone CherryMe-Schnittstelle wird hier bewusst in einem Worker-Thread aufgerufen. Diese Konstruktion ist für eine einzelne isolierte Staging-Messung bestimmt; bei mehrfachen parallelen Durchläufen muss die Host-Eventloop- und Thread-Zuständigkeit explizit geprüft werden.

## Notwendige Host-Sicherheitsgrenzen

1. Host-HMAC-Schlüssel dürfen **nicht** im Modellkontext, in Modelltools, im selben ungeschützten Shellkonto oder in öffentlicher CI vorhanden sein. Dass eine Pythonklasse einen Schlüssel benutzt, beweist seine Isolation nicht. Für starke Evidenz einen dedizierten Auditprozess/Sidecar verwenden.
2. HostCapture hat keine direkte Netzwerkfunktion; es führt selbst keine Modell- oder MCP-Abfragen aus. Die Methode submit_model übergibt nur den bereits vom Host kompilierten Request an den tatsächlich gewählten Client-Callback.
3. Ein signiertes client_payload_sha256 belegt den **Host-Client-Call**, nicht notwendigerweise die auf dem Netzwerk gesendeten Provider-Bytes oder die tatsächlich konsumierten Tokens. Für einen vollständigen Z01-Endpunkt wird ein letzter Transport-/Provider-Receipt benötigt.
4. Durch die Source-Aufnahme abgelehnte Webinhalte müssen für eine Filter-Wirksamkeitsanalyse gesondert gezählt werden. Ein fehlender source_admitted-Eintrag beweist nicht, dass beim Retrieval nichts vorhanden war.
5. Signaturen über Eventdaten machen eine bestehende Logdatei nicht unveränderbar. Separate Aufbewahrung und unabhängiger Replay-Audit sind erforderlich.
6. Nur autorisierte Testinstanzen mit synthetischen Quellen, begrenzten Werkzeugen und ohne produktive Zugangsdaten verwenden.

## Abnahme und Status

~~~bash
python -m pytest -q tests/test_zombie_fruitstack_capture.py -m "not remote"
~~~

Die Offline-Tests decken echte Response-Schemas, Digest-Konsistenz, verworfene Aufrufe, Liniennachweise, signierte Eventketten, Modellclient-Eingaben und den privaten Dateisink ab.

**Noch nicht erfolgt:** Deployment des Adapters in einer echten FruitStack-Hostinstanz, unabhängig bestätigte Schlüsselisolation, dauerhafte Kopplung an die echte Modell-Context-Kompilierung, Nullverteilung, kontrollierte Trial-Bedingungen und externe Verifikation. Ein grüner Offline-Test wird nicht als wissenschaftliches IPI-Ergebnis ausgegeben.
