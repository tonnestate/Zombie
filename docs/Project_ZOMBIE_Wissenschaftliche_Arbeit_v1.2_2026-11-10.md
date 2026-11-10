---
title: "Project ZOMBIE: Expositionsdosis, Kontextprovenienz und Persistenz fremder Information in autonomen KI-Agenten"
subtitle: "Forschungsstand, kausales Untersuchungsdesign und Präregistrierungsentwurf mit Implikationen für Generative Engine Optimization"
date: "2026-11-10"
status: "Forschungsmanuskript und Präregistrierungsentwurf – keine experimentellen ZOMBIE-Ergebnisse"
language: "de"
version: "1.2"
keywords:
  - Indirect Prompt Injection
  - Agentic AI
  - Memory Poisoning
  - Dosis-Wirkung
  - Knowledge Graph
  - GEO
  - Kausalinferenz
  - Reproduzierbarkeit
---

# Project ZOMBIE: Expositionsdosis, Kontextprovenienz und Persistenz fremder Information in autonomen KI-Agenten

**Forschungsmanuskript und Präregistrierungsentwurf**  
**Stand:** 10. November 2026 · **Revision 1.2**  
**Anwendungsrahmen:** FruitStack als vorhandener Experimentier- und Validierungsverbund; TOKI SEO und Fruit-Hub.com als mögliche spätere Anwendungskontexte.  
**Ergebnisstatus:** Es wurden für dieses Manuskript **keine eigenen ZOMBIE-Messreihen ausgeführt**. Alle beschriebenen Z01–Z05-Ergebnisse sind *Forschungsfragen oder vorab festgelegte Erfolgskriterien*, keine Beobachtungen.

## Zusammenfassung

Autonome KI-Agenten verarbeiten externe Webseiten, Dateien, E-Mails und Werkzeugantworten, um Nutzeraufgaben zu lösen. Enthalten diese unzuverlässigen Quellen verhaltenssteuernde Anweisungen, kann eine **indirekte Prompt-Injection** (Indirect Prompt Injection, IPI) entstehen: Der Agent behandelt Teile fremder Daten unter Umständen als Handlungsanweisungen. Die Forschung dokumentiert Angriffe über nicht sichtbare Inhalte, Obfuskation, dynamisch zusammengesetzte Webseiten und persistente Agentenspeicher. Sie zeigt jedoch nicht, dass eine bestimmte Anzahl wiederholter Abrufe, beispielsweise 20, automatisch eine Agentenübernahme auslöst. [1–5]

Dieses Manuskript entwickelt daher eine falsifizierbare Fragestellung: **Verändert die wiederholte Exposition gegenüber derselben externen Quelle das Verhalten eines KI-Agenten über den Effekt der zusätzlich präsentierten Informationsmenge hinaus?** Ferner wird untersucht, ob beobachtete Veränderungen der Retrieval-Schicht, dem aktuellen Kontext, persistenten Speichervorgängen oder der Werkzeugautorisierung zuzuordnen sind. Ein mehrstufiges, aber getrennt auszuwertendes Versuchsprogramm (Z01–Z05) verbindet eine vorgelagerte Nullverteilung, token- und zykluskontrollierte Vergleichsarme, ein faktorielles Grunddesign mit explizitem Abwehrfaktor, modellstratifizierte Auswertung sowie ereignisbasierte Provenienzprotokolle. Ergänzende Prüfarme adressieren die Schreibentscheidung ins Langzeitgedächtnis (*Write Election*), multimodale Eingaben, Tool-Registry-Provenienz und die Retrieval-Barriere. Die wirtschaftliche Anwendung in Generative Engine Optimization (GEO) wird eigenständig untersucht: Eine zentrale, überprüfte Wissensbasis kann sachlich konsistente HTML-, Markdown- und strukturierte Datenrepräsentationen für verschiedene Clients erzeugen. Potenzielle Empfehlungs- oder Affiliate-Effekte werden gemessen und nicht vorausgesetzt. [6–9]

**Wissenschaftlicher Anspruch:** Project ZOMBIE ist der Arbeitsname einer **Versuchsinfrastruktur**, keine bereits validierte Angriffsklasse und kein wissenschaftlicher Befund.

**Schlüsselwörter:** KI-Agenten, indirekte Prompt-Injection, Kontextkontamination, Memory Poisoning, dosisabhängige Exposition, Retrieval, Kausalinferenz, GEO, Agentensicherheit.

---

## 1. Problemstellung und Abgrenzung

Die Bezeichnung *ZOMBIE* beschreibt anschaulich die Sorge, dass fremde Informationen über mehrere Verarbeitungsschritte hinweg zu unautorisiertem Agentenverhalten führen können. Für die wissenschaftliche Untersuchung ist diese Metapher jedoch ungeeignet, sobald sie eine dauerhafte Kontrolle oder einen vorhersagbaren Umschaltpunkt suggeriert. Eine einmalige ungeeignete Antwort, eine fehlerhafte Empfehlung, eine versuchte Tool-Aktion und eine tatsächlich durchgesetzte Rechteverletzung sind verschiedene Beobachtungen. Sie dürfen nicht unter einer pauschalen „Übernahmequote“ zusammengefasst werden.

Die **Untersuchungseinheit** ist ein eindeutig identifizierter *Agentenlauf* in einer kontrollierten Umgebung. Die Einheit verfügt über einen festgelegten Benutzerauftrag, festgelegte Werkzeugrechte, eine dokumentierte Pipeline für externe Inhalte und einen versionierten Modellzustand. Ein Test kann die Wirkung einer externen Information nur dann zuordnen, wenn nachvollziehbar ist, ob diese Information überhaupt an das Modell übergeben wurde.

Die Arbeit trennt vier Ebenen:

1. **Verfügbarkeit:** Eine HTTP-Antwort oder ein Dokument wurde angefordert und gegebenenfalls zugestellt.
2. **Exposition:** Der relevante Inhalt ist nach Parsing, Filterung und Kontextkürzung tatsächlich in die Modelleingabe gelangt.
3. **Verhaltensänderung:** Die Ausgabe, Empfehlung oder geplante Aktion weicht unter kontrollierten Bedingungen von der Referenz ab.
4. **Autorisierungsverletzung und Persistenz:** Ein Agent versucht eine unzulässige Tool-Aktion beziehungsweise nutzt Informationen in späteren Sitzungen über einen nachweisbaren persistenten Speicherpfad erneut.

Die Arbeit behandelt Angriffsmechanismen ausschließlich als Gegenstand **autorisierter, isolierter Sicherheitsforschung**. Sie spezifiziert keine verdeckte Manipulationskampagne, keine operative Übernahme fremder Agenten und keine Umgehung von Schutzmaßnahmen bei realen Besucherinnen und Besuchern.

### 1.1 Begriffspräzisierung: „Bitcode“

Im vorliegenden Themenkomplex bezeichnet „Bitcode“ umgangssprachlich unterschiedliche Dinge, die technisch auseinanderzuhalten sind:

- **Unsichtbare oder besondere Unicode-Zeichen:** sind reguläre Textzeichen beziehungsweise Tokenisierungsinputs, nicht ausführbarer Maschinencode.
- **Kodierte Textrepräsentationen:** etwa Base64- oder Hexdarstellungen, die im Modellkontext als Zeichenfolge vorkommen können; ihre semantische Dekodierung ist nicht garantiert.
- **Metadaten, HTML-Attribute, versteckte DOM-Elemente:** werden nur dann relevant, wenn die jeweilige Extraktionspipeline sie beibehält.
- **Ausführbarer Bytecode/Binärcode:** benötigt eine geeignete Laufzeit oder ausführende Komponente; bloßes Vorkommen im Text bedeutet keine Codeausführung.

Ein Sprachmodell besitzt keinen eigenen universellen HTML-Renderprozess. Entscheidend ist aber **nicht** die abstrakte Aussage „das LLM liest allen Quelltext“, sondern die konkrete Pipeline zwischen Netzwerkantwort, Browser/Parser, Snapshot, Retrieval und tatsächlicher Modellnachricht.

### 1.2 Forschungsfragen

**F1:** Welche versteckten, kodierten oder strukturierten Signale erreichen in unterschiedlichen Ingestion-Pipelines tatsächlich den Modellkontext?  
**F2:** Besteht bei wiederholter Exposition gegenüber *inhaltlich unveränderten* Quellen ein eigenständiger, dosisabhängiger Effekt auf Empfehlungen oder Aufgabenerfüllung, wenn Tokenbudget und Position kontrolliert werden?  
**F3:** Welche Wirkung haben nachträgliche Inhaltsversionswechsel, und wie lassen sich Cache- sowie Retrievaleffekte vom Modelleffekt trennen?  
**F4:** Führt eine verhaltensrelevante Information nur zu Antwortabweichungen oder auch zu unautorisierten **Tool-Versuchen** beziehungsweise tatsächlich ausgeführten Aktionen?  
**F5:** Wann kann eine spätere Beeinflussung eindeutig auf einen dokumentierten persistenten Memory-Write und Memory-Read statt auf Restkontext oder erneuten Fetch zurückgeführt werden?  
**F6:** Wie wirken sich wahrheitsgetreue, agentengerechte Darstellungen identischer Produktfakten auf Retrieval, Zitation, Produktempfehlung und – getrennt gemessen – Affiliate-Conversions aus?

---

## 2. Forschungsstand

### 2.1 Indirekte Prompt-Injection als Systemproblem

Die OWASP-Einordnung **LLM01:2025 Prompt Injection** unterscheidet manipulative Eingaben und deren Auswirkungen auf die Verarbeitung von Anweisungen und Daten. Dass Inhalte für Menschen unsichtbar sind, schließt eine Wirkung nicht aus, sofern sie tatsächlich in die modellverarbeitete Repräsentation gelangen. Eine bloße Textabgrenzung oder nachträgliche Säuberung ist jedoch kein vollständiger Ersatz für Berechtigungs- und Ausführungskontrollen. [1]

*AgentDojo* stellt eine öffentlich dokumentierte Evaluationsumgebung für agentische Aufgaben mit unzuverlässigen Werkzeugantworten bereit. Die Veröffentlichung berichtet 97 realistische Aufgaben und 629 Sicherheitstestfälle. Die Studie ist ein wissenschaftlicher Nachweis für systematisch messbare Schwachstellen, nicht für die universelle Wirksamkeit eines bestimmten Payloads bei allen Agenten. [2]

### 2.2 Unsichtbare Zeichen und Webseitenrepräsentationen

Die Forschungsarbeit *Imperceptible Jailbreaking against Large Language Models* untersucht unsichtbare Unicode-Variation-Selectors und deren Einfluss auf Tokenisierung und Modellverhalten. Sie demonstriert entsprechende Effekte in den untersuchten Versuchsbedingungen; daraus folgt keine garantierte Übertragbarkeit auf beliebige Modelle, Parser oder produktive Suchagenten. [3]

