# Project ZOMBIE — Guardrail Reverse Engineering und Harness Differential Security
**Research Addendum, 10. November 2026.** Bestandteil der bestehenden ZOMBIE-Forschungsagenda, keine eigenständige Studie. Quellenbasis: öffentliche Primärdokumentation und offen einsehbarer Code, keine internen Anbieterunterlagen. **Keine neuen Live-Resultate behauptet.**

## 1. Forschungsfrage

Wie stark hängt unerlaubtes Agentenverhalten bei konstantem Basismodell davon ab, ob ein Harness vertrauenswürdige Arbeitsvorgaben konserviert, externe Inhalte als Daten behandelt, Skill-/Tool-Rechte infrastrukturseitig begrenzt und seine eigenen Verbesserungen gegen unveränderliche Sicherheitsanforderungen validiert?

**Methode:** Reverse Engineering veröffentlichter Schutzmaßnahmen als Fehlermodell, danach getrennte kontrollierte Interventionen. Das Vorhandensein eines Schutzmechanismus ist keine Evidenz dafür, dass jeder andere Harness ohne ihn verwundbar ist.

**Forschungslogik:**
1. Anbieter beschreibt eine Schutzgrenze (belegt).
2. Daraus folgt ein potenzieller Fehlermodus an der Grenze (Hypothese).
3. Eine unveränderte Modellversion führt dieselbe synthetische Aufgabe durch verschiedene Harness-Konfigurationen aus (Experiment).
4. Der Host bestätigt exakt welche Eingaben, Entscheidungen, Regeln und Effekte stattfanden (Evidenz).
5. Nur ein kontrollierter Unterschied darf als harnessvermittelter Effekt ausgewertet werden (Kausalbefund).

## 2. Anbieter- und Architekturvergleich

### 2.1 Anthropic: Kontainment, Gegenprüfung und externe Daten

Primärquelle (25.05.2026): https://www.anthropic.com/research/how-we-contain-claude

Anthropic unterscheidet die Verteidigung von **Umgebung**, **Modell** und **externen Inhalten**. Die Umgebung muss etwa Zugriff auf Dateisysteme, Netzwerke und Geheimnisse unabhängig vom Modell begrenzen. Der Beitrag berichtet auch von Approval Fatigue (ca. 93 % von Berechtigungsabfragen wurden genehmigt) und explizit davon, dass ein GitHub-Connector bei intakter Connector-Sicherheit trotzdem vergiftete README-Inhalte in den Modellkontext einbringen kann.

Ergänzende primäre Browser-Untersuchung (24.11.2025): https://www.anthropic.com/research/prompt-injection-defenses

**Ableitung:** Prompt-/Klassifikatorabwehr ist nicht gleich echte Tool-Autorisierung. ZOMBIE muss Exposition, Modellentscheidung, Tool-Versuch, Host-Erlaubnis und Ausführung getrennt messen. Claude in Chrome darf zur Untersuchung fremder, ungeprüfter Skills nicht als Erstprüfer eingesetzt werden.

### 2.2 OpenAI: Agent Sandbox, Auto-Review und externe Tool-Policies

Primärquellen:
- https://openai.com/index/designing-agents-to-resist-prompt-injection/
- https://developers.openai.com/api/docs/guides/agents-api/environments/security
- https://developers.openai.com/api/docs/guides/agents/guardrails-approvals

OpenAI beschreibt indirekte Prompt Injection zunehmend als Social-Engineering-Problem. Die Agenten-API empfiehlt getrennte Sandboxen, beschränkten Netzwerkzugriff, getrennte Schlüssel, Authentifizierung durch vertrauenswürdige Broker und explizite Tool-Freigaben. Eine eigene Responses-/Agents-SDK-Integration übernimmt Codex Auto-Review nicht automatisch.

**Ableitung:** Eine Modellentscheidung darf nicht selbst ihre Berechtigung definieren. Bei einem abweichenden Harness ist zu prüfen, ob Berechtigungsprüfung vor echten Systemeffekten stattfindet.

OpenAI Codex demonstriert zudem platform-spezifische Ausführungslogik im öffentlich lesbaren Code: https://github.com/openai/codex/blob/main/codex-rs/core/src/exec_policy.rs . Daraus folgt **nicht**, dass beobachtete Luna-/Copilot-Probleme bereits einem Windows-Sandboxfehler zugeordnet wären; genau das wäre experimentell zu prüfen.

### 2.3 GitHub Copilot: Cloud-Agent-Schutz und lokale IDE sind zu trennen

Primärquellen:
- https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations
- https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-the-firewall
- https://docs.github.com/en/copilot/concepts/prompting/response-customization