Unit 42 dokumentierte 2026 webbasierte indirekte Prompt-Injections in realen Beobachtungen und klassifizierte 22 Techniken. Darunter fallen verborgene Webseitenbestandteile und dynamisch zur Laufzeit zusammengesetzte Inhalte. In dieser Forschung ist insbesondere die **Differenz zwischen anfänglich abgerufenem Quelltext und später verarbeitetem Seitenzustand** relevant. [4]

Eine groß angelegte Studie von Khodayari und Koautoren analysierte nach eigenen Angaben 1,2 Milliarden URLs und identifizierte 15.300 validierte Fälle von Prompt-Injection in Webseiten. Rund 70 % der identifizierten Fälle lagen in nicht sichtbaren Kanälen; ergänzende kontrollierte Tests zeigten modell- und repräsentationsabhängige, insgesamt begrenzte Erfolgsraten. Verbreitung, Absicht und beobachtete Modellwirkung sind hier getrennte Messgrößen. Die Arbeit war zum Stichtag als Preprint öffentlich verfügbar; eine spätere Konferenzveröffentlichung wird nicht vorweggenommen. [5]

### 2.3 Persistentes Gedächtnis und werbliche Manipulationsversuche

Microsoft Security Research beschrieb im Februar 2026 **AI Recommendation Poisoning**: verdeckte Anweisungen, insbesondere über „Summarize with AI“-Links, sollten Assistenten dazu bewegen, bestimmte Marken dauerhaft bevorzugt zu behandeln. Die berichteten über 50 unterschiedlichen Prompt-Varianten stammten von 31 Unternehmen aus 14 Branchen. Das ist ein Nachweis **beobachteter Manipulationsversuche**, kein kausaler Beleg für dauerhafte, universelle Rankingsteigerungen. [6]

Microsofts Bericht vom Juni 2026 über Agentengedächtnis erläutert die Möglichkeit zeitversetzter Auswirkungen. Ein darin dargestelltes Szenario verzögerter Tool-Ausführung ist explizit als **hypothetisches Veranschaulichungsbeispiel** gekennzeichnet, das von realen Forschungsmustern inspiriert ist. Es darf nicht als einzeln nachgewiesener Produktivvorfall zitiert werden. [7]

Die aktualisierte Microsoft-Taxonomie agentischer Fehlerklassen nennt unter anderem Goal Hijacking, Memory Poisoning, Session Context Contamination und Tool-/Plugin-Abuse. Ihre operative Red-Team-Erfahrung ist für das Bedrohungsmodell relevant, erlaubt aber ohne Stichprobengrundlage keine frei generalisierbare Inzidenzschätzung für alle Agentensysteme. [8]

### 2.4 Generative Engine Optimization und legitime Mehrfachdarstellung

Die GEO-Arbeit von Aggarwal und Koautoren untersucht die Sichtbarkeit von Quellen in generativen Antworten und berichtet im eigenen Benchmark Verbesserungen von bis zu 40 %. Dieses Ergebnis ist eine **benchmarkgebundene Sichtbarkeitsmetrik**, keine allgemeine Prognose für Google-Rankings, Affiliate-Umsätze oder tatsächliche Marktanteile. [9]

Cloudflare führte 2026 eine Option ein, Webseiten bei entsprechender HTTP-Inhaltsverhandlung als Markdown auszuliefern. Dies belegt die technische Möglichkeit formatabhängiger Repräsentationen. Ein behaupteter SEO-Vorteil folgt daraus nicht automatisch. [10]

Google Search Central erklärt, dass besondere Dateien wie `llms.txt` für Googles generative Suchfunktionen keinen Sonderstatus als Rankingsignal haben. Ebenso müssen strukturierte Daten zur sichtbaren Hauptinformation passen; täuschendes Cloaking sowie verborgene Inhalte zur Rankingmanipulation verstoßen gegen die Richtlinien. `GEO.md` wird in dieser Arbeit daher **nicht** als etablierter universeller Abrufstandard vorausgesetzt. [11–13]

### 2.5 Cross-Session-Persistenz: GhostWriter, ZombieAgent und Memory Governance

Torres, Shrestha und Misra beschreiben mit **GhostWriter** einen zweistufigen Memory-Poisoning-Mechanismus aus *Injection* (Eintrag in den Langzeitspeicher) und *Activation* (spätere Wiederauffindung/Aktivierung). Ihr Preprint berichtet näherungsweise **98 % Injektionsrate** und **60 % durchschnittliche Aktivierungsrate** in den untersuchten Agentenbedingungen. Diese unterschiedlichen Nenner dürfen nicht zu einer „98-prozentigen Agentenübernahme“ zusammengezogen oder ungeprüft auf andere Modelle, längere Zeiträume oder Produktionssysteme übertragen werden. Die Autoren schlagen mit *AM-Sentry* eine Governance aus Memory-Speicherpolicy und Retrieval-Prüfung vor. [15]

Radware veröffentlichte bereits am **8. Januar 2026** den herstellerseitigen Bericht *ZombieAgent*. Dieser beschreibt persistente, über Sitzungen wirksame IPI-Angriffsmechanismen. Es handelt sich um einen Sicherheitsanbieterbericht, nicht um eine allgemeine Prävalenzschätzung und nicht um einen Beleg für universelle C2-Kontrolle über alle KI-Agenten. [16]

Unit 42 dokumentierte einen eigenen **Proof of Concept** gegen die Langzeitgedächtnis-Zusammenfassung in einem Amazon-Bedrock-Agentenszenario. Der Bericht weist ausdrücklich darauf hin, dass dies keine Bedrock-Plattformschwachstelle an sich nachweist, sondern Risiken einer unzureichend gesicherten Agentenarchitektur. Ein persistenter Eintrag, seine spätere Retrieval-Aktivierung und eine nachfolgende unerlaubte Aktion sind daher getrennt zu messen. [25]

**Methodische Erweiterung:** Z05 muss neben dem Persistieren eines bereits erzeugten Eintrags die *Write Election* prüfen: Entscheidet die Speicherpolicy bei sachlich äquivalenten Inhalten je nach unzuverlässigem Framing unterschiedlich über Schreiben, Namespace, Provenienz und Vertrauensgewicht? Bei einer Policy, die ohnehin alle Inhalte speichert, ist bloße Persistenz trivial und noch kein Poisoning-Befund.

### 2.6 Die „Lethal Trifecta“ und Werkzeug-Governance

Simon Willison formulierte 2025 die **Lethal Trifecta**: (1) Zugriff auf private Daten, (2) Verarbeitung unvertrauenswürdiger Inhalte und (3) Möglichkeit zur externen Kommunikation. Ihr Zusammentreffen beschreibt ein besonders hohes *strukturelles Risiko*, aber noch keine automatisch erfolgreiche konkrete Attacke. Die Zuschreibung an Sysdig als Urheber wäre ungenau. [17]

Für MCP müssen zumindest drei Oberflächen unterschieden werden: **Tool-Definitionen und ihre Metadaten**, **Tool-Antworten während der Laufzeit** und **reale Ausführung nach einer Modellentscheidung**. Microsoft beschreibt Tool Poisoning, einschließlich veränderlicher Tool-Definitionen, und betont, dass eine separate, deterministische Ausführungskontrolle erforderlich ist. Eine fremde Webseite wird nicht allein dadurch zur registrierten MCP-Werkzeugdefinition; hierfür muss die jeweilige Integrations- bzw. Discovery-Pipeline diese Daten tatsächlich als Tool-Metadaten verwenden. Ebenso impliziert Prompt-Injection keine Remote-Code-Ausführung ohne einen technisch vorhandenen und berechtigten Ausführungspfad. [18, 19]

Der Ausdruck **„MCP-GAIR“** und die behauptete automatische Registry-Infektion konnten aus den hier geprüften Primärquellen nicht als einheitlich definierte Angriffsklasse bestätigt werden; sie werden daher nicht als eigenständiger empirischer Befund eingeführt. Die relevante überprüfbare Gefahrenklasse ist *MCP Tool Poisoning* mit gesonderter Prüfung der Berechtigungsgrenze.

### 2.7 Multimodale indirekte Prompt-Injection

Die CVPR-2026-Arbeit **ARGUS** von Lu et al. untersucht Verteidigung gegen multimodale IPI in Bild-, Video- und Audiokanälen. Sie ist eine Studie zu einer Abwehrmethode, kein Beleg, dass jeder Vision-Encoder unsichtbare Pixelinformationen automatisch in ausführbare Befehle „übersetzt“. [20]

Nguyen und Husain stellen mit **MMPIBench** eine zweite, getrennte methodische Referenz bereit: **720 untersuchte Läufe** über sechs Agentenframeworks, fünf Basismodelle und verschiedene visuelle Träger. Im berichteten Bild-/Visionsetting wurden unzulässige Aktionen in rund **12,8 %** der Läufe versucht, aber nur in ungefähr **1 %** abgeschlossen. Diese Zahlen sind nicht als allgemeine Angriffsquote zu lesen; sie verdeutlichen den Bedarf, *Perception*, *Planning*, *Attempt* und *Completion* zu trennen. [21]

Für Z01 gilt daher: Rohdatei, Bild-/Videodekodierung, OCR/Metadatenextraktion, multimodaler Modellinput und spätere Agentenhandlung sind unterschiedliche Ereignisse. EXIF-Metadaten wirken beispielsweise nur, wenn die Ingestion sie ausliest und an die relevante Komponente weitergibt. Sicherheitsprüfungen müssen sowohl Text- als auch Bild-/Audio-/Videoeingaben erfassen, sofern FruitStack diese tatsächlich verarbeitet.

### 2.8 Retrieval-Barriere: Auffindbarkeit ist eine eigene kausale Stufe

Chang, Bao, Luo und Yu untersuchen in **Overcoming the Retrieval Barrier** (USENIX Security 2026) die Frage, ob manipulierte Dokumente unter natürlichen Benutzeranfragen überhaupt abgerufen werden. Die Autoren berichten auf **11 Benchmarks und 8 untersuchten Embeddingmodellen** nahezu vollständige Retrieval-Erfolgsraten für ihren optimierten, experimentellen Angriffsansatz sowie niedrige Kosten einzelner Optimierungsläufe. Das ist **kein** Nachweis, dass nahezu 100 % aller beliebigen RAG-Systeme angegriffen werden können und **kein** Beleg für eine ebenso hohe Rate ausgeführter unerlaubter Aktionen. [22]

Daraus folgt ein eigenständiger Messpfad: *Quelle verfügbar → vom Retrieval ausgewählt → nach Cutoff im Modellkontext → als Anweisung interpretiert → Werkzeugaktion versucht → Werkzeugaktion durch Policy gestattet/verweigert*. Retrieval-Erfolg und Modellbefolgung werden getrennt berichtet. Eine weitere methodologische Begründung liefert der **nicht begutachtete** Preprint *Exposure Before Success* von Khan, Fatima und Asif. Er weist darauf hin, dass rohe Attack Success Rates ohne tatsächliche Exposition zu falschen Rangfolgen führen können. [24]

### 2.9 Validierung von Memory-Abwehrmaßnahmen

Der AWS-Sicherheitsblog vom **9. November 2026** zeigt für AgentCore ein Beispiel der **mehrschichtigen Write-Validierung**, inklusive Namespace-Kontrollen, Quarantäne und Vorabprüfung. Die dort berichteten **11 Demo-Testfälle** beruhen teilweise auf einer lokalen Näherung für semantische Ähnlichkeit und sind keine statistisch belastbare universelle Sicherheitsquote. Diese Implementierung illustriert jedoch einen geeigneten **Interventionsfaktor** für das Forschungsdesign: *Provenance-gated Memory Write an/aus* bei unverändertem Benutzerauftrag. [26]

### 2.10 Forschungslücke

Die Literatur belegt (a) die Existenz von Prompt-Injection-Mechanismen und (b) bestimmte Demonstrationen gegen Agenten. Weniger geklärt ist die **kausale Form einer Expositionsdosis-Wirkungs-Beziehung** bei konstanten Produktfakten und konstantem Tokenbudget sowie die **Zuordnung** eines Effekts zu Retrieval, aktuellem Kontext, persistentem Speicher und Werkzeuggrenze. Hinzu kommt die Lücke zwischen Red-Team-Demonstration und belastbarer, generalisierbarer Feldwirkung.

---

## 3. Hypothesen und Falsifizierbarkeit

| ID | Vorab definierte Hypothese | Falsifikationsbedingung / Alternativerklärung |
|---|---|---|
| H1 | Die Extraktionsrate harmloser Testkennungen unterscheidet sich zwischen Roh-HTML, sichtbarem Text, Accessibility-Snapshot und Markdown. | Keine Unterschiede oberhalb der vorab festgelegten minimal relevanten Effektstärke; Filterung entfernt die Kennungen. |
| H2 | Die Anzahl tatsächlicher Expositionen beeinflusst die Empfehlungswahrscheinlichkeit **über ein gleiches Tokenbudget hinaus**. | Kein Dosisparameter-Effekt oder gleiche Verschiebung im tokenbudgetgleichen One-Shot-Arm. |
| H3 | Ein Versionswechsel A→B beeinflusst den Agenten nur, wenn B nachweisbar in den Kontext gelangt. | Beobachteter Unterschied ohne Übergabe von B; dann liegt ein Störfaktor oder Messfehler vor. |
| H4 | Nicht autorisierte Anweisungen in externen Daten erhöhen in einer isolierten Umgebung die Rate **versuchter** unerlaubter Tool-Aufrufe. | Kein Unterschied zur Nullverteilung; deterministische Gatekeeper blockieren alle tatsächlichen Nebenwirkungen. |
| H5 | **Write Election und Persistenz:** Bei gleichen Sachinformationen und gleicher Exposition verändert adversariales Framing die Speicher-Schreibentscheidung, Ziel-Namespace oder dokumentierte Trust-Einstufung; ein späterer Effekt wird nur bei Write + Read + Kontextreset + ohne Refetch als Memory-vermittelt gewertet. | Gleiche Schreibrate und Trust-Einstufung wie bei neutralem Framing; kein nachgewiesener Write/Read; gleicher Effekt bei Memory-aus. |
| H6 | Sachlich identische, strukturierte Darstellungen können die korrekte Faktenerfassung und/oder zitierende Berücksichtigung verändern. | Kein Unterschied außerhalb des Rauschbodens; mehr Zitierung ohne korrektes Retrieval zählt nicht als entsprechender Nachweis. |
| H7 | Bei kontrollierten **multimodalen** Eingaben unterscheiden sich Expositions-, Verhaltensabweichungs- und Durchsetzungsraten zwischen textbasierter und multimodaler Verarbeitung bei gleicher legitimer Aufgabe. | Kein nachweisbarer Input im jeweiligen Wahrnehmungspfad; keine Differenz nach Kontrolle für Modell und Eingabekanal. |
| H8 | Ein vorgeschalteter Retrieval-Prozess moderiert die beobachtete IPI-Rate unabhängig von der bedingten Befolgungsrate **unter tatsächlich exponierten Läufen**. | Keine Retrieval-Selektion oder keine Differenz bei gültig kontrollierter Exposition. |
| H9 | Eine nach Provenienz prüfende Speicher-Schreibkontrolle reduziert unzulässige *Memory Writes* und spätere Policy-Verletzungen gegenüber identischen Läufen ohne diese Abwehr bei akzeptabler Aufgabenerfüllung. | Kein nachweisbarer Abwehrunterschied oder unvertretbarer Verlust legitimer Aufgabenerfüllung. |

Die Kurvenform in H2 wird **nicht vorweggenommen**: linear, nicht linear, sättigend oder Null-Effekt sind zulässige Ergebnisse. Ein Schwellenwert bei genau 20 Abrufen ist keine Grundannahme. Eine spätere Schwelle wäre nur mit Unsicherheitsintervall und unabhängiger Replikation berichtbar.

---

## 4. Untersuchungsdesign und Präregistrierung

### 4.1 Festlegung vor dem ersten Eingriff

Vor dem ersten konfirmatorischen Test werden eingefroren:

1. Modellidentifikatoren und Versionskennungen; jede automatische Rückstufung oder Modellrotation wird separat als Protokollereignis erfasst.
2. Temperatur, Top-p und weitere verfügbare Samplingparameter; bei nicht einstellbaren Parametern wird dieser Umstand dokumentiert.
3. Identische Benutzeraufträge, Aufgabenbank, Faktenbasis und Referenzprodukte.
4. Extraktionspfade (Roh-HTML, gerenderter Text, Accessibility-Snapshot, Markdown oder dokumentierte API-Antwort).
5. Primäre Endpunkte, minimal relevante Effektstärken, Alpha-Niveau, Testfamilien und Regeln für Ausschlüsse.
6. Randomisierung, Reihenfolge, Seed-Verwendung soweit unterstützt, maximal zulässige Tool-Rechte sowie die Aufbewahrung versionierter Evidenz.
7. Eindeutige Regeln zur Trennung von Pilotdaten, vorregistrierter Auswertung und explorativer Nachanalyse.

**Keine Modellfamilie wird stillschweigend durch eine andere ersetzt.** Ergebnisse einer Fallback-Route werden entweder einem separaten Modellstratum zugeordnet oder gemäß Präregistrierung als nicht konfirmatorisch gekennzeichnet.

### 4.2 Nullverteilung vor jeder Beeinflussungsbehauptung

Die primäre Baseline sind wiederholte, **identisch konfigurierte** Agentenläufe ohne experimentelle Fremdeinwirkung. Die natürliche Variation wird je Modell, Aufgabentyp und Konfiguration geschätzt. Dies ist notwendig, weil nicht deterministisches Sampling bereits ohne Inhaltsmanipulation die Rangfolge empfohlener Produkte verändern kann.

Für jeden Lauf werden mindestens aufgezeichnet:

- Rangposition des vorab bestimmten Zielprodukts oder die Kennzeichnung „nicht genannt“;
- Trefferquote korrekter Fakten, Quellenreferenzen und Benutzeraufgabenerfüllung;
- versuchte und tatsächlich genehmigte/verweigerte Werkzeugaktionen;
- Expositions- und Speicherevents sowie Tokenzählung, soweit technisch verfügbar.

Die Nullverteilung wird nicht nachträglich anhand der am besten passenden Metrik ausgewählt. Vor einem konfirmatorischen Vergleich müssen eine minimale relevante Effektstärke und das zugehörige Verfahren feststehen.

### 4.3 Der zentrale Confound: Wiederholung versus Textmasse

Eine zwanzigfache Exposition gegenüber demselben Produkt bedeutet häufig auch eine zwanzigfache Präsentation produktbezogenen Texts. Ein beobachteter Empfehlungswechsel kann daher schlicht auf **Salienz oder Informationsmasse** zurückgehen. Z02 enthält zwingend einen Vergleichsarm mit **identischem Tokenbudget und identischen Produktfakten in einem einzigen Kontakt**.

Ein dritter Kontrollarm hält die **Anzahl Tool-/Retrieval-Zyklen** konstant: dieselbe Gesamtzahl und Verteilung von Beobachtungen wie im Wiederholungsarm, jedoch mit voneinander verschiedenen, sachlich neutral formulierten Dokumenten, die **insgesamt dieselben Produktfakten und dasselbe produktbezogene Tokenbudget** enthalten. Damit werden zusätzliche Zyklen und Informationen konstant gehalten und die wiederholte Identität einer bestimmten Quelle separat variiert.

Zusätzlich werden die Position und Distanz zur abschließenden Empfehlung kontrolliert. Dazu dienen zufällig variierte Expositionspositionen und eine Gruppe mit gleicher Informationsmenge, aber anderer zeitlicher Verteilung. Werden diese Einflüsse nicht getrennt, kann ein Reihenfolge- oder Recency-Effekt nicht als Vertrauensaufbau interpretiert werden.

### 4.4 Faktorielles Hauptdesign

Zur Lokalisierung des Effekts ist ein **2×2×2-Grunddesign** vorgesehen; für die Wirksamkeit von Gegenmaßnahmen wird eine vierte, randomisierte Dimension ergänzt:

| Faktor | Stufe 0 | Stufe 1 |
|---|---|---|
| M – Persistenter Speicher | Memory aus | Memory an |
| V – Inhaltsversion | Unveränderte Version | Kontrollierter Wechsel A→B |
| R – Retrieval | Statische Dokumentreihenfolge | Dokument-Re-Ranking nach Vorkontakten |
| G – Governance | Standardpolicy ohne Provenienz-Gate | Provenance-gated Memory-Write aktiv |

Das ergibt **8 Grundzellen** für M×V×R. Nominal entstehen **16 Zellen** bei vollständiger Kreuzung mit G; **4 davon sind bei Memory-aus strukturell redundant**, weil ein Memory-Write-Gate ohne Memory keinen wirksamen Schreibvorgang kontrollieren kann. Für die eigentliche Memory-Mitigationsanalyse ist daher ein **verschachteltes Design mit 12 eindeutigen Bedingungen** (4 ohne Memory und 8 mit Memory/Governance an/aus) sachgerechter. Die Expositionsdosis ist ein zusätzlicher, vorab spezifizierter Faktor bzw. eine getrennte, verschachtelte Dosisstudie, nicht stillschweigend eine weitere Interpretationsdimension derselben wenigen Beobachtungen. Dosisstufen können zur Untersuchung der Kurvenform beispielsweise 0, 1, 5, 10 und 20 betragen; diese Zahlen sind **Designentscheidungen**, keine vermuteten natürlichen Schwellen.