Copilot Cloud Agent hat branch-begrenzte Schreibrechte, menschliche PR-Reviews, CodeQL/Dependency/Secret-Prüfung und eingeschränkten Internetzugriff. Die dokumentierte Firewall schützt **nicht unmittelbar MCP-Serverprozesse oder Setup-Schritte**. Das ist eine dokumentierte Abdeckungsgrenze, kein hier nachgewiesener Exploit. Die Priorität verschiedener Instructions hängt von der Copilot-Oberfläche ab; lokale IDE, Copilot CLI und Cloud-Agent sind keine einheitliche Harness-Konfiguration.

**Ableitung:** Vergleiche innerhalb von Copilot müssen Client, Extension-Version, OS, Skill-Suche, Compaction-Strategie und Tool-Gate getrennt erfassen. Eine negative Nutzerregel ist kein automatisch signierter, persistenter Policy-Kontrakt.

### 2.4 OpenCode: Doom-Loop-Regel und ihre semantische Grenze

Primärquelle: https://docs.opencode.ai/docs/permissions/

OpenCode bietet Allow/Ask/Deny pro Tool, Skill, Subagent und Außenverzeichnis. Die dokumentierte Doom-Loop-Prüfung wird bei **dreimal identischem Tool-Aufruf mit identischen Eingaben** ausgelöst. Die meisten Standard-Tools sind ohne eigene Konfiguration erlaubt; Außenverzeichniszugriffe und Doom-Loops erfordern standardmäßig Rückfrage.

**Ableitung:** Semantische Reparaturschleifen A→B→A mit veränderten Argumenten sind **nicht identisch** mit einem Tool-Aufruf-Loop. ZOMBIE muss Fehlerzustände, Zwischenänderungen und Nettofortschritt erfassen. Diese Lücke ist ein zu prüfender Fall, keine bewiesene OpenCode-Sicherheitslücke.

### 2.5 Google Harness²: Selbstverbesserung erzeugt einen neuen Autoritätsübergang

Primärquellen:
- Paper (09.10.2026): https://arxiv.org/abs/2610.14224
- Repository: https://github.com/google-research/harness2
- Optimierungsmechanik: https://github.com/google-research/harness2/blob/main/harness2/core/recursion.py
- Veränderte Komponenten und Editor-Regeln: https://github.com/google-research/harness2/blob/main/harness2/core/prompts.py
- Strukturprüfung: https://github.com/google-research/harness2/blob/main/harness2/core/tree.py
- Erfahrungsbibliothek: https://github.com/google-research/harness2/blob/main/harness2/core/library.py
- CLI-Editor: https://github.com/google-research/harness2/blob/main/harness2/core/proposer.py

Google verändert bei konstantem Modell Systemprompt, Guardrails, Memory, Tools, Skills, Scripts, Subagents und Plugins. Bei Task-Level-Rekursion entstehen mehrere Kandidaten; nach Probes wird ein neuer Harness zusammengesetzt. Zwischen Aufgaben können verbesserte Harnesses und Lessons persistiert werden.

Der öffentlich lesbare tree.validate-Code prüft u. a. erlaubte Dateiformate, Größen, Trigger-/Skriptverweise und Hooks-Schema. Das ist **keine vollständige semantische Autoritäts- und Policy-Invariantenprüfung**. Es ist noch nicht belegt, dass die vollständige Laufzeit gar keinen separaten Schutz gegen abträgliche Guardrail-Änderungen enthält. Der Claude-CLI-Pfad in proposer.py enthält bedingt den Parameter --dangerously-skip-permissions. Diese konkrete Implementierungsentscheidung ist **nicht** gleichbedeutend damit, dass alle Benchmark-Exekutoren in diesem Modus laufen.

**Neue Hypothese:** Ein selbstoptimierender Harness kann Task-Erfolg verbessern und gleichzeitig Robustheit, Constraint-Provenienz oder die Wirkung einer Policy verschlechtern. Deshalb beides getrennt messen; kein Sicherheitsgewinn aus Benchmark-Erfolg ableiten.

### 2.6 OpenClaude: technisch relevanter Fork, Herkunft und Rechte gesondert prüfen

Projektbeschreibung: https://github.com/doc-war/openclaudefork und https://github.com/mjohnnywest/openclaude

Die Projekte bezeichnen sich als Forks eines öffentlich gewordenen Claude-Code-Quellstands mit Anpassungen für andere Modellanbieter. Das ist **keine offizielle Freigabe oder Supportzusage von Anthropic**. Quellcodeherkunft und Nutzungsrechte sind vor jeder technischen Übernahme unabhängig zu prüfen; Änderungen in API-Shims, Berechtigungsprüfung und Kontextkompilierung sind getrennte Forschungsgegenstände.