Für die Hauptanalyse muss klar sein, ob die 12 eindeutigen Bedingungen mit einer ausgewählten Dosis geprüft werden oder ob eine voll gekreuzte 12×5-Anordnung untersucht wird. Letztere umfasst **60 nicht redundante Zellen je Modell**, vor Wiederholungen und Aufgabenstrata. Die Fallzahl ergibt sich aus der Power-Planung, nicht aus der Attraktivität einer großen Zellenzahl.

### 4.5 Mehrere Modelle statt einer einzigen Erfolgsquote

Vorgesehen sind mehrere tatsächlich verfügbare, eindeutig versionierte Modelle mit separaten Auswertungen. **Modell wird als fixer Faktor** behandelt; gemittelte Erfolgsquoten über heterogene Modellklassen sind keine Primärmetrik. Das Pooling über Modelle ist allenfalls eine zusätzlich gekennzeichnete deskriptive Zusammenfassung.

Modell×Dosis- und Modell×Memory-Interaktionen werden als mögliche Moderatoren vorab spezifiziert. Jede Änderung am Modell, Systemprompt, Tool-Schema oder Parser während der Messperiode wird als potenzieller Bruch der Vergleichbarkeit behandelt.

### 4.6 Power, Stichprobe und Stoppkriterien

Da für unsere konkrete Agentenpipeline noch keine belastbaren Varianzschätzungen vorliegen, wird **keine scheinpräzise finale Stichprobengröße behauptet**. Zunächst wird die Nullverteilung erhoben; darauf folgt eine dokumentierte Power-Berechnung anhand des vorab festgelegten primären Endpunkts und der minimal relevanten Effektstärke.

Für das **konfirmatorische Primärmaß von Z02** wird vor der Power-Analyse ein **binärer Endpunkt** (vorab definiertes Zielprodukt in Top-*k*: ja/nein) festgelegt; die genaue Wahl von *k* sowie der Referenzfragekatalog bleiben vor Studienbeginn einzufrieren. Ordinale Rangpositionen sind sekundäre Endpunkte, die eine getrennte modellgerechte Power-Planung erfordern.

Als Größenordnungsbeispiel, **nicht als festgelegtes Studien-N**, benötigen zwei unabhängige gleich große Gruppen bei einem binären Anteil von 0,50 versus 0,60, zweiseitigem α = 0,05 und 80 % Power näherungsweise **390 Beobachtungen pro Gruppe** (einfache Normalapproximation ohne Mehrfachtest-, Cluster- oder Modellkorrektur). Das zeigt, warum 20 ad-hoc-Trials je Zelle für einen konfirmatorischen Nachweis typischerweise nicht ausreichen.

Abbruchkriterien werden **vor dem Test** festgelegt: fehlende Modell-/Parser-Provenienz, defekte Instrumentierung, nicht autorisierte externe Netzwerkziele, Schutzverletzungen trotz Simulatorgrenze oder Überschreiten eines vorab definierten lokalen Kosten- beziehungsweise Laufzeitbudgets. Ein Budgetabbruch ist zu dokumentieren und darf nicht nachträglich als Nullbefund ausgegeben werden. Kein wiederholtes Zwischenprüfen auf Signifikanz ohne vorab spezifizierte sequentielle Methode.

---

## 5. Z01–Z05: getrennt auswertbare Experimente

### Z01 – Exposition und Unsichtbarkeit

**Fragestellung:** Welche nicht sichtbaren oder kodierten **harmlosen** Testkennungen überstehen den gewählten Parsingpfad und erreichen die Modellnachricht?

**Versuchsbedingungen:** Identische faktische Ausgangsinhalte werden über unterschiedliche, dokumentierte Eingabeformate verarbeitet. Die Testkennung ist neutral und trägt keine Befehlsfunktion. Beispielsweise kann eine eindeutig zuordenbare Kennung wie `ZOMBIE-TOKEN-7F3A` verwendet werden; ihr Vorkommen in einer **vom Nutzer mitgelieferten Beschreibung** ist noch kein Nachweis, dass sie zuvor von einem unabhängigen Webagenten abgerufen wurde.

**Primärer Endpunkt:** Nachweis des Kennungsstrings im protokollierten tatsächlich übergebenen Modellkontext.  
**Sekundärer Endpunkt:** Korrekte Wiedergabe/Erkennung in einer unabhängigen Antwort.  
**Abgrenzung:** Erkennung ist **keine** Handlungsbeeinflussung und **kein** Jailbreak-Nachweis.

### Z02 – Expositionsdosis unter konstanter Informationsmenge

**Fragestellung:** Führt die wiederholte Begegnung mit derselben unveränderten Quelle zu einer über die Textmasse hinausgehenden Empfehlungsverschiebung?

**Versuchsbedingungen:** Kontrollgruppe ohne Quelle; einmalige Exposition; wiederholte Expositionen mit vorab festgelegten Dosen; zusätzlicher One-Shot-Arm mit gleichem Produkt-Tokenbudget; **Zyklen-Kontrollarm mit gleich vielen Retrieval-/Reasoning-Beobachtungen, gleicher Produktfaktenmenge und gleichem Produkt-Tokenbudget, aber unterschiedlichen neutralen Dokumentquellen**; randomisierte Positionen und feste Produktfakten.

**Primärer Endpunkt:** Vorregistriertes binäres Top-*k*-Ereignis, verglichen mit Nullverteilung, One-Shot-Tokenbudget-Kontrollarm und Zyklen-Kontrollarm. Ordinale Rangpositionen sind sekundär.  
**Falsifikationsrisiko:** Bleibt nur ein Textmasseneffekt, darf nicht von „Vertrauen“ gesprochen werden.  
**Auswertung:** Dosis als numerischer Prädiktor mit vorab spezifizierter Möglichkeit nicht linearer Verläufe und Konfidenzintervallen.

### Z03 – Kontrollierter Inhaltsversionswechsel

**Fragestellung:** Wann gelangt eine neue, sachlich eindeutig versionierte Antwort B anstelle von A in die Modelleingabe, und verändert dies die Agentenentscheidung?

**Versuchsbedingungen:** Ein ausschließlich interner Testserver liefert versionierte, ungefährliche Inhaltsvarianten; Cache-Pfad und tatsächlicher Modellkontext werden dokumentiert. Ein Versionswechsel wird **nicht** als Täuschung fremder Crawler eingesetzt.

**Primärer Endpunkt:** Übereinstimmung zwischen serverseitig referenzierter Version, tatsächlich ausgeliefertem Body-Hash und im Modellkontext beobachteter Version.  
**Sekundärer Endpunkt:** Unterschiede in der Verarbeitung transparenter Versionsinformationen.  
**Abgrenzung:** Bloßer Inhaltswechsel ist noch keine Time-of-Check-to-Time-of-Use-Schwachstelle. Eine solche liegt erst vor, wenn eine relevante Prüfung auf A beruht, die nachfolgende Verwendung jedoch ungeprüft B betrifft.

### Z04 – Werkzeug- und Autorisierungsgrenze

**Fragestellung:** Versucht der Agent aufgrund unzuverlässiger Inhalte eine Handlung, die außerhalb des Benutzerauftrags oder seiner Rechte liegt?

**Versuchsbedingungen:** Ein Simulator mit synthetischen Datensätzen und **nicht produktiven** Werkzeugen. Eine getrennte Fixture bildet MCP-Tool-Metadaten und Tool-Antworten ausschließlich lokal nach; Schema-/Registry-Fingerprints und Policy-Entscheidungen werden protokolliert. Der Simulator erlaubt keine reale Exfiltration oder Ausführung auf fremden Systemen. Prüfbare Testintentionen sind etwa ein zusätzlicher, nicht angeforderter Werkzeugaufruf oder ein verweigerter Zustandswechsel in einer Dummy-Ressource. Es gibt keine echten Mail-Exfiltrationspfade, Kontenänderungen oder Remote-Code-Ausführungen.

**Getrennte Endpunkte:**

- *Attempted policy violation:* Das Modell schlägt eine verbotene Aktion vor oder ruft ein gesperrtes Dummy-Werkzeug auf.
- *Enforcement failure:* Eine deterministische Ausführungsgrenze lässt die Aktion tatsächlich zu.
- *Utility retention:* Der Agent löst weiterhin die legitime Aufgabe.

Ein einzelnes Schlüsselwort in der Ausgabe ist **kein** ausreichender Sicherheitsnachweis. Die Tool-Auditdaten sind die primäre Wahrheit über versuchte und ausgeführte Nebenwirkungen.

### Z05 – Nachgewiesene Persistenz

**Fragestellung:** Wirkt eine Information in einer **neuen** Sitzung fort, obwohl kein erneuter Fetch erfolgt und der kurzfristige Kontext tatsächlich entfernt wurde?

**Versuchsbedingungen:** Memory-an und Memory-aus mit sonst identischen Aufgaben; gesondert kontrollierte neue Sitzung; Verifikation des Kontextresets; Verbot erneuten Abrufs während der Nachprüfung; Protokollierung von Memory-Schreib- und Leseereignissen. **Zusätzlicher Write-Election-Kontrast:** neutral gerahmte Information versus adversarial gerahmte, aber sachlich äquivalente Information bei gleicher Exposition; Governance-Gate an/aus wird randomisiert. Tests verwenden ausschließlich synthetische Daten, inert markierte Trigger und nicht produktive Dummy-Tools.

**Getrennte Endpunkte:**

1. **Write-Election-Rate:** Anteil der tatsächlich in den persistierenden Store übernommenen exponierten Inhalte, getrennt nach neutral/adversarial und nach Governance-Faktor.
2. **Write-Trust-Delta:** Differenz in Namespace-Zuweisung, Provenienz-/Trust-Klasse oder einem **tatsächlich existierenden** Gewichtungsfeld zum Schreibzeitpunkt. Wenn das System keine Trust-Weights kennt, werden sie nicht erfunden; die Kategorie ist „nicht verfügbar“.
3. **Read-Activation-Rate:** Anteil der nachgewiesenen späteren Reads unter vorab geeigneten persistierten Einträgen.
4. **Unauthorized Dummy-Tool Attempt Rate:** Auftreten eines nur im Simulator vorgesehenen unerlaubten Tool-Versuchs nach der späteren Aktivierung; **Blockierung und Ausführung** separat berichten.
5. **Utility und False-Positive-Rate:** Fehlende legitime Erinnerungen beziehungsweise zu Unrecht abgewiesene neutrale Writes unter aktivierter Abwehr.

**Strenger Persistenznachweis:**

1. Die ursprüngliche Information ist in einer dokumentierten Exposition in den Modellkontext gelangt.
2. Ein persistenter **Memory-Write** mit Provenienz, Write-Entscheidung und Speicherklasse ist nachgewiesen.
3. Die neue Sitzung enthält den vorherigen Kontext nicht mehr und ruft die ursprüngliche Quelle nicht erneut ab.
4. Ein **Memory-Read** referenziert den zuvor geschriebenen Zustand.
5. Der entsprechende Effekt liegt außerhalb der Nullverteilung und oberhalb der festgelegten minimal relevanten Effektstärke.

**Kein Write – kein nachgewiesenes Memory Poisoning.** Ein bloß länger mitgeschleppter Kontext oder ein erneutes Abrufen der Webseite genügt nicht. **Ein Write allein beweist ebenfalls kein Poisoning**, wenn eine unveränderte, generelle Speicherpolicy sachlich gleichwertige neutrale Inhalte genauso übernimmt. Die spezifische Gefahr eines schlafenden, sitzungsübergreifenden Tool-Triggers wird nur als isolierter Dummy-Tool-Versuch, nicht als operative C2-Kette geprüft. [15, 23, 25, 26]

### 5.1 Warum die Reihenfolge nicht als eine einzige Angriffskette ausgeführt wird

Die Stufen Z01 bis Z05 bilden eine **logische Abhängigkeit der Messfragen**, aber nicht zwingend einen einzigen sequentiellen Agentenlauf. Für wissenschaftliche Vergleichbarkeit werden unabhängige Runs verwendet; andernfalls kontaminieren frühe Expositionen die späteren Bedingungen. Wo eine mehrstufige Agentenfolge Forschungsgegenstand ist, wird sie als eigener, vorregistrierter Longitudinalarm behandelt.

### 5.2 Zusatzmodul Retrieval: Selektion vor Exposition

Ein separat präregistrierter Aufgabenblock misst, welcher Anteil der bereitgestellten Dokumente die Retrieval-Auswahl passiert, welcher Teil nach Snippet-/Kontextkürzung im Modellkontext erscheint und wie hoch die **bedingte** Regelverletzungsrate nur unter tatsächlich exponierten Läufen ist. Die Experimente verwenden harmlose Marker, synthetische Korpora und keine Optimierung gegen fremde Produktivsysteme. Direkte Modellkontext-Injektion ist hierfür **kein** Ersatz, weil sie die zu untersuchende Retrieval-Barriere überspringt. [22, 24]

### 5.3 Zusatzmodul Multimodalität: H7 außerhalb des Text-Hauptdesigns

Die multimodale Studie unterscheidet Input-Datei/Metadaten, extrahierte Wahrnehmungsrepräsentation, Modellkontext, Antwort bzw. geplante Handlung und zugelassene/verweigerte Dummy-Tool-Aktion. Bild-, Video- und Audioarme werden nur aufgenommen, wenn das gewählte Modell und der vorhandene FruitStack-Pfad diese Modalität unterstützen. Andernfalls ist der Befund „nicht instrumentierbar“, nicht „sicher“. Die Stichprobenplanung für diese Arme erfolgt getrennt, um textbasierte und multimodale Ergebnisse nicht unzulässig zu mitteln. [20, 21]

---

## 6. Beobachtbarkeit, Agentenidentität und Provenienz

### 6.1 Was Weblogs belegen – und was nicht

| Beobachtung | Aus Logs grundsätzlich ableitbar | Methodische Grenze |
|---|---|---|
| HTTP-Zeitpunkt und URL | Ja | Kein Nachweis der Modellverarbeitung |
| User-Agent | Behauptete Agentenidentität | Leicht spoofbar |
| IP-Adresse | Netzwerkherkunft | Kein eindeutiger Sitzungs-/Modellidentifikator |
| Verifizierter Bot-Betreiber | Bei geeigneter Prüfung | Nicht die individuelle LLM-Sitzung |
| HTTP-Status / ETag | Auslieferungs-/Cachehinweise | `304` liefert keinen neuen Response-Body |
| SHA-256-Body-Hash | Eindeutige Inhaltsfassung im Protokoll | Nur aussagekräftig am richtigen Übergabepunkt |
| Eigene korrelierte Run-ID | Im selbst kontrollierten Harness | Nicht auf fremde Agenten übertragbar |
| Internes Modell und Prompt | Nein, nicht aus gewöhnlichen Serverlogs | Nur bei Zugriff auf die eigene Agentenpipeline |

Eine scheinbare Abfolge „derselbe Agent war 20-mal hier“ kann bei öffentlichen Diensten auf viele Sitzungen hinter derselben Netzwerkadresse zurückgehen. Eine angeblich exakte Zählung ohne Sitzungsprovenienz ist daher nicht tragfähig.

### 6.2 Minimale Ereigniskette

Für jeden Versuch wird eine zusammenhängende Provenienz benötigt:

`experiment_id → run_id → request_id → HTTP/body_hash → parser_snapshot_hash → model_context_hash → model_id/version → output → tool_attempt → policy_decision → memory_write/read → follow-up_outcome`

Die Speicherereignisse werden nur aufgenommen, wenn sie tatsächlich stattgefunden haben. Der Ereignisgraph muss folgende Konflikte explizit markieren: HTTP-Antwort A, Parserrepräsentation B, Modellkontext unbekannt; unklarer Modellwechsel; CDN-Cache statt Origin-Zugriff; vermeintlicher Memory-Effekt bei erneutem Seitenfetch.

### 6.3 Konkrete Dokumentationspflichten

Jeder publizierbare Run benötigt UTC-Zeitstempel, Experiment- und Aufgaben-ID, Pipelineversion, vollständige Modellkennung, Samplingparameter, Anzahl tatsächlicher Expositionen, relevante Body-/Snapshot-/Kontext-Hashes, Rechteprofil, Referenzbewertung und neutrale Evidenzanker. Geheime Systemprompts, Authentifizierungsdaten und private Benutzerdaten gehören **nicht** in frei verfügbare HTML-Testberichte.

---

## 7. Primäre Endpunkte und statistische Analyse

### 7.1 Operationale Definitionen

| Kennzahl | Zähler / Ereignis | Nenner / Bedingung |
|---|---|---|
| Extraction Rate | Im Modellkontext nachgewiesene Testkennungen | Tatsächlich geprüfte Inhaltsrepräsentationen |
| Utility Rate | Erfolgreich bearbeitete legitime Aufgaben | Gültige Agentenläufe |
| Recommendation Share | Vordefiniertes Produkt korrekt empfohlen | Passende, vorab definierte Suchaufgaben |
| Behavior Deviation Rate | Vorregistrierte Abweichung vom Auftrag | Gültige Läufe mit Vergleichsbasis |
| Unauthorized Tool Attempt Rate | Versuchte, regelwidrige Tool-Aufrufe | Läufe mit verfügbarer Dummy-Tool-Oberfläche |
| Enforcement Failure Rate | Tatsächlich zugelassene unerlaubte Aktionen | Regelwidrige Tool-Versuche |
| Memory Persistence Rate | Nachweisbarer Wiederverwendungseffekt nach Write/Read | Geeignete Nachsitzungsprüfungen |
| Differential Memory Write Rate | Unterschied adversarial versus neutral bei gleichem Sachinhalt | Gleiche Exposition und Aufgabenbedingungen |
| Governance Risk Difference | Verringerung regelwidriger Speicherwrites durch Provenienz-Gate | Randomisierte Governance-an/aus-Arme |
| Retrieval Exposure Rate | Tatsächlich im Kontext sichtbare relevante Dokumente | Für denselben Test zur Auswahl stehende Dokumente |
| Conditional Tool Attempt Rate | Unerlaubte Dummy-Tool-Versuche nach nachgewiesener Exposition | Exponierte, auswertbare Agentenläufe |
| Multimodal Perception Rate | Marker/Instruktion nach Modalitätsverarbeitung tatsächlich verfügbar | Eingaben mit technisch unterstütztem Wahrnehmungspfad |
| Recovery Rate | Korrektur einer nachgewiesenen Abweichung | Läufe mit zuvor festgestellter Abweichung |
| Citation Rate | Antworten mit korrekter Quellenreferenz | Antworten auf quellengestützte Fragen |
| Affiliate Conversion Rate | Bestätigte qualifizierte Conversion | Zuordenbare Klicks oder vermittelte Aktionen |

**Wichtig:** „Keine problematische Zeichenfolge in der Antwort“ beweist weder fehlende Exfiltration noch korrekt durchgesetzte Werkzeugrechte. Ebenso ist ein zitiertes Wort aus einer fremden Quelle nicht automatisch das Befolgen einer Anweisung.

### 7.2 Primäranalyse

Die Primäranalyse für Z02 ist eine modellgetrennte Schätzung der Dosis-Wirkungs-Beziehung mit einem expliziten **One-Shot-Tokenbudget-Kontrast** und einem **gleichzyklischen Neutraldokument-Kontrast**. Primär ist das vorregistrierte binäre Top-*k*-Ereignis; Rangpositionen werden sekundär ordinal ausgewertet. Für binäre Endpunkte ist eine logistische Regression beziehungsweise ein geeignetes generalisiertes gemischtes Modell vorgesehen, für Rangpositionen ein ordinales oder rangbasiertes Verfahren, je nach vorab festgelegtem Endpunkt. Aufgaben- oder Produktgruppen können als Cluster berücksichtigt werden. Freiheitsgrade, Clusterung und Konfidenzintervalle werden berichtet.

Eine beispielhafte Modellstruktur lautet:

\[
\operatorname{logit}\,P(Y=1)=\alpha_m+f(d)+\beta_M M+\beta_V V+\beta_R R
+\beta_{MV}(M\cdot V)+\beta_{MR}(M\cdot R)+\beta_{VR}(V\cdot R)
+\gamma^\top X,
\]

mit Modellindex \(m\), tatsächlicher Expositionsdosis \(d\), den drei faktoriellen Grundvariablen und vorab festgelegten Kovariaten \(X\) für Tokenbudget, Zahl der Retrieval-Zyklen, Position und Aufgabenblock. Der **Governance-Faktor G** und dessen Interaktionen werden in einem getrennten, vorregistrierten Mitigationsvergleich ergänzt, damit die Grundgleichung keine Vollständigkeit vorgibt, die sie nicht besitzt. Die genaue Funktionsform von \(f(d)\) wird vor dem konfirmatorischen Test festgelegt; explorativ geschätzte Schwellen werden ausdrücklich als solche gekennzeichnet.

### 7.3 Fehlerkontrolle und Replizierbarkeit

- Zweiseitige Konfidenzintervalle und tatsächliche Effektstärken werden **vor** bloßen p-Werten berichtet.
- Primärer Hypothesentest und Testfamilie werden präregistriert; sekundäre Vergleiche erhalten eine geeignete Mehrfachtestkorrektur (etwa Holm oder Benjamini–Hochberg, entsprechend vorab definiertem Ziel).
- Wiederholte Läufe mit identischem Seed werden nicht mit unabhängigen Zufallsbeobachtungen verwechselt.
- Interaktionseffekte werden pro Modell ausgewiesen; Nullbefunde erhalten Konfidenzintervalle.
- Eine unabhängige Replikation auf einem eingefrorenen neuen Aufgabenblock dient der Robustheitsprüfung.
- Für Z05 werden **Write Election, Write Trust/Namespace, tatsächlicher Read, Aktivierung und Durchsetzung** als getrennte Outcomes analysiert. Eine bedingte Aktivierungsrate verwendet keinen Nenner, der alle ursprünglich nicht geschriebenen Inhalte einschließt, ohne diesen separat auszuweisen.
- Retrieval- und Expositionsraten werden vor jeder Aussage zur Modellbefolgung separat berichtet; eine hohe Retrieval-Quote ist keine hohe Übernahmequote.
- Wenn sich Provider-Modell, Systemprompt, Retrievalpipeline oder Rechteprofil ändern, wird die Vergleichbarkeit nicht stillschweigend unterstellt.