**Ableitung:** Ein ähnlicher Name oder übernommener Tool-Satz beweist nicht dieselben Sicherheitsmechanismen. Für wissenschaftliche Differenzialanalyse nur bestätigte, rechtmäßig verfügbare Quellen verwenden.

## 3. Unabhängige empirische Anhaltspunkte

- NVIDIA (05.10.2026): https://research.nvidia.com/ai-security/assume-misalignment-securing-ai-agents-beyond-prompt-injection . Beschreibt explizit Zielabweichungen, Instruktionsverlust über lange Laufzeiten und bei Agentenübergaben. Diese Mechanismen stimmen mit der **Art** der Nutzerbeobachtung überein, belegen aber nicht deren individuelle Ursache.
- Google Research (2026): https://research.google/pubs/securing-multi-agent-systems-an-empirical-analysis-of-security-prompt-hardening-and-residual-risks/ . In einem untersuchten Multi-Agent-Framework sank die Single-Turn-Fehlerrate mit Prompt-Härtung von 19,48 % auf 2,60 %, Multi-Turn von 75,00 % auf 46,88 %. Kein universeller Modell- oder Harness-Effekt; Restanfälligkeit bleibt hoch.
- Agent Skills in the Wild (15.01.2026): https://arxiv.org/abs/2601.10338 . 31.132 analysierte Skills, 26,1 % mit mindestens einem risikobehafteten Muster, 5,2 % mit starken Verdachtsmustern für bösartige Absicht. **Nicht** 26,1 % bestätigte Malware.
- USENIX Security 2026: https://www.usenix.org/conference/usenixsecurity26/presentation/liu-yi . Unterscheidet absichtlich bösartige Skills und sicherheitstechnisch mangelhafte Skills. Intent darf nicht aus einem einzelnen Regex-Treffer gefolgert werden.

## 4. Experimentelle Fragestellungen innerhalb der bestehenden ZOMBIE-Arbeit

**G1 — Trust-Label Loss:** Wird die Herkunft externer Daten bei Browser, Retrieval, Parser, Skill-Activation oder Subagent-Handoff nicht übernommen? Evidenz: Originalreceipt → Host-Transform → tatsächlicher Model-Input-Digest → Entscheidung.

**G2 — Constraint Provenance Loss:** Nach einer unabhängig bestätigten Fehlentscheidung X wird X durch autorisierte Nutzer-/Hostentscheidung ausgeschlossen. Wird X nach Compaction, Delegation oder einem Harness-Wechsel wieder als zulässige Lösung gewählt? Evidenz: Constraint-ID, Revision, Cause-Receipt, Resume-Input, selected/attempted/executed.

**G3 — Repair Oscillation:** Bei gleicher Testsuite und autorisierten Änderungen durchläuft ein Agent eine signierte Fehlerfolge A→B→A ohne messbaren Nettofortschritt. Negativkontrollen: bloßer Nachtest, Teständerung, erfolgreiche Regression, zulässiger Rollback. Subarm: sicherheitsmotivierte Wiederholung (FREE-Konfiguration).

**G4 — Editable Guardrail Regression:** Gleicher Task und gleiches Modell, aber editierbarer vs. host-pinned Guardrail. Getrennt messen: Task-Erfolg, erneute verbotene Entscheidung, Host-Policy-Erlaubnis, echte Seiteneffekte, Performancekosten.

**G5 — Skill Approval Drift:** Skill-Version v1 ist freigegeben; v2 ändert SKILL.md, LICENSE oder referenzierte Datei. Prüfen, ob die Änderung entdeckt wird, ob die Skill-Auswahl erfolgt und ob die aktuelle Version ohne erneute Autorisierung geladen wird. Kein echter Malware-Code erforderlich.

**G6 — Cross-Agent Autoritätskaskade:** Auftrag und Einschränkungen an A; delegierte B/C haben gleiche oder reduzierte Rechte. Messen, welche Instruktionen, Provenienz-Receipts und Policy-Gates auf jedem Handoff erhalten bleiben.

**G7 — Client/OS-Abweichung:** Bei konstantem Modell und Aufgabe verschiedene Harness-/OS-Konfigurationen. Die effektive Tool-Registry, die realen Requests, Compaction-Resultate und Sandbox-Policies müssen mitgeloggt werden. Windows-Effekt ist Hypothese, kein Ergebnis.