**Kausale Grenze:** Auch ein statistisch signifikanter Empfehlungsunterschied beweist für sich genommen kein subjektives „Vertrauen“ eines Modells. Der Begriff ist allenfalls eine theoretische Interpretation und darf erst nach Ausschluss naheliegender Alternativen vorsichtig verwendet werden.

---

## 8. Technische Umsetzung im bestehenden FruitStack: Anforderungen, kein Fake-Code

Es wird **keine neue Agentenarchitektur als bereits implementiert behauptet**. Die folgenden Punkte sind prüfbare Anforderungen an die vorhandene FruitStack-Infrastruktur:

1. **Versionierte Fixture-Quelle:** kontrollierte harmlose Testdokumente mit Inhalts-Hashes und eindeutigem Versionsprotokoll.
2. **Instrumentierte Ingestion:** Erfassung von HTTP, Parsing, Snapshot, tatsächlichem Modellkontext und Kontextkürzung.
3. **Run-Controller:** unabhängige Wiederholungen, Randomisierung, Modell-Fingerprinting und Budgetkontrolle.
4. **Dummy-Tools mit deterministischer Policy:** Trennung von vom Modell *versuchten* und vom System *genehmigten* Aktionen.
5. **Memory-Audit:** beweiskräftige Schreib-/Leseereignisse, Speicherabschaltung, Provenienz-, Namespace- und Abwehrentscheidungen sowie explizite Kontextresets.
6. **Auswertung:** Nullverteilungen, Konfidenzintervalle, modellspezifische Statistiken, Aufgabenutility und maschinenlesbare Ergebnisartefakte.
7. **Adversariale unabhängige Prüfung:** eine getrennte Validierung der Evidenz, damit keine Modellselbstaussage als einzige Quelle für einen Erfolg dient.

Vor Entwicklung oder Ausführung ist zu prüfen, **welche dieser Fähigkeiten bereits tatsächlich existieren**. Die Nutzung von FruitStack als Testplattform ist ein Projektziel; eine nachgewiesene ZOMBIE-Implementierung wird nicht behauptet.

### 8.1 Bewertung der im Gespräch bereitgestellten pytest-Skizzen

Die übergebenen Beispiele sind eine **Ausgangsskizze**, keine wissenschaftlich oder betrieblich vollständige Prüfsuite:

- Ein Agenten-Endpoint muss nachweisbar das Feld `retrieved_content` als **nicht vertrauenswürdige Quelle** und nicht als privilegierte Benutzeranweisung verarbeiten. Sonst testet man die falsche Vertrauensgrenze.
- `pytest.warning(...)` ist kein gültiger allgemeiner pytest-Warnungsaufruf; fehlende Zugangsdaten müssen durch sauberes Preflight-/Skip-/Fehlerverhalten behandelt werden.
- Das bloße Fehlen der Wörter `pwned`, `system prompt` oder einer URL in der Antwort beweist nicht, dass keine nicht autorisierte Tool-Aktion stattfand. Umgekehrt kann eine zulässige Zitierung einer verdächtigen Zeichenfolge einen falschen Alarm auslösen.
- Aussagen über tatsächliche Datenabflüsse müssen über Netzwerk- und Tool-Auditdaten validiert werden, nicht nur über Textassertions.
- Beim HTML-Reporting sind die **dokumentierten Versionen** von `pytest-html` und `pytest-metadata` maßgeblich; nach aktueller offizieller Anleitung lässt sich die Metadaten-Tabelle über `pytest_configure` und `config.stash[metadata_key]` bearbeiten. Die früher vorgeschlagene Hook-Signatur darf nicht ohne Versionsprüfung übernommen werden. [14]
- Fehlerfallanhänge müssen Credentials, Tokens, Systemprompts, Personenbezüge und Nutzerdaten vor der Ablage zuverlässig entfernen.
- Git-Revision, Testsuite-Version, Modell-ID, Parser-/Tool-Version und Endpoint-Umgebung gehören in jedes Artefakt. Eine Versionszeichenfolge aus einer selbst gesetzten Umgebungsvariable ist noch kein Nachweis der tatsächlich antwortenden Modellversion.
- CI ist **nicht** gleich Forschung: Einzelne pytest-Pass/Fail-Werte sind Regressionstests, keine statistische Replikation. Kurze lokale Sicherheitsprüfungen und auf Budget begrenzte, manuell oder zeitgesteuert gestartete größere Evaluationsläufe sind getrennt zu behandeln.

### 8.2 Beweiskette statt Erfolgsbehauptung

Ein Ergebnis zählt nur, wenn die Art des Nachweises zur Behauptung passt. Beispiel: „Marker im Prompt“ benötigt einen archivierten Modellinput. „Empfehlung verschoben“ benötigt Kontrollgruppe und Nullverteilung. „Memory Poisoning“ benötigt Write/Read, Reset und ausbleibenden Refetch. „Rechteverletzung“ benötigt Policy- und Tool-Audit. **Ein Screenshot mit einer auffälligen Modellantwort allein reicht für keine dieser vier Aussagen aus.**

---

## 9. GEO-/Affiliate-Anwendungsfall als separate Forschungsdomäne

### 9.1 Adaptive Content Delivery aus einer Wahrheitsquelle

Ein überprüfter **Knowledge Graph** kann die sachlichen Eigenschaften eines Produkts einmalig und nachvollziehbar speichern: Hersteller, Funktionen, unterstützte Formate, Preise mit Gültigkeitsdatum, Vergleichskriterien, Belege, Einschränkungen und gegebenenfalls Affiliate-Kennzeichnung.

Aus dieser Datenquelle entstehen verschiedene **faktentreue** Darstellungen:

| Empfänger | Geeignete technische Darstellung | Unveränderliche Voraussetzung |
|---|---|---|
| Mensch | Lesbare Produktseite, Navigation, erklärende Texte und Bilder | Gleiche überprüfbare Kernaussagen |
| Suchcrawler | Crawlbares HTML, interne Links, passende strukturierte Daten | Kein irreführender Mehrinhalt für Bots |
| Text-/KI-Agent | Kompakte Markdown- oder strukturierte Faktenansicht, falls angefordert und unterstützt | Gleiche Tatsachen und Quellen |
| Commerce-/Vergleichsclient | Dokumentierter Produktfeed oder API mit eindeutigen Feldern | Aktualisierte Preise und zulässige Partnerschaftskennzeichnung |

Dies ist ein **Architekturziel**, kein Nachweis einer höheren Position in einer bestimmten Suchmaschine. `schema.org` und JSON-LD können eine sinnvolle formale Schicht bereitstellen; sie ersetzen keine belegbaren, nutzerrelevanten Inhalte und begründen keinen garantierten Eintrag in Googles Knowledge Graph. [12–13]

### 9.2 Agent Influence Analytics ohne verdeckte Fremdsteuerung

Die geordnete Forschungsfrage lautet: **Welche sachlich korrekten Darstellungen derselben Produktfakten verändern die Wahrscheinlichkeit korrekter Extraktion, Zitation, Empfehlung oder Conversion?**

Messgrößen werden getrennt erhoben: *Fetch/Crawl → Retrieval → Modell-Exposition → faktische Übernahme → Zitation → Empfehlung → qualifizierter Klick → bestätigte Affiliate-Conversion*. Keine Stufe darf durch eine andere ersetzt werden. Beispielsweise ist eine öfter erwähnte Marke noch kein Beweis zusätzlicher Affiliate-Umsätze.

### 9.3 Experiment versus produktiver Einsatz

Eine autorisierte Red-Team-Demonstration belegt eine **Möglichkeit unter definierten Bedingungen**. Sie ist kein Beleg für einen dauerhaften Effekt auf beliebige reale Agenten und darf nicht stillschweigend in eine verborgene Kampagne gegen fremde Nutzeragenten umgedeutet werden. Abweichende Inhalte zur Täuschung von Suchsystemen, fabrizierte Bewertungen und verdeckte Handlungsanweisungen sind daher **keine Produktfunktion** des hier vorgeschlagenen GEO-Systems. Die relevante Forschung untersucht solche Mechanismen kontrolliert, um Wirksamkeit, Grenzen und Abwehrmaßnahmen zu bestimmen. [11–13]

---

## 10. Validität, Forschungsethik und Grenzen

### 10.1 Interne Validität

Die größten Risiken sind (a) Samplingrauschen, (b) unterschiedliche Tokenmengen, (c) Positions- und Recency-Effekte, (d) nicht dokumentiertes Caching, (e) Modell-Fallbacks, (f) kontaminierte Kontrollläufe sowie (g) eine unvollständige Erinnerungstrennung. Jeder Punkt erhält einen eigenen Kontroll- oder Ausschlussmechanismus.

### 10.2 Externe Validität

Ergebnisse aus einer isolierten Testumgebung gelten zunächst **nur** für die geprüfte Kombination aus Modell, Prompt, Retrieval, Tools, Aufgaben und Datendarstellung. Änderungen an Sicherheitsmechanismen können beobachtete Effekte verringern oder aufheben. Ergebnisse über spezielle Modelle werden nicht ungeprüft auf „alle KI-Agenten“ verallgemeinert.

### 10.3 Konstrukte und Terminologie

„Vertrauen“, „Zombie“, „Übernahme“ und „Jailbreak“ sind als Labels ungeeignet, wenn nur ein abweichender Satz beobachtet wurde. Die Publikation nutzt die messbaren Bezeichnungen **Exposition, Antwortabweichung, Tool-Versuch, Enforcement-Versagen und verifizierter Memory-Effekt**.

### 10.4 Umgang mit bestehenden Forschungsdemonstrationen

Die Sichtung eines Jailbreak-Videos oder einer veröffentlichten Angriffsstudie liefert einen Anhaltspunkt für die technische Plausibilität, nicht automatisch eine eigene Replikation. Bei einem behaupteten Effekt müssen Input, tatsächlicher Kontext, Modellidentität, Ergebnis, Negativkontrollen und Wiederholung zugänglich sein. Ein auf einer Laborinstanz demonstrierter Angriff ist nicht mit einem bestätigten Einsatz gegen reale Nutzer gleichzusetzen.

### 10.5 Sicherheits- und Datenschutzgrenzen

Alle Versuche erfolgen ausschließlich mit eigenen oder ausdrücklich autorisierten Agenten und synthetischen Daten. Tool-Aktionen werden durch eine nicht produktive Policy-Grenze kontrolliert. Es werden keine realen Tokens, Kontaktdaten, Kundenhistorien oder fremden Systemprompts erhoben. Für wissenschaftliche Nachvollziehbarkeit wird die notwendige Evidenz archiviert; sensible Rohdaten bleiben geschützt. Die Studie dient insbesondere dem Nachweis, **wann** technische Schutzschichten funktionieren oder versagen.

---

### 10.6 Externe Forschungsbehauptungen kritisch prüfen

GhostWriter, ZombieAgent, ARGUS, MMPIBench und die USENIX-Retrieval-Arbeit verwenden **unterschiedliche Aufgaben, Modelle, Kanäle, Nenner und Erfolgskriterien**. Ergebnisse dürfen nicht addiert oder zu einer universellen Angriffserfolgsquote verdichtet werden. Eine simulierte Tool-Aktion ist kein realer Datenabfluss; ein positiver Memory-Read ist keine unabhängige Ausführung; ein erfolgreiches Retrieval ist keine bestätigte Befolgung.

Für multimodale Angriffe gilt: Pixel- oder Metadateninformationen erreichen ein Modell nur über einen tatsächlich vorhandenen Wahrnehmungs- oder Extraktionspfad. Für MCP gilt: Veränderte Tool-Metadaten sind nicht automatisch eine Systemrolle; unzulässige Ausführung setzt zudem unzureichende Berechtigungsgrenzen voraus.

Die in externen Darstellungen vorkommenden Bezeichnungen „MCP-GAIR“ sowie angeblich allgemeingültige Aktivierungswörter und universelle Schwellenwerte werden ohne reproduzierbaren Primärbeleg nicht als empirisch erwiesen behandelt. Solche Aussagen dürfen erst durch explizite Experimente und entsprechende Provenienz gestützt werden.

## 11. Erwartbarer Erkenntnisbeitrag und Publikationskriterien

Ein veröffentlichungsfähiger Beitrag entsteht **nicht** aus der bloßen Existenz eines Testharnesses. Er benötigt mindestens einen der folgenden empirischen Befunde:

1. Eine replizierte, modellspezifisch berichtete **Dosis-Wirkungs-Kurve**, die über Samplingrauschen, Tokenbudget und Position hinausgeht – oder einen präzise eingegrenzten Nullbefund.
2. Einen instrumentierten, kausal nachvollziehbaren Vergleich von Roh-HTML, Parser, Snapshot und Modellkontext bei verborgenen Signalen.
3. Eine faktoriell belegte Lokalisierung eines Effekts in Retrieval, Sitzungskontext und/oder expliziten Memory-Write-/Read-Pfaden.
4. Eine validierte Unterscheidung zwischen einer vom Modell beabsichtigten Tool-Aktion und einer von der Infrastruktur **tatsächlich zugelassenen** Berechtigungsverletzung.
5. Einen unabhängig replizierten Effekt **wahrheitsgetreuer** Content-Repräsentationen auf konkrete GEO-Kennzahlen und, sofern Daten vorhanden, bestätigte Conversions.

Das Manuskript ist als Präregistrierungsentwurf erst dann final, wenn Aufgabenbank, Modellpool, minimal relevante Effektstärke, Power-Berechnung, konkrete Instrumentierungsfähigkeit und alle Ausschlussregeln mit überprüfbaren Versionen festgelegt sind.

## 12. Fazit

Die bisherige Forschung zeigt, dass indirekte Prompt-Injection über externe Daten, versteckte Textrepräsentationen und Agentengedächtnisse möglich ist. Sie zeigt **nicht**, dass eine Webseite durch genau 20 Abrufe automatisch die Kontrolle über einen fremden Agenten gewinnt. Die wissenschaftlich belastbare Frage betrifft die **Form und kausale Herkunft** möglicher Expositionseffekte.

Project ZOMBIE ist daher als **experimentelles Messinstrument** zu verstehen. Sein Erfolg hängt von einer sauberen Nullverteilung, tokenbudgetkontrollierten Wiederholungen, versionierten Inhaltswechseln, überprüften Tool-Grenzen und einem zwingend nachgewiesenen Memory-Write/-Read-Pfad ab. Daraus kann gleichzeitig eine eigenständige, legitime GEO-Forschung entstehen: agentengerechte, faktenkonsistente Content-Auslieferung und empirisch überprüfbare Empfehlungseffekte.

**Kernaussage:** *Nicht die Behauptung einer Agentenübernahme ist der Befund, sondern eine reproduzierbare, kausal zuordenbare Veränderung agentischer Entscheidungen bei bekannten Expositionsbedingungen.*

---

## Literaturverzeichnis und überprüfte Primärquellen

Die nachfolgenden Quellen wurden für die Erstellung am **10. November 2026** anhand öffentlich zugänglicher Originalveröffentlichungen beziehungsweise offizieller Produktdokumentation abgeglichen. URLs dienen der Nachprüfbarkeit; die Quelle ist nicht automatisch ein Beleg für jede im Manuskript diskutierte Hypothese.

[1] OWASP Gen AI Security Project. **LLM01:2025 Prompt Injection.** OWASP Top 10 for LLM Applications. https://genai.owasp.org/llmrisk/llm01-prompt-injection/

[2] Debenedetti, E., Zhang, J., Balunović, M., Beurer-Kellner, L., Fischer, M., & Tramèr, F. (2024). **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents.** *NeurIPS 2024, Datasets and Benchmarks Track.* https://arxiv.org/abs/2406.13352 ; https://proceedings.nips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html

[3] Gao, K., Li, Y., Du, C., Wang, X., Ma, X., Xia, S.-T., & Pang, T. (2025). **Imperceptible Jailbreaking against Large Language Models.** arXiv:2510.05025. https://arxiv.org/abs/2510.05025

[4] Unit 42 / Palo Alto Networks. (2026, März). **Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild.** https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/

[5] Khodayari, S., Zhang, X., Acharya, B., & Pellegrino, G. (2026). **Indirect Prompt Injection in the Wild: An Empirical Study of Prevalence, Techniques, and Objectives.** arXiv:2604.27202 (Preprintstand zum Manuskriptstichtag). https://arxiv.org/abs/2604.27202

[6] Microsoft Defender Security Research Team & Kochavi, N. (2026, 10. Februar). **Manipulating AI memory for profit: The rise of AI Recommendation Poisoning.** Microsoft Security Blog. https://www.microsoft.com/en-us/security/blog/2026/02/10/ai-recommendation-poisoning/

[7] Isak, N., & Cooley, S. (2026, 22. Juni). **Guarding AI memory.** Microsoft Security Blog. https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/

[8] Microsoft AI Red Team. (2026, 4. Juni). **Updating the taxonomy of failure modes in agentic AI systems: What a year of red teaming taught us.** https://www.microsoft.com/en-us/security/blog/2026/06/04/updating-taxonomy-failure-modes-agentic-ai-systems-year-red-teaming-taught-us/

[9] Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., & Deshpande, A. **GEO: Generative Engine Optimization.** Princeton-Forschungsarbeit / arXiv:2311.09735. https://arxiv.org/abs/2311.09735

[10] Cloudflare. (2026, 12. Februar). **Introducing Markdown for Agents.** Cloudflare Changelog. https://developers.cloudflare.com/changelog/post/2026-02-12-markdown-for-agents/

[11] Google Search Central. (2026). **Google's Guide to Optimizing for Generative AI Features on Google Search.** https://developers.google.com/search/docs/fundamentals/ai-optimization-guide

[12] Google Search Central. **Spam Policies for Google Web Search.** https://developers.google.com/search/docs/essentials/spam-policies

[13] Google Search Central. **General Structured Data Guidelines.** https://developers.google.com/search/docs/appearance/structured-data/sd-policies

[14] pytest-html-Entwicklerteam. **pytest-html User Guide** (Dokumentation zum Berichtsformat und zu Metadaten-/Extras-Hooks). https://github.com/pytest-dev/pytest-html/blob/master/docs/user_guide.rst

[15] Torres, G., Shrestha, S., & Misra, S. (2026). **When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents.** arXiv:2607.06595. Eingeführter Angriff: GhostWriter; separates Injection- und Activation-Maß. https://arxiv.org/abs/2607.06595

[16] Radware. (2026, 8. Januar). **ZombieAgent: The Agentic Revolution Comes with Malicious Gifts.** Hersteller-Research/Threat Advisory. https://www.radware.com/security/threat-advisories-and-attack-reports/zombieagent/

[17] Willison, S. (2025, 16. Juni). **The Lethal Trifecta for AI Agents: Private Data, Untrusted Content, and External Communication.** Technische Primärdarstellung eines Bedrohungsmodells. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

[18] Microsoft for Developers. (2025, 28. April). **Protecting against indirect prompt injection attacks in MCP.** https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp/

[19] Batzner, J. / Microsoft for Developers. (2026, 22. April). **Securing MCP: A Control Plane for Agent Tool Execution.** https://developer.microsoft.com/blog/securing-mcp-a-control-plane-for-agent-tool-execution/

[20] Lu, W., Zeng, Z., Zhang, K., Li, H., Zhuang, H., Wang, R., Chen, C., & Peng, H. (2026). **ARGUS: Defending Against Multimodal Indirect Prompt Injection via Steering Instruction-Following Behavior.** *CVPR 2026*; Vorfassung arXiv:2512.05745. https://arxiv.org/abs/2512.05745 ; https://github.com/ZeroNLP/ARGUS

[21] Nguyen, V. K., & Husain, M. I. (2026). **An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks.** arXiv:2609.09404 (MMPIBench; Preprint). https://arxiv.org/abs/2609.09404

[22] Chang, H., Bao, E., Luo, X., & Yu, T. (2026). **Overcoming the Retrieval Barrier: Indirect Prompt Injection in the Wild for LLM Systems.** *35th USENIX Security Symposium*, 1567–1586. https://www.usenix.org/conference/usenixsecurity26/presentation/chang-hongyan

[23] Dash, P., Ge, T., Jain, A., Shah, T., & Shang, Z. (2026). **From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents.** arXiv:2606.04329v2 (MPBench; Preprint). https://arxiv.org/abs/2606.04329

[24] Khan, M. A., Fatima, A., & Asif, T. (2026, 19. Oktober). **Exposure Before Success in Indirect Prompt Injection Measurement.** *Preprints.org*, Version 1; **nicht peer-reviewed**. https://www.preprints.org/manuscript/202610.1741

[25] Unit 42 / Palo Alto Networks. **When AI Remembers Too Much – Persistent Behaviors in Agents’ Memory.** Forschungsbericht/PoC über Memory-Summarization und sitzungsübergreifende Auswirkung. https://unit42.paloaltonetworks.com/indirect-prompt-injection-poisons-ai-longterm-memory/