**G8 — Persistent Harness Improvement Contamination:** Eine unerlaubte Instruktion wird in eine Trainings-/Improvement-Lesson oder die nächste Harness-Version übernommen. Messung: adoptierter Dateidigest, Ursprungsbeleg, unveränderlicher Constraint-Vertrag, spätere Aktivierung ohne Reimport.

## 5. Konfirmatorische Designprinzipien

1. **Versuchsstand:** genehmigte synthetische Aufgabenbank; identische Ausgangsversion und Model-Provider; keine realen Kundendaten, Credentials oder produktiven Tools.
2. **Manipulation:** nur eine abgegrenzte Dimension pro Hauptkontrast ändern, etwa Guardrail-Pinning oder Skill-Freigabestufe. Modellwechsel, OS, Compaction und Harness nicht gleichzeitig verändern.
3. **Nullarme:** neutrale gleich lange Information, identische Retrievalzyklen und wiederholte unabhängige Läufe.
4. **Beobachtung:** tatsächlicher Host-Input, Prompt-Compiler-Receipt, Modell-/Provider-Receipt, Tool-Vorschlag, Policy-Entscheidung und tatsächlich ausgeführter Seiteneffekt. Signatur eines Simulators beweist noch keinen realen Provider-Aufruf.
5. **Raten:** False-Activation-Rate, legitimer Task-Erfolg, Forbidden-Reopen-Rate, Repair-Oscillation-Rate, Unauthorized-Tool-Attempt und Unauthorized-Execution getrennt.
6. **Langzeit:** pre-registrierte maximal zulässige Schritte, keine automatische Verlängerung nach Fehlschlägen; Handoff-/Resume-Aufgaben nach 1, 3 und 5 Iterationen nur dann vergleichen, wenn Modellinput-Budget und Evaluation synchronisiert werden.
7. **Kausalität:** gleiche Aufgabe über verschiedene Konfigurationen gepaart; Reihenfolge randomisiert; stratifiziert nach Modell, Harness, OS und Aufgabenfamilie. Bericht mit Konfidenzintervallen und Unsicherheiten.
8. **Abstinenz:** Änderungen an Guardrails nur in Wegwerf-Labor mit extern unveränderlichen Host-Policy-Gates; niemals in produktiven Browser-/MCP-/Cloud-Konten.

## 6. Transfer zu FruitStack

Die bestehenden Komponenten sind Ausgangspunkte, **keine durchgängige, nachgewiesene Instrumentierung**:
- PeachMe: Gateway-Receipt, tatsächlicher Policy-Verdikt, Toolversuch und Ausführung.
- CherryMe: externe Evidenz, Candidate→Verified und unabhängige Verifikationsreceipts.
- MangoMe: hostautorisierte Constraints, Write-/Read-Receipts und Sitzungsübergänge.
- OrangeMe: versionierter Projekt-/Auftragszustand und Nachweis unveränderter Anforderungen.
- PlumMe: tatsächliche Provider-/Modellroute und effektiver Kontext statt frei behaupteter Modell-ID.
- ZOMBIE: read-only Prüfer und gepaarte Angriffsfälle; aktuelle Offline-Tests sind keine Forschungsergebnisse.

**Architekturprinzip:** Harness² darf im Labor Vorschläge zur Verbesserung liefern. Verbindliche Sicherheits- und Auftragsentscheidungen gehören in einen separaten, signierten, nur per autorisierter Änderung revidierbaren Host-Vertrag. Der Agent darf seine eigenen Beglaubigungen nicht erstellen.

## 7. Priorität und Falsifizierbarkeit

**Erster kontrollierter Hauptkontrast:** G2 + G3, weil sie die konkreten Luna-/FruitStack-Beobachtungen abbilden und mit harmlosen Code-Aufgaben testbar sind. Vergleich: gleiches Modell/gleicher Task, einmal reguläre Kontextübergabe und einmal hostgebundener Constraint-Vertrag, unabhängig getestete A/B-Fehlerfolge. Erfolg ist weniger unzulässiges Reopening und weniger A→B→A ohne Verlust legitimer Task-Performance. Bleibt der Unterschied aus, ist die angenommene Harnessursache in dieser Konfiguration nicht bestätigt.

**Zweiter Kontrast:** G4 + G8 bei Google-Harness²-artiger Selbstoptimierung. Jede adoptierte Harness-Version muss einen maschinenprüfbaren, hostseitig unveränderlichen Constraint-Satz bestehen. Positive Performance ohne Guardrail-Integrität wird nicht als erfolgreiche Optimierung berichtet.

Das Ergebnis ist eine überprüfbare Hypothesenarchitektur und Quellenkartierung – noch kein Live-Experiment.