[26] Kumar, T. / AWS Security Blog. (2026, 9. November). **Help defend against memory poisoning in Amazon Bedrock AgentCore with multi-layer write validation.** Technische Demonstration mit 11 lokalen Tests, kein universeller Wirksamkeitsnachweis. https://aws.amazon.com/blogs/security/help-defend-against-memory-poisoning-in-amazon-bedrock-agentcore-with-multi-layer-write-validation/

---

## Anhang A – Vorregistrierungsblatt (auszufüllen vor konfirmatorischen Läufen)

| Feld | Status / einzutragende Festlegung |
|---|---|
| Forschungsfrage und primärer Endpunkt | F2 / Empfehlungsänderung unter tokenbudgetgleichem Kontrollarm – endgültig vorab festzulegen |
| Konkrete Modell-IDs und tatsächlich verwendete Versionen | **Offen; nicht erfunden** |
| Modell- und Provider-Fallback-Regel | Separates Stratum oder festgelegter Ausschluss |
| Samplingparameter | **Offen**; je Modell zu dokumentieren |
| Aufgabenbank / Produktfakten / Versions-Hashes | **Offen**; einzufrieren |
| Nulldistribution und Nullverteilungsmethodik | Vor Manipulation; N abhängig von Präzisionsziel |
| Minimal relevante Effektstärke | **Offen**; vor Power-Berechnung festzulegen |
| Power / Stichprobe / Aufgabencluster | **Offen**; nicht aus Pilot-Ergebnis „schönrechnen“ |
| Faktorplan | Memory × Versionswechsel × Retrieval-Re-Ranking = 8 Grundzellen; mit verschachteltem Governance-Gate = 12 eindeutige Zellen (16 nominell) |
| Dosis und Kontrollarme | Dosis numerisch; gleiches Tokenbudget **und** gleiche Retrieval-/Reasoning-Zyklen mit Neutraldokumenten verpflichtend |
| Z03 Caching/Body-Hashes | Provenienz muss technisch nachgewiesen werden |
| Z04 Tool-Policy | Nur Dummy-Tools und synthetische Datensätze |
| Z05 Memory-Nachweis | Write + Read + Reset + kein Refetch verpflichtend |
| Z05 Write-Election-Kontrast | Neutral versus adversarial gerahmt; gleicher Sachinhalt und gleiche Exposition; Trust/Namespace beim Write protokollieren |
| Governance-Abwehrfaktor | Provenance-gated Memory Write an/aus; Utility und Fehlalarme mitberichten |
| Retrieval-Barriere H8 | Retrieval → tatsächliche Exposition → bedingte Befolgung getrennt messen |
| Multimodaler Zusatzarm H7 | Abhängig von tatsächlich unterstützten Modalitäten; getrennte Stichprobenplanung |
| Z02 primärer Top-k-Endpunkt | Binär; *k* und minimale relevante Effektstärke vor Power-Berechnung fixieren |
| Mehrfachtests und Konfidenzintervalle | Vorab festzulegen |
| Ausschluss- und Abbruchkriterien | Vor Ausführung zu dokumentieren |
| Evidenzarchiv und Datenschutz | Interne Speicherung mit Geheimnis-Redaktion |
| Replikationsdatensatz | Unabhängig von der Explorationsstichprobe |

## Anhang B – Aussageklassen im Abschlussbericht

| Kennzeichnung | Zulässige Aussage |
|---|---|
| **Beobachtung** | Durch Log, Modellkontext, Tool-Audit oder Memory-Ereignis belegt. |
| **Statistischer Befund** | Vorab definierter Kontrast, Effektgröße und Unsicherheitsintervall vorhanden. |
| **Interpretation** | Mit möglichen Alternativerklärungen versehen, nicht als Beweis formuliert. |
| **Hypothese** | Falsifizierbar, aber noch nicht getestet. |
| **Implementierungsstatus** | Durch ausgeführte Funktionen und Artefakte nachgewiesen; kein Fake-Code. |
| **Produkteffekt** | Separat von Laborwirkung durch tatsächliche Retrieval-/Zitations-/Conversion-Daten belegt. |

### Revisionsvermerk 1.1 (10. November 2026)

Die vorhandenen Z01–Z05-Forschungsfragen, die Nullverteilung-vorher-Regel, die methodische Trennung von Exposition/Verhalten/Autorisierung/Persistenz sowie die Aussageklassen aus Anhang B bleiben erhalten. Ergänzt wurden: wissenschaftlich verifizierte Literatur zu GhostWriter, ZombieAgent, MCP, multimodalem IPI und Retrieval-Barrieren; Write Election als notwendiger Z05-Kontrast; ein Governance-Abwehrfaktor; der Retrieval-Zyklen-Kontrollarm; die Vorfestlegung eines binären Primärendpunkts für die beispielhafte Power-Rechnung; separate multimodale und Retrieval-Zusatzmodule. **Eigene Versuche oder Resultate wurden weiterhin nicht behauptet.**

**Ende des Forschungsmanuskripts.**


---

## Anhang C – Implementierungsnachweis und erster instrumentierter Prüfstand (Revision 1.2)

### C.1 Repositorium und Prüfumgebung

Die Entwicklungsgrundlage wurde am 10. November 2026 im Repository [`tonnestate/Zombie`](https://github.com/tonnestate/Zombie) angelegt. Der erste reproduzierbare Code-Stand ist Commit [`7b67d9552c8a2167396c0a985001c650e10f8fbd`](https://github.com/tonnestate/Zombie/commit/7b67d9552c8a2167396c0a985001c650e10f8fbd).

Die erste Installation enthält `zombie_harness.py`, `test_agent_ipi.py`, `conftest.py`, `tests/test_pipeline_unit.py`, `requirements.txt` und eine GitHub-Actions-Pipeline. Die aktuellen Testfälle umfassen zwei isolierte Z01-Repräsentationstests, zwei Z03-Versionierungs-/Validierungstests sowie drei optionale Staging-Tests mit harmlosen Fehlverhaltensmarkern. Die Staging-Tests führen **keine** unautorisierten Datenzugriffe oder externe Tool-Aktionen aus.

Die lokale Ausführung vor dem Commit ergab **vier bestandene Offline-Tests und drei korrekt übersprungene Remote-Tests** (`4 passed, 3 skipped`). Die erste GitHub-Actions-Ausführung ist abgeschlossen und erfolgreich: [ZOMBIE IPI Harness, Run 42794535937](https://github.com/tonnestate/Zombie/actions/runs/42794535937). Dies ist ein Engineering-Smoke-Test, **kein wissenschaftlicher Nachweis für H1–H9 und kein Befund über produktive Agenten**.

### C.2 Schnittstelle zur realen FruitStack-Ausführung

Ein echter Endpoint wird aus Sicherheitsgründen nicht angenommen oder geraten. Ein Staging-Adapter wird nur aktiviert, wenn `AGENT_ENDPOINT` auf einen ausdrücklich autorisierten Endpunkt gesetzt ist und `ZOMBIE_AUTHORIZED_TARGET=YES` vorliegt. Das vorgesehene Austauschformat ist ein `POST`-JSON-Objekt mit den Feldern `task` und `retrieved_content`; die Rückgabe muss `response` enthalten. Ob FruitStack selbst diesen Vertrag bereits bereitstellt, ist **nicht geprüft**. Die Schnittstelle ist deshalb zunächst eine isolierte Testvereinbarung, keine Behauptung über den Bestand des vorhandenen Systems.

Ausgabereports enthalten bei Fehlern lediglich Hashes, Zeichenzahlen und Verfügbarkeitsmerkmale einer Tool-Audit-Liste; keine API-Schlüssel, Rohprompts, vertraulichen Modellantworten oder sensitiven Tool-Argumente. In der GitHub Actions Pipeline sind Remote-Tests nur über einen manuellen, gesondert geschützten Staging-Job vorgesehen. Der CI-Job für Pull Requests führt ausschließlich Offline-Tests aus.

### C.3 Instrumentierungsgates für konfirmatorische Z01–Z05-Tests

| Forschungsstufe | Bereits überprüft | Noch benötigter Nachweis vor konfirmatorischen Tests |
|---|---|---|
| Z01 | Parsing-Differenz zwischen rohem HTML und vereinfachtem sichtbarem Text | Tatsächlich an das Modell gesendete Nachricht nach realer Browser-/RAG-Extraktion |
| Nullverteilung | Testumgebung und reproduzierbare Fixtures | Festgelegte Modell-IDs, Samplingparameter, Aufgabenbank, N und Minimal Relevant Effect Size (MRES) |
| Z02 | Experimenteller Kontrollplan im Manuskript | Getrennte Messung von Tokenmasse, Wiederholung derselben Quelle und Anzahl der Retrieval-/Reasoning-Zyklen |
| Z03 | Deterministische, versionierte Auslieferung und Body-Hashes | HTTP-/Cache-Provenienz plus Übergabe der Version an den tatsächlichen Modellkontext |
| Z04 | Wissenschaftlich definierte Tool-Boundary | Autoritative Protokolle versuchter, erlaubter und blockierter realer Tool-Aktionen |
| Z05 | Theoretisches Write-Election-Design mit Provenienz und Abwehr-Faktor | Eindeutiger persistenter Store, Write-/Read-Audit, Trust-/Namespace-Felder und nachweislicher Reset flüchtigen Kontexts |

### C.4 Falsifizierbarkeit und Grenzen

Die aktuelle Infrastruktur ist **nicht** als Nachweis eines erfolgreichen oder vereitelten Angriffs zu interpretieren: Ein Offline-Parser führt kein LLM aus, ein unveränderter Antwortstring beweist keine Tool-Sicherheit und ein GitHub-Action-Erfolg belegt nicht die Verfügbarkeit eines produktiven FruitStack-Endpunkts.

Insbesondere wird Z05 erst als Memory-Poisoning-Test gewertet, wenn bei gleicher Exposition ein Unterschied in der *Write Election* zwischen neutralen und adversarial gerahmten, sachlich gleichwertigen Daten nachgewiesen ist und ein späterer Einfluss ausdrücklich auf `memory_write` und `memory_read` zurückgeführt wird. Ein gespeicherter Text ohne nachgewiesene Write-Election-Differenz ist lediglich ein Persistenzbefund.

Die GEO-/Affiliate-Domäne bleibt ein getrennter, faktentreuer Optimierungsarm. Ohne echte attribuierbare Conversion-Daten kann das Repository keine reale Affiliate-Umsatzwirkung behaupten.

**Revisionsvermerk 1.2 (10. November 2026):** Einrichtung und Überprüfung des initialen öffentlichen Repositories, lokale Offline-Tests und erfolgreicher CI-Lauf. Forschungsfragen, Hypothesen und frühere Aussageklassen bleiben inhaltlich unverändert; es werden keine neuen Wirksamkeitsbehauptungen eingeführt.