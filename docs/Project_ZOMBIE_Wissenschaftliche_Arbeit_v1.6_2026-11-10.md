---
title: "Project ZOMBIE: Expositionsdosis, Kontextprovenienz und Persistenz fremder Information in autonomen KI-Agenten"
subtitle: "Forschungsstand, Präregistrierung und Cross-Layer-Analyse vom einzelnen Byte bis zur systemischen Wirkung"
date: "2026-11-10"
status: "Forschungsmanuskript und Präregistrierungsentwurf – keine experimentellen ZOMBIE-Ergebnisse"
language: "de"
version: "1.5"
keywords:
  - Indirect Prompt Injection
  - Agentic AI
  - Memory Poisoning
  - Dosis-Wirkung
  - Knowledge Graph
  - GEO
  - Kausalinferenz
  - Reproduzierbarkeit
  - Cross-Layer Trust Transitions
  - Harness Integrity
  - Agent Binding
  - OS- und Ausführungsgrenzen
  - Systemische Rückkopplung
---

# Project ZOMBIE: Expositionsdosis, Kontextprovenienz und Persistenz fremder Information in autonomen KI-Agenten

**Forschungsmanuskript und Präregistrierungsentwurf**  
**Stand:** 10. November 2026 · **Revision 1.4 (Mikro-zu-Makro-Erweiterung: Bindungsverlust und Constraint Drift)**  
**Anwendungsrahmen:** FruitStack als vorhandener Experimentier- und Validierungsverbund; TOKI SEO und Fruit-Hub.com als mögliche spätere Anwendungskontexte.  
**Ergebnisstatus:** Es wurden für dieses Manuskript **keine eigenen ZOMBIE-Messreihen ausgeführt**. Die beschriebenen Z01–Z05-Ergebnisse sind *Forschungsfragen oder vorab festgelegte Erfolgskriterien*, keine Beobachtungen; dies gilt ebenso für die zusätzlichen, explorativen Z06–Z11-Module.

## Zusammenfassung

Autonome KI-Agenten verarbeiten externe Webseiten, Dateien, E-Mails und Werkzeugantworten, um Nutzeraufgaben zu lösen. Enthalten diese unzuverlässigen Quellen verhaltenssteuernde Anweisungen, kann eine **indirekte Prompt-Injection** (Indirect Prompt Injection, IPI) entstehen: Der Agent behandelt Teile fremder Daten unter Umständen als Handlungsanweisungen. Die Forschung dokumentiert Angriffe über nicht sichtbare Inhalte, Obfuskation, dynamisch zusammengesetzte Webseiten und persistente Agentenspeicher. Sie zeigt jedoch nicht, dass eine bestimmte Anzahl wiederholter Abrufe, beispielsweise 20, automatisch eine Agentenübernahme auslöst. [1–5]

Dieses Manuskript entwickelt daher eine falsifizierbare Fragestellung: **Verändert die wiederholte Exposition gegenüber derselben externen Quelle das Verhalten eines KI-Agenten über den Effekt der zusätzlich präsentierten Informationsmenge hinaus?** Ferner wird untersucht, ob beobachtete Veränderungen der Retrieval-Schicht, dem aktuellen Kontext, persistenten Speichervorgängen oder der Werkzeugautorisierung zuzuordnen sind. Ein mehrstufiges, aber getrennt auszuwertendes Versuchsprogramm (Z01–Z05) verbindet eine vorgelagerte Nullverteilung, token- und zykluskontrollierte Vergleichsarme, ein faktorielles Grunddesign mit explizitem Abwehrfaktor, modellstratifizierte Auswertung sowie ereignisbasierte Provenienzprotokolle. Ergänzende Prüfarme adressieren die Schreibentscheidung ins Langzeitgedächtnis (*Write Election*), multimodale Eingaben, Tool-Registry-Provenienz und die Retrieval-Barriere. Die wirtschaftliche Anwendung in Generative Engine Optimization (GEO) wird eigenständig untersucht: Eine zentrale, überprüfte Wissensbasis kann sachlich konsistente HTML-, Markdown- und strukturierte Datenrepräsentationen für verschiedene Clients erzeugen. Potenzielle Empfehlungs- oder Affiliate-Effekte werden gemessen und nicht vorausgesetzt. [6–9]

**Wissenschaftlicher Anspruch:** Project ZOMBIE ist der Arbeitsname einer **Versuchsinfrastruktur**, keine bereits validierte Angriffsklasse und kein wissenschaftlicher Befund.

**Erweiterung in Revision 1.3:** Der bisherige Forschungsgegenstand bleibt unverändert erhalten, wird aber als erste Stufe einer größeren *Mikro-zu-Makro*-Fragestellung interpretiert: Unter welchen überprüfbaren Bedingungen kann eine minimal veränderte Information die Grenzen von Repräsentation, Retrieval, Modellkontext, Harness, persistentem Zustand, Werkzeugautorisierung und Systemausführung überschreiten und schließlich eine längerfristige oder verteilte Wirkung entfalten? Die Erweiterung definiert eine formale Übergangstaxonomie und zusätzliche, zunächst **explorative** Versuchsarme Z06–Z11. Sie ändert weder die Primärhypothesen H1–H9 noch die zuvor festgelegten Kontrollen; sie begründet insbesondere **keine** Behauptung, dass Binärdaten durch ihre bloße Anwesenheit im Modellkontext ausführbar würden.


**Zusatz in Revision 1.4:** Ein zuvor fehlgeschlagener, ausdrücklich ausgeschlossener Lösungsweg kann bei späteren Agentenschritten erneut als Option auftauchen, wenn der Zusammenhang zwischen Fehlerbeobachtung, verbindlicher Gegenentscheidung und aktuellem Auftrag nicht robust übertragen wird. Diese Fallklasse wird als *Constraint Provenance Loss* bzw. *Goal Reopening* untersucht. Eine im Projektkontext berichtete Beobachtung mit Codex Luna wird als **unbestätigte Fallvignette**, nicht als verifizierter Fehler- oder Kausalbefund, behandelt. Die Arbeit führt ein gesondertes, zunächst exploratives Modul Z11 mit kontrolliertem Kontextübergang und unabhängiger Tool-Durchsetzung ein. Die Z01–Z05-Kernpräregistrierung bleibt unverändert. 

**Schlüsselwörter:** KI-Agenten, indirekte Prompt-Injection, Kontextkontamination, Memory Poisoning, dosisabhängige Exposition, Retrieval, Kausalinferenz, GEO, Agentensicherheit, Harness Integrity, Constraint Provenance Loss, Goal Reopening.

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

**F7:** Unter welchen Bedingungen beeinflussen Unterschiede einzelner Bytes, Steuerzeichen oder Kodierungen die nachfolgende Repräsentation, ohne dass sich die intendierte Sachinformation ändert?  
**F8:** Wie stark verändern Harness-Kontext, Skill-Discovery/-Selection, Auftraggeberbindung und deterministische Regeln das Verhalten **desselben** Modells bei gleichbleibender legitimer Aufgabe?  
**F9:** Welche Unterschiede zwischen Windows- und Linux-Ausführung sind auf Encoding, Dateisystem, Shell, Umgebung, Tool-Registry oder konkrete Berechtigungsgrenzen zurückführbar, wenn Modell und Auftragsbedingungen kontrolliert sind?  
**F10:** Wann wird eine niedrig vertrauenswürdige Information von bloßem Datenmaterial zu einer ausgelösten, zugelassenen oder tatsächlich ausgeführten Systemaktion, und welche unabhängige Policy hätte den Übergang verhindern können?  
**F11:** Können frühere Agentenentscheidungen über persistente Zustände, generierte Inhalte oder erneut indexierte Informationen auf spätere Informationsauswahl zurückwirken, und wie lässt sich das von normaler Variation der Informationsumgebung trennen?  
**F12:** Unter welchen Bedingungen verliert ein Agent beim Kontext- oder Harness-Übergang die **kausale Bindung** zwischen einem beobachteten Fehlversuch, einer ausdrücklich verbindlichen Ausschlussentscheidung und dem fortbestehenden Arbeitsziel?  
**F13:** Erhöht die bloße Präsenz eines untersagten Lösungswegs im Kontext die spätere erneute Erwähnung, Auswahl oder versuchte Ausführung, **wenn** verbotener Inhalt, Tokenbudget und Salienz kontrolliert werden?  
**F14:** Kann ein hostseitiger, unveränderlicher Ausschlusskontrakt unerlaubte Ausführung verhindern, selbst wenn das Modell den bereits verworfenen Lösungsweg erneut vorschlägt?  


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


### 2.11 Von der Zeichenrepräsentation zur Systemautorität: Erweiterung des Bedrohungsmodells

Die bisherige IPI-Literatur ist eine notwendige, aber nicht hinreichende Perspektive auf Agentensysteme. Ein Einfluss auf das System kann **vor** dem Modell (Dekodierung, Retrieval, Filterung), **im** Modellkontext (Repräsentation und Inferenz), **im Harness** (Skill-Auswahl, Zusammenführung von Instruktionen und Arbeitszuständen), **nach** dem Modell (Tool-Policy, Schreibberechtigungen, Ausführung) oder **durch Rückkopplung** über spätere Sitzungen entstehen. Die Schichten sind kausal und hinsichtlich ihrer Vertrauensgrenzen getrennt zu betrachten; ein beobachteter Fehler in einer Schicht ist kein Beweis für die Kompromittierung aller nachfolgenden Schichten. Die OWASP-Taxonomie agentischer Risiken unterstreicht insbesondere Identitäts-, Tool-, Speicher-, Supply-Chain- und unerwartete Ausführungsrisiken. [30]

**Kleinste Einheit:** Ein Byte oder Unicode-Codepoint ist zunächst ein kodierter Datenwert. Steuerzeichen (beispielsweise `U+200B`, `U+202E`, `CR`, `LF`, `NUL`) können jedoch bei der Transformation zwischen Anwendungen beeinflussen, welcher Text sichtbar, vergleichbar, signierbar oder parsebar wird. Eine wirksame Manipulation folgt daraus erst, wenn die Interpretation einer vertrauensrelevanten Komponente messbar divergiert. Das ist eine **Repräsentationsdifferenz**, keine automatische Codeausführung. Analog sind LLVM-Bitcode, WebAssembly, Java-Bytecode und nativer Maschinencode technisch verschiedene Zwischen- bzw. Ausführungsformate. Ihre Ausführung erfordert jeweils einen vorhandenen Loader, eine Runtime oder einen ausführenden Prozess. In Project ZOMBIE wird Ausführung nur über isolierte, autorisierte Mock- oder Sandbox-Grenzen untersucht.

**Harness als eigenständiger Mechanismus:** Für GitHub Copilot dokumentieren VS Code und GitHub die progressive Skill-Discovery anhand von Name und Beschreibung, das nachfolgende Laden der `SKILL.md` sowie die davon getrennte Verwendung ergänzender Ressourcen. Die automatische Auswahl ist daher nicht mit der vorhandenen Fähigkeit gleichzusetzen. Im Standardfall werden die Skill-Anweisungen in den Elternkontext geladen; eine separate Ausführung im geforkten Kontext ist experimentell. Der relative Beitrag des Harness ist folglich nicht schon durch bessere Ergebnisse nach automatischem Einfügen einer bislang fehlenden `SKILL.md` bewiesen. [27, 28]

**Auftraggeber- und Zustandsbindung:** Persönliche Präferenzen, freigegebene Projektentscheidungen, Skill-Instruktionen und Tool-Berechtigungen sind unterschiedliche Autoritätsklassen. Ein Nutzerprofil darf weder aus beliebigen Webdokumenten rekonstruiert noch von untrusted Retrieval-Ergebnissen verändert werden. Ebenso sind Skill-Beschreibungen als Verfahrensanleitung **keine** allgemeine Autorisierung für externe Nebenwirkungen. Eine prüfbare Architektur muss jede Autoritätsklasse sowohl beim Lesen als auch beim Übergang zur Handlung erhalten.

**Verteilte Wirkung:** Rückkopplung entsteht dann, wenn ein Agent ein Artefakt oder einen persistenten Zustand verändert, der anschließend Retrieval, weitere Agenten oder spätere Empfehlungen beeinflusst. Das ist eine über mehrere Ereignisse vermittelte Wirkung. Weder eine einzelne veränderte Antwort noch ein einzelner gespeicherter Text belegt bereits eine selbstverstärkende Kausalkette. Die Publikationsrelevanz liegt in der eindeutigen Rekonstruktion und Abgrenzung dieser Übergänge.

### 2.12 Abgrenzung von Modellmodifikation, Inferenzsteuerung und Harness-Effekten

Drei experimentelle Interventionsklassen müssen auseinandergehalten werden: **(i)** Änderung persistierter Modellparameter (z. B. nachvollziehbare Checkpoint-/Adapter-Differenz), **(ii)** Änderung des Inferenzzustands bei konstanten Modellgewichten (z. B. Kontextgestaltung oder temporäre Aktivierungssteuerung) und **(iii)** Änderung externer Harness-Regeln, Werkzeugrechte oder Kontextkompilation. Die Aussage, ein Modell sei „durch eine Gewichtsänderung intelligenter geworden“, ist ohne überprüfbare Modellartefakte, Kontrollbedingungen und vergleichbare Evaluation kein wissenschaftlicher Befund. Eine beobachtete Verbesserung durch Astra/Qwen ist deshalb als **zu validierende Implementierungsbeobachtung**, nicht als bereits nachgewiesene Gewichtsmutation Bestandteil des Programms.

Die Forschung trennt ferner **benignes Capability-Provisioning** von **adversarialer Autoritätserschleichung**. Beide nutzen gegebenenfalls dieselbe Harness-Oberfläche, haben aber unterschiedliche Sicherheits- und Nutzenendpunkte. Gerade diese gemeinsame Mechanik begründet ihre Untersuchung im Rahmen *derselben* ZOMBIE-Arbeit; die Angriffs- und Qualitätsfragen bleiben innerhalb des Manuskripts getrennt auswertbar.

### 2.13 Suchmaschinen, Retrieval und Quellenwirksamkeit als größte Ebene

Die äußerste Beobachtungsebene ist nicht das Ranking eines einzelnen Modells, sondern die Verbreitung und Wiederaufnahme einer Information über Such-, Index-, Agenten- und Veröffentlichungsprozesse. Für Google gilt: Suchergebnispositionen sind query-, kontext- und zeitabhängig; eine allgemeine Position 1 für beliebige Suchbegriffe ist weder ein plausibles Erfolgskriterium noch aus kontrollierten Agentenversuchen ableitbar. Zudem untersagen Googles Spamrichtlinien insbesondere täuschendes Cloaking, missbräuchlich verborgene Inhalte und Keyword-Stuffing. [29]

Die legitime GEO-Teilfrage F6 wird daher als **faktentreue Darstellung und empirische Sichtbarkeitsmessung** weitergeführt, nicht als verdeckter Versuch, fremden Agenten neue Anweisungen unterzuschieben. Die Rückkopplungsfrage F11 untersucht getrennt, ob ein verändertes, autorisiert erzeugtes Dokument später messbar häufiger abgerufen und korrekt zitiert wird. Ohne nachweisbare Indexierungs-, Retrieval- und Expositionsdaten sind Aussagen über Suchmaschinenwirkung ausgeschlossen.

---

### 2.14 Negativwissen, Constraint Provenance Loss und Goal Reopening

Ein eigenständiges Problem langfristiger Agentenarbeit entsteht, wenn eine **negative Entscheidung** von ihrem Entscheidungsgrund getrennt wird. Ein Beispiel ist ein früherer fehlerhafter Ansatz `X`, dessen Fehler durch einen Test oder eine Nutzerkorrektur belegt wurde. Daraufhin wird `X` für einen definierten Auftrag, eine Umgebung oder eine konkrete Voraussetzung ausdrücklich ausgeschlossen. Bei einem späteren Kontextwechsel enthält der Agent möglicherweise nur noch eine verkürzte Erwähnung von `X`, nicht jedoch die wirksame Verknüpfung zu Fehlerevidenz, Geltungsbereich und bindender Entscheidung. In einem solchen Fall könnte der Agent `X` erneut als Handlungsmöglichkeit behandeln.

Die beobachtbare Fehlermöglichkeit ist **nicht** identisch mit klassischer IPI: Der ursprüngliche Ausschluss kann vollständig legitim und vom Nutzer selbst autorisiert sein. Sie gehört dennoch zu Project ZOMBIE, weil dieselben Speicher-, Kontext-, Harness- und Autoritätsübergänge über die tatsächliche Wirksamkeit einer Regel entscheiden, die auch ein Angreifer mit fremden Inhalten beeinflussen könnte. Die Sicherheitsrelevanz liegt im möglichen **Bedeutungsverlust einer bindenden Regel bei gleichzeitigem Erhalt ihres thematischen Gegenstands**.

Für die Analyse sind vier Phänomene zu trennen:

1. **Referentielle Wiedererwähnung:** Der Agent erwähnt `X`, etwa um dessen frühere Ablehnung zu erklären. Dies ist kein Verstoß.
2. **Goal Reopening:** Der Agent schlägt `X` erneut als ernsthaft zu prüfende Option vor, obwohl der Ausschluss für die aktuelle Aufgabe weiterhin gilt.
3. **Decision Reversal:** Der Agent trifft oder behauptet eine neue positive Entscheidung zugunsten von `X`, ohne dass eine gültige Revisionsfreigabe vorliegt.
4. **Unauthorized Effect:** Ein unabhängiger Ausführungsmonitor bestätigt, dass der verbotene Schritt nach einem Tool-Versuch tatsächlich ausgeführt wurde. Ein bloßer Plan oder Textbeleg ist dafür nicht ausreichend.

Eine **Negations-Priming-Hypothese** ist dabei nur eine konkurrierende Erklärung. Eine höhere Wiedererwähnungsrate kann aus Salienz, Informationsverlust, unklarer Reichweite, einer veränderten Aufgabenstellung, fehlender Speicherung, Modellrotation oder Harness-Selektion resultieren. Subjektive Absicht des Agenten ist weder beobachtbar noch notwendige Annahme. Für die Kausalattribution muss die Untersuchung die vorherige Fehlerentscheidung, ihre Herkunft und ihre Gültigkeit **separat** von einer bloßen Textanweisung wie „Mach X nicht“ protokollieren.

**Fallvignette (unbestätigt):** Im zugrunde liegenden Projektkontext wurde berichtet, dass ein Codex-Luna-Agent zunächst `X` umsetzte, dadurch einen Fehler verursachte, anschließend ein ausdrückliches *NOT* erhielt und später `X` erneut in Erwägung zog beziehungsweise konträr zum Ausschluss handelte. Ohne unveränderte Original-Traces, Modell-/Harness-Version, dokumentierte Kontextübergabe und Tool-Effektbelege ist daraus keine Aussage über Häufigkeit, Fehlerursache oder spezifische Schwäche von Copilot oder Codex ableitbar. Die Vignette dient ausschließlich der Hypothesengenerierung.

### 2.15 Verbindlichkeit ist keine bloße Informationspräsenz

Ein persistenter Speicher kann die Zeichenfolge `X ist verboten` zuverlässig aufbewahren und dennoch scheitern, wenn bei ihrer Wiederverwendung die Autorität der Entscheidung, der **Geltungsbereich** und ihre Ursache fehlen. Das Problem ist daher nicht nur *Memory Retrieval*, sondern die **Integrität einer normativen Zustandsbeziehung**:

`Fehlerevidenz → Entscheidung über X → autorisierter Regelstatus → unveränderlicher Auftragsscope → spätere Ausführungsentscheidung`.

Die sichere Behandlung benötigt zwei voneinander unabhängige Pfade: einen **epistemischen Pfad**, auf dem der Agent nachvollziehen kann, warum `X` verworfen wurde, und einen **normativen Pfad**, auf dem der Harness einen weiter gültigen Ausschluss auch dann durchsetzt, wenn das Modell dessen Begründung vergessen hat. Wird lediglich ein Textabschnitt ins Kontextfenster kopiert, ist die Verbindlichkeit nicht eigenständig geschützt. Eine Sperre darf aber auch keine unzulässige Dauerwirkung entfalten: Sie muss an Auftrag, Umgebung, Ablaufdatum und eine explizite, auditierbare Revisionsberechtigung gebunden sein.

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



### 3.1 Erweiterungshypothesen H10–H14 (explorativ; nicht nachträglich konfirmatorisch)

Die folgenden Hypothesen erweitern H1–H9; sie werden **erst nach** Instrumentierung, Pilotierung und separater Einfrierung ihrer Endpunkte zu konfirmatorischen Hypothesen. Nullbefunde sind zulässig.

| Hypothese | Messbarer Kontrast | Alternative Erklärung / Falsifikation |
|---|---|---|
| **H10 – Repräsentationsdivergenz** | Sachlich identische, unterschiedlich kodierte Inputs führen unter definierter Transformationspipeline zu unterschiedlich ausgewählten oder dargestellten Inhalten. | Gleiche kanonische Repräsentation; Unterschiede verschwinden bei kontrolliertem Parser oder sind nur Darstellungsartefakte. |
| **H11a – Skill-Selektion** | Bei identischen Aufgaben steigert eine regelgeleitete Auswahl die Rate **korrekt gewählter Skills** gegenüber Modellselektion, bei gleichzeitig erfasster False-Activation-Rate. | Kein Nettovorteil nach Abzug falscher Aktivierungen und zusätzlicher Kosten. |
| **H11b – Skill-Compliance bei konstanter Activation** | Bei exakt identischem Skill-Text im aktiven Modellkontext hat die **Herkunft der Auswahlentscheidung** (Modell vs. Resolver) einen zusätzlichen Effekt auf die Ausführungstreue. | Kein Unterschied; die gesamte Wirkung beruht auf Skill-Präsenz, Zeitpunkt oder Tool-Verfügbarkeit. |
| **H12 – Harness-/OS-Anteil** | Ein kontrolliertes Cross-over desselben Modells über Windows/Linux und unterschiedliche Harness-Konfigurationen erklärt reproduzierbar einen Teil der Verhaltensvarianz. | Keine reproduzierbare Differenz nach Kontrolle von Umgebung, Versionen, Shell, Kontext und Berechtigungen. |
| **H13 – Autoritätsübergang** | Nicht vertrauenswürdige Informationen erhöhen unter kontrollierten Bedingungen das Auftreten unberechtigter **Aktionsversuche**; unabhängige Ausführungspolitik verringert die Quote tatsächlich ausgeführter Effekte. | Keine Differenz zur Baseline; Versuche bleiben vollständig an der Enforcement-Grenze blockiert. |
| **H14 – Rückkopplung** | Eine autorisierte Veränderung eines persistenten bzw. veröffentlichten Artefakts vermittelt über nachgewiesene spätere Wiederaufnahme eine messbare Folgeabweichung. | Effekt verschwindet ohne erneutes Retrieval/Read oder ist durch normale Ranking-/Kontextvariation erklärbar. |

**Keine Tautologie als Beitrag:** „Skill vorhanden und geladen“ gegenüber „Skill nicht geladen“ ist primär ein *Activation*-Vergleich. Er beweist weder die Überlegenheit eines Resolvers noch einen eigenständigen Einfluss der Herkunft der Entscheidung. H11a, H11b und die False-Activation-Gegenmetrik werden deshalb separat ausgewertet. Das Gesamtprogramm untersucht außerdem, ob ein besserer Resolver bei mehrdeutigen Aufgaben schadet oder unnötige Schritte verursacht.

---

### 3.2 Erweiterungshypothesen H15–H17: Kontextbindung und Negativwissen (explorativ)

| Hypothese | Messbarer Kontrast | Ausschluss konkurrierender Erklärung |
|---|---|---|
| **H15 – Constraint-Provenienz** | Bei identischer Regelpräsenz senkt eine unverändert mitgeführte, hostbestätigte Bindung `Fehlerbeleg → Ausschluss → Scope` gegenüber einer **gleich langen**, begründungslosen `NOT X`-Notiz die Rate unerlaubter Wiederentscheidungen. | Kein Effekt bei gleichem Informationsgehalt; Gründe und Scope erreichen in einem Arm den Modellinput nicht; abweichendes Tokenbudget erklärt den Befund. |
| **H16 – Context-Transition Drift** | Nach einem vorab definierten Kontextwechsel, einer Zusammenfassung oder einem Sitzungs-Handoff steigt die *Goal-Reopening*-Rate stärker, wenn der Ausschluss nur als Freitext statt als unveränderlicher Entscheidungszustand übertragen wird. | Kein Interaktionseffekt, unveränderte Kontextinformation oder bloßer Modell-/Harness-Wechsel. |
| **H17 – Enforcement unabhängig vom Modell** | Ein hostseitiger, gültigkeitsgeprüfter Ausschlusskontrakt verhindert **ausgeführte** verbotene Aktionen unabhängig davon, wie häufig das Modell `X` vorschlägt. | Verbotener Effekt bei aktivem und für den Scope gültigem Gate; kein Unterschied zur Kontrollbedingung bei gleicher Aufgabenleistung. |

**Keine Unterstellung eines ironischen Gegenteileffekts:** Die Aussage „Auf keinen Fall X“ enthält `X` im Kontext, doch allein daraus folgt nicht, dass `X` wahrscheinlicher ausgeführt wird. Die Studie trennt thematische Erwähnung, echte Auswahl, Versuch und Effekt. Negative und positive Formulierungen mit gleicher Bedeutung sowie salienzkontrollierte neutrale Formulierungen werden explizit gegeneinander getestet. H15–H17 dürfen nicht nachträglich an Beobachtungen angepasst und als vorregistriert bezeichnet werden.

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


### 4.7 Das Mikro-zu-Makro-Prinzip als experimentelle Leiter

Die Erweiterung beginnt grundsätzlich beim **kleinsten beobachtbaren Unterschied** und steigt erst dann zur nächsten Ebene auf, wenn der Übergang messtechnisch belegt ist. Dabei wird **nicht** angenommen, dass alle Stufen in einem erfolgreichen Lauf durchlaufen werden. Auch der Abbruch an einer Zwischenstufe ist ein relevantes Ergebnis.

| Stufe | Prüfobjekt | Minimale Beobachtung | Übergangsgate |
|---|---|---|---|
| L0 – Byte/Codepoint | Originalbytes, Encoding, Steuerzeichen | Byte-Hash und dekodierte Zeichenfolge | tatsächliche Dekodierung dokumentiert |
| L1 – Repräsentation | Parser, DOM, OCR, Metadaten, Struktur | kanonische bzw. abgeleitete Repräsentation | Transformation und Verlust/Erhalt von Signal belegt |
| L2 – Retrieval | Ranking, Snippet, Cache, Kontext-Cutoff | Auswahlposition und tatsächlich übernommener Ausschnitt | Modellinput enthält den abgeleiteten Ausschnitt |
| L3 – Modellkontext | Instruktionsrollen, Fakten, Skill-Text | vollständiger relevanter Prompt-/Context-Digest | geplanter/veränderter Output beobachtet |
| L4 – Harness | Skill-Discovery, Auftraggeberbindung, Policies | Aktivierungs- und Entscheidungsprotokoll | wirksame Entscheidung gegen gültige Policy vergleichbar |
| L5 – Persistenz | CherryMe/MangoMe/weitere Stores | Write Election, Receipt, späterer Read | Cross-Session und No-Refetch belegt |
| L6 – Werkzeuge | Tool-Registry, Authorization, Gateway | Attempt / Deny / Allow | tatsächliche Ausführung separat attestiert |
| L7 – Betriebssystem | Shell, Prozess, Runtime, Dateien, API | beobachteter synthetischer Seiteneffekt | Endeffekt durch unabhängigen Monitor belegt |
| L8 – Ökosystem | Agenten-Handoff, veröffentlichte Fakten, Suche | erneuter Abruf und nachfolgende Entscheidung | Rückkopplungspfad ohne Konfundierung dokumentiert |

Die Bezeichnungen L0–L8 sind **eine für ZOMBIE vorgeschlagene Taxonomie**, keine bereits etablierte externe Norm. Eine Stufe darf nicht übersprungen werden: Beispielsweise reicht der Nachweis von Base64 in L0 nicht für die Annahme einer Dekodierung in L1 oder einer Befolgung in L3. Ebenso ist ein durch ein Modell erzeugter Shell-Befehl kein Nachweis seiner Ausführung in L7.

### 4.8 Transformationsprovenienz statt unzulässiger Hash-Gleichsetzung

Ein bisheriges Canary-Audit, das denselben Inhalts-Hash über alle Komponenten erwartet, kann den Übergang zwischen **Roh-HTML**, **bereinigtem Text** und **Modellnachricht** nicht korrekt abbilden: Jede legitime Transformation verändert die Bytes. In einem erweiterten *Trust Transition Graph* \(G=(V,E)\) repräsentiert daher jeder Knoten eine bestimmte **versionierte Repräsentation**; jede gerichtete Kante trägt den vom vertrauenswürdigen Host vergebenen Transformationsbeleg:

\[
E_i=(\text{parent\_event\_id},\text{input\_sha256},\text{output\_sha256},\text{transform\_id},\text{policy\_receipt},\text{actor\_id}).
\]

Die Eigenschaft \(\text{input\_sha256}=\text{output\_sha256}\) ist nur bei identischer Byte-Repräsentation erforderlich. Andernfalls muss die Kante den **beabsichtigten** Transformationsschritt und den daraus resultierenden Digest nachvollziehbar attestieren. Ein Modell kann diese Provenienz nicht allein dadurch autorisieren, dass es die passende Behauptung in eine Tool-Antwort schreibt. Für signierte Ereignisse sind getrennte, modellunzugängliche Host-Schlüssel und eine unabhängig geprüfte Rechtevergabe Voraussetzung. Ein HMAC beweist ansonsten nur, dass der Schlüssel verwendet wurde, nicht dass der signierende Prozess den Modellinput nicht ungeprüft übernahm.

### 4.9 Kausale Harness-Vergleiche und Varianzzerlegung

Die Untersuchung vergleicht **dasselbe Modell und dieselbe Aufgabenbank** in vorab festgelegten Harness-Bedingungen. Dabei werden zwei Experimente getrennt:

1. **Discovery-/Selection-Kontrast:** Alle Bedingungen verfügen über denselben Skill-Katalog. Gemessen wird, ob ein geeigneter Skill **gefunden und korrekt ausgewählt** wird, einschließlich *False Activation* bei mehrdeutigen oder skillfreien Aufgaben.
2. **Compliance-Kontrast bei konstanter Activation:** Der identische Skill-Inhalt (Datei-Digest, Tokenbudget, Position, Zeitpunkt) liegt in allen verglichenen Bedingungen bereits vor. Lediglich der **Entscheidungspfad**, über den die Aktivierung zustande kam, unterscheidet sich. Die Compliance-Differenz ist damit von bloßer Skill-Präsenz getrennt.

Hinzu kommen **negative Kontrollen** (keine relevante Fähigkeit erforderlich), **doppelt zuordenbare Aufgaben**, Kontrollaufträge ohne externe Daten und **Plattform-Cross-over** Windows/Linux bei eingefrorenen Versionen von Modell, IDE, Agenten-Erweiterung und Runtime. Laufreihenfolge, Aufgabencluster, Modell- und Harness-Identität werden im statistischen Modell berücksichtigt. Die geplante Varianzzerlegung unterscheidet Komponenten für Aufgabe, Modell, Harness, Betriebssystem, Interaktionen und zufällige Restvariation; ein Modell-/Harness-Effekt darf nicht allein aus dem Vergleich verschiedener Modelle auf verschiedenen Plattformen abgeleitet werden.

Als Primärmetriken für H11 dienen *Correct Skill Selection*, *False Activation*, *Task Utility* und die Anzahl unnötiger Aktionen; für H11b zusätzlich *Compliance bei verifizierter Activation*. Für H12 wird die zwischen Bedingungen erklärte Varianz mit Unsicherheitsintervallen berichtet. Die endgültige Modellform und Power werden vor der konfirmatorischen Phase anhand unabhängiger Pilotdaten festgelegt.

### 4.10 Kontextgebundene Negativentscheidungen: Experimenteller Kontrast

Der Test beginnt mit einem **synthetischen, reproduzierbaren Fehlversuch**: Das Ausführen von `X` liefert einen deterministischen Misserfolg, dessen Diagnose und gültige Ausschlussentscheidung vor dem Agenten-Folgeschritt im Host-Ledger festgehalten werden. Das spätere Ziel bleibt identisch; es wird kein neuer Nutzerauftrag erfunden. Die bereits gescheiterte Handlung `X` ist weiterhin gegenstandsbezogen relevant, aber für den definierten Scope nicht autorisiert. Der Host kennt die verbindliche Wahrheit; das Modell kann sie nur über den ihm angebotenen Kanal wahrnehmen.

Für die isolierte Ursache-Wirkungs-Frage werden zwei Faktoren kontrolliert gekreuzt:

| Faktor | Zustand 0 | Zustand 1 |
|---|---|---|
| **Kontextübergang C** | Vollständiger gültiger Arbeitskontext | Vorab festgelegte, versionierte Kontextkomprimierung oder Sitzungsübergabe |
| **Constraint-Bindung B** | Gleichlange, unstrukturierte Freitextnotiz mit dem Ausschluss | Host-attestierter Verweis auf Fehlerbeleg, verbindliche Entscheidung, Scope und Revisionsrecht |

Das resultierende **2×2-Design** wird um einen unabhängig kontrollierten *Policy-Enforcement*-Faktor **G** ergänzt, ohne diesen mit dem primären Kontext-Bindungskontrast zu vermischen. Alle Arme erhalten denselben verbotenen Begriff `X`; Tokenzahl, Kontextposition, Zielbeschreibung, Zahl der Modell- und Tool-Zyklen und verfügbares Werkzeugset werden nach Möglichkeit paarig gleichgehalten. Unterschiede im zusätzlichen Kontextinhalt (z. B. erläuternde Kausalbeziehung) werden als eigener erklärender Faktor oder durch geeignete Kontrollen ausgewiesen, nicht als reine Wirkung des Wortes „NOT“ interpretiert. Für eine rein semantische Kontrolle kann derselbe sachliche Fehlerbeleg in allen Bedingungen bereitliegen, während nur die **hostbestätigte Bindung der Entscheidung** variiert.

Eine zweite, orthogonale Formulierungsstudie prüft positive gegenüber negativen, sachlich äquivalenten Anforderungen unter gleicher Informationsmenge; sie wird nicht mit dem Primärdesign vermischt. Randomisiert werden Aufgabenpaar, Oberfläche/Harness, Ausführungsreihenfolge und gegebenenfalls Formulierung. Modell-ID, Gewichte, Samplingparameter, Kontextfenstergröße, verfügbare Skills und Tool-Policy werden dokumentiert. Modelle oder Hosts dürfen nicht nach beobachtetem Erfolg dynamisch ersetzt werden, ohne eine eigene experimentelle Bedingung zu erzeugen.

Ein fehlendes oder beschädigtes Context-Receipt führt zum Status **NICHT INSTRUMENTIERBAR**, nicht zu einem fingierten Beleg für Drift. Tatsächliches Nachdenken ist aus einem finalen Antworttext nicht direkt messbar; erfasst werden nur prüfbare Pläne, explizite Vorschläge, Entscheidungen, Tool-Requests und Effekte, die der Harness tatsächlich protokolliert.

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


### 5.4 Erweiterungsmodul Z06 – Byte-, Steuerzeichen- und Parser-Differential

**Kleinstmögliche Intervention:** Variation einer einzelnen eindeutig definierten Repräsentationseigenschaft, etwa Normalisierungsform, Zeilenende, unsichtbares Unicode-Zeichen oder Text-/Attributposition bei **identischer intendierter Sachinformation**. Der Inhalt ist harmlos; es werden ausschließlich synthetische Canary-Marker und Produktfakten verwendet. Die Testmatrix enthält mindestens Originalbytes, Decoder-Output, Parser-Output, Retrieval-Snippet und tatsächlichen Modellkontext. Gemessen werden Signal-Erhalt, parserabhängige Unterschiede und unbeabsichtigte Kontextaufnahme. Die Gegenprobe ist ein kanonisch normalisierter Eingang. Ein beobachteter Byteunterschied ohne weitergereichten Effekt zählt nicht als Injection.

### 5.5 Erweiterungsmodul Z07 – Harness-Bindung und Skill-Activation

**Intervention:** Konstanter Modellcheckpoint und Benutzerauftrag; variiert werden allein die nachweisbare Skill-Discovery, das Auswahlsystem und die vom Host bereitgestellte, autorisierte Auftragsbindung. Die Studie unterscheidet **User-Binding**, **Project-Binding**, **Skill-Presence**, **Skill-Selection** und **Enforcement** als verschiedene Variablen. Skill-Instruktionen bleiben ohne eigene Berechtigung, externe Effekte auszulösen.

Der primäre Selection-Kontrast erfasst passende, unpassende und nicht benötigte Skills. Der gesonderte Compliance-Kontrast stellt die **identische** `SKILL.md` in allen Armen bereit und misst nur die Ausführungstreue. Zusätzlich werden Default-Pfade und Konfigurationen dokumentiert (`.github/skills/`, `.claude/skills/`, `.agents/skills/`, `disable-model-invocation`, in den jeweiligen dokumentierten Harness-Versionen). Behauptungen über „schlechteres Verhalten“ unter Copilot oder Windows werden erst nach reproduzierbaren, gepaarten Läufen formuliert. [27, 28]

### 5.6 Erweiterungsmodul Z08 – Komponentenübergreifende Autoritäts- und Memory-Übergänge

**Intervention:** Ein einziger inert markierter Informationseintrag durchläuft die realen Host-Übergänge. Unterschieden werden Retrieval-Quelle, CherryMe-Kandidat, unabhängig verifizierte Evidenz, CherryMe Knowledge-Write, PeachMe-Ausführungsentscheidung und MangoMe-Checkpoint. Für jeden Übergang werden *Producer*, Host-Signatur, Elternereignis, Transformationsnachweis, Entscheidungsautorität, Schreibentscheidung und Wiederverwendung protokolliert. Die Veröffentlichung eines Kandidaten ist kein Verifikationsnachweis; ebenso ist das Bestehen eines KnowledgeStore-Statuschecks kein Beweis hostseitiger Unfälschbarkeit.

Der frühere Z05-Kontrast – **neutral gegen adversarial gerahmt bei identischen Fakten** – bleibt der wissenschaftliche Kern für kontaminierende *Write Election*. Z08 ist die *Instrumentierungs- und Übergangsprüfung*, keine zweite Umbenennung des Memory-Poisoning-Endpunkts. Erst die nachgewiesene Modell-/Host-Trennung ermöglicht eine konfirmatorische Auswertung von H5 und H9.

### 5.7 Erweiterungsmodul Z09 – Tool- und Betriebssystemgrenzen

**Intervention:** Identischer ungefährlicher Nutzerauftrag und identischer Modellinput unter zwei dokumentierten Harness-/OS-Konfigurationen; alle nach außen wirkenden Werkzeuge werden auf **synthetische, inerte Mock-Tools** beschränkt. Gemessen werden die Stufen *proposed*, *attempted*, *policy-decided*, *invoked* und *side-effect-observed*. Shell-, Dateisystem- und Runtime-Differenzen werden als mögliche Moderatoren separat protokolliert. Ein ausführbares Fragment darf die Sandbox weder verlassen noch reale Kernel- oder Betriebssystemschutzmechanismen verändern. Es werden keine Kernel-Injection-, Persistenz- oder Privilegieneskalationsverfahren in Zielsystemen erprobt.

Die zentrale Kausalfrage lautet, ob eine niedrig vertrauenswürdige Information die **Autorisierungsentscheidung** verändert oder lediglich das Modell zu einem blockierten Versuch veranlasst. Reale Ausführung wird nur nach unabhängigen, nicht modellbasierten Effektbelegen gezählt. Die OS-Dimension prüft Reproduzierbarkeit, nicht eine vorausgesetzte Schwäche von Windows oder Linux.

### 5.8 Erweiterungsmodul Z10 – Rückkopplung zwischen Agenten, Artefakten und Retrieval

**Intervention:** In einem kontrollierten lokalen Informationskorpus erstellt oder aktualisiert ein autorisierter Agent sachlich korrekte Artefakte. Ein unabhängiger zweiter Agent greift zu vorher definierten Zeitpunkten auf diesen Korpus zu. Erfasst werden Erstellungsreceipt, Veröffentlichungs-/Indexierungszeit, tatsächlicher Retrieval-Treffer, Kontextaufnahme und anschließende Entscheidung. Die Kontrollgruppe erhält identische Fakten mit fixiertem Stand oder ohne erneute Indexierung. Damit wird die Rückkopplung als **mehrgliedriger vermittelter Effekt** überprüft, nicht aus einer bloßen Empfehlung abgeleitet.

Eine externe GEO-Validierung mit Suchmaschinen und Affiliate-Daten ist ein separater, ethisch begrenzter Anschlussarm. Eine pauschale „Google-Position 1 für jeden Begriff“ ist **kein** wissenschaftlich sinnvoller Endpunkt; analysiert werden querybezogene Sichtbarkeit, korrekte Zitierung, attribuierte Klicks und gegebenenfalls reale Conversion-Raten. Täuschendes Cloaking, versteckte Rankingbefehle oder die Manipulation fremder Agenten sind ausdrücklich ausgeschlossen. [29]

### 5.10 Erweiterungsmodul Z11 – Goal Reopening nach verlorener Constraint-Provenienz

**Ausgangslage (kleinster Zustandseingriff):** Ein einzelner synthetischer Befehl `X` schlägt nachweisbar fehl. Ein autorisierter Auftraggeber schließt `X` für denselben Auftrag explizit aus. Die Host-Quelle speichert **Fehlerevidenz, Ausschluss, Scope, Aussteller, Zeitstempel und erlaubte Revisionsregel** getrennt. Weitere Versuchsbedingungen variieren nur, *wie* diese Entscheidung in einen neuen Kontext übergeben wird.

**Ablauf:**

1. `t0 – ERROR_OBSERVED`: Hostseitiger Test liefert einen echten, aber ausschließlich simulierten Fehler von `X`; ein unveränderliches Receipt belegt die Ursache.
2. `t1 – CONSTRAINT_ESTABLISHED`: Eine autorisierte, scopegebundene Entscheidung `NOT X` wird versioniert gespeichert. Ihr Wortlaut ist in allen Vergleichsarmen semantisch gleich.
3. `t2 – CONTEXT_TRANSFORMED`: Derselbe Auftrag wird entweder vollständig fortgeführt oder mit einer deterministisch dokumentierten Zusammenfassung beziehungsweise Übergabe fortgesetzt. Ein `context_input_hash` belegt den tatsächlichen Input des Folgemodells.
4. `t3 – GOAL_REOPENING_OBSERVED`: Die nächste Folgeentscheidung wird ausschließlich anhand archivierter, äußerlich beobachtbarer Ausgaben/Actions klassifiziert: zulässige Fehlerreferenz, erneuter Lösungsoption-Vorschlag, tatsächliche Auswahl oder Tool-Versuch.
5. `t4 – POLICY_ENFORCED`: Ein separat instrumentierter Tool-Mock bestätigt, ob das Verbot im aktuellen Scope technisch eingehalten wurde. `ATTEMPT`, `DENIED`, `ALLOWED` und `EXECUTED` bleiben unterschiedliche Kategorien.
6. `t5 – RECONCILED`: Das unabhängige Zustandsledger hält fest, ob eine gültige, autorisierte Revision des Ausschlusses vorlag. Ohne solche Revision zählt eine Wiederöffnung nicht als legitime Änderung.

**Kontrollbedingungen:** Ohne vorherigen Fehler; mit Fehler, aber ohne Ausschluss; mit vollständiger Kausalbindung; mit gleichlanger, aber aus ihrem Fehlerbeleg gelöster Notiz; mit und ohne Kontextkomprimierung; mit und ohne unabhängige Tool-Sperre. Es werden keine realen Dateien zerstört, keine produktiven Agentenrechte erhöht und keine fremden Agenten getestet.

**Primäre technische Prüfpunkte:** Unveränderte Error-/Constraint-Receipts, `decision_id`, `scope_id`, `issuer_identity`, `issuer_authority`, `revision`, `expiration`, `model_input_hash`, `context_transform_receipt`, `tool_attempt_id`, `policy_verdict`, `execution_receipt`. Kontextausgaben, die den alten Fehler erwähnen, gelten nicht automatisch als erneuter Fehlversuch.

**Interpretation:** Die zentrale Zielvariable ist der **unautorisierte erneute Entscheidungsschritt zugunsten von X** (nicht die reine Erwähnung). Hostseitig verweigerte Tool-Aufrufe belegen einen Enforcement-Erfolg, keine zwingende Verbesserung der Modell-Compliance. Fehlende Nachweise für die Kontinuität zwischen `t1` und `t3` begrenzen die Aussage auf eine nicht zuordenbare Abweichung.

---

### 5.9 Integrationsprinzip: keine lineare Erfolgsannahme

Z06–Z10 werden **nicht** als eine einzige, zwangsläufig erfolgreiche Angriffskette ausgeführt. Vielmehr wird ein aufsteigendes Evidenzprogramm durchlaufen: Jede höhere Stufe verlangt den geprüften Nachweis der vorausgehenden erforderlichen Übergänge; Stufen können an vorhandenen Sicherheitsgrenzen enden. Alle Ergebnisse werden auf Ebene ihrer tatsächlich beobachteten Kettenglieder berichtet. Die Kernexperimente Z01–Z05 behalten ihre unabhängigen Primärendpunkte und Kontrollarme, sodass die neue Forschung den ursprünglichen wissenschaftlichen Beitrag nicht nachträglich umdefiniert.

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


### 6.4 Trust Transition Graph: Ereigniskontrakt über Komponenten hinweg

Jeder für eine kausale Behauptung verwendete Übergang erhält mindestens: `trace_id`, `event_id`, `parent_event_id`, `representation_kind`, `input_sha256`, `output_sha256`, `transform_id`, `source_receipt`, `producer`, `policy_receipt`, `session_id`, `actor_identity`, `trust_class_origin` und den unabhängig beobachteten Folgezustand. Die Felder sind **pro Ereignistyp optional bzw. verpflichtend zu spezifizieren**: Ein reiner Retrieval-Event benötigt beispielsweise noch keinen Memory-Read, ein tatsächlicher Effekt dagegen einen unabhängigen Ausführungsbeleg. Der Audit muss unverifizierte, fehlende oder nicht lesbare Evidenz als **nicht nachgewiesen** ausweisen, statt sie zu ergänzen.

Insbesondere prüft der Host, ob Quellen-/Trust-Metadaten **außerhalb des kontrollierten Modelloutputs** erzeugt und vor Veränderung geschützt wurden. Sowohl eingehende MCP-Tool-Metadaten als auch Tool-Antworten bleiben bis zur bewussten Host-Genehmigung untrusted. Wenn der Parser Text kürzt, eine Datei konvertiert oder ein Skill kompiliert wird, verweist die Nachfolgerpräsentation über die Transformationskante auf ihren Elternknoten, anstatt einen unveränderten Body-Hash vorzutäuschen.

Der erste Canary kann zeigen, dass bestimmte Ereignisse technisch existieren; er kann **weder** H5/H9 bestätigen **noch** eine spätere Wiederverwendung oder einen unabhängigen Host-Sicherheitsrand beweisen, solange echte Adapter, Host-Schlüsselgrenzen, Schreib-/Leseprotokolle und vollständige Reset-Belege fehlen.

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


### 7.4 Endpunkte der Mikro-zu-Makro-Erweiterung

Die zusätzlichen Größen werden **neben**, nicht anstelle der ursprünglichen Primärendpunkte ausgewertet:

- **Transformationsübertritt:** Anteil gültig empfangener Canary-Ereignisse, deren erwarteter Signalzustand in der abgeleiteten Repräsentation nachweisbar ist; getrennt nach zulässiger und unerwarteter Übernahme.
- **Skill-Selektionsqualität:** Sensitivität auf klar geeigneten Aufgaben, False-Activation-Rate auf nicht passenden Aufgaben, Task Utility und unnötige Tool-Kosten.
- **Compliance unter konstanter Activation:** Differenz der Ausführungstreue bei gleichem Skill-Text, gleicher Tokenposition und gleicher Zugriffsberechtigung.
- **Cross-Harness-/OS-Varianz:** durch Harness, Betriebssystem und Interaktion erklärte Varianzanteile; berichtet mit Aufgabenclustern, Replikationen und Konfidenzintervallen.
- **Durchgesetzte Autoritätsverletzung:** Anteil mit unabhängig attestiertem unberechtigtem *Effekt*; klar getrennt von Modelltext, Tool-Vorschlag und Tool-Aufrufversuch.
- **Nachgewiesene Rückkopplung:** Anteil der Läufe mit vollständigem Ereignispfad von Artefaktänderung über erneuten Abruf bis zur späteren Antwort-/Handlungsänderung; ohne vollständigen Pfad nur deskriptiv.

Eine zusammenfassende „ZOMBIE-Gesamterfolgsrate“ wäre bei diesen unterschiedlichen Endpunkten irreführend. Falls künftig ein zusammengesetzter Risikoindex eingeführt wird, müssen Gewichte, Schadensklassen, fehlende Evidenz und der Einfluss der Skalenwahl vor einer konfirmatorischen Erhebung festgelegt werden.

### 7.5 Zusätzliche Messgrößen für Constraint Drift (Z11)

Die folgenden Outcomes sind für Z11 getrennt zu berichten; ein positiver Wert in einer niedrigeren Stufe impliziert keinen höheren:

| Outcome | Zähler | Nenner und Beweisanforderung |
|---|---|---|
| **Mention-Recurrence-Rate** | Folgeantwort erwähnt `X` | Alle gültigen Folgeantworten; **nicht** als Regelverstoß zählen |
| **Goal-Reopening-Rate** | `X` wird trotz weiter gültigen Ausschlusses erneut als aktive Option vorgeschlagen | Alle gültigen, dem Modell nachweisbar exponierten Folgeläufe; externe Klassifikationsrubrik und Blindannotation |
| **Decision-Reversal-Rate** | `X` wird ohne autorisierte Revision ausgewählt oder freigegeben | Alle gültigen Fälle mit dokumentierter Entscheidungsgelegenheit |
| **Unauthorized Tool Attempt Rate** | Tool-Mock registriert einen verbotenen Versuch | Alle Läufe mit identischer Tool-Gelegenheit; Receiptpflicht |
| **Enforcement Failure Rate** | Verbote werden von der Infrastruktur trotz aktivem Gate tatsächlich vollzogen | Alle gültigen, im betreffenden Scope eingegangenen gesperrten Tool-Anfragen; unabhängiger Effect-Monitor |
| **Constraint-Link Survival** | Fehlerbeleg, Ausschluss, Scope und Autoritätsstatus sind nach Übergabe vollständig rekonstruierbar | Alle geprüften Kontextübergänge; vollständige verifizierte Kante nötig |
| **Legitimate-Task Utility** | Auftrag korrekt abgeschlossen, ohne `X` | Alle gültigen Aufgaben; schützt vor trivialem „nichts tun“ als vermeintlichem Sicherheitsgewinn |

Die Hauptanalyse ist ein vorab spezifizierter Interaktionskontrast `Kontextübergang × Constraint-Bindung` auf die *Goal-Reopening-Rate* sowie ein unabhängiger Policy-Kontrast auf tatsächlich ausgeführte verbotene Aktionen. Aufgaben, Kontextläufe und Provider-Modellidentitäten werden als Cluster berücksichtigt. Die Nullverteilung ist **zuerst** zu erheben. Ein indirekter Vertrauens- oder Intentionsbegriff ist nicht messbarer Primärendpunkt. Effekte bleiben explorativ, bis Aufgabenbank, Schwellen, Stichprobenplanung und Rubriken separat eingefroren sind.

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


### 8.3 Projektstand zum 10. November 2026 und nachgewiesene Integrationslücken

Der Repository-Vertrag in [`tonnestate/Zombie`](https://github.com/tonnestate/Zombie) enthält eine Offline-Testumgebung, einen signierten Canary-Ereignisverifier und getrennte CI-Workflows. Der zunächst vorhandene Sichtbarkeitsparser behandelte HTML-Void-Elemente wie `<img>` als verschachtelte Elemente und konnte dadurch nachfolgend sichtbaren Text irrtümlich verbergen. Ein gezielter Fix und zusätzliche Regressionstests wurden in GitHub übernommen; die CI-Erfolge sind **Engineering-Nachweise** für diese begrenzten Tests, nicht für die Forschungsfragen Z01–Z10. Die verbleibende Abweichung eines Toy-Parsers von einem vollständigen Browser-DOM wird explizit dokumentiert.

Bei der Quellcodeinspektion des bestehenden FruitStack wurden folgende **technische Prüfpunkte** sichtbar (keine pauschalen Sicherheitsurteile):

- [`PeachMe/src/peachme/tool_gateway.py`](https://github.com/tonnestate/PeachMe/blob/main/src/peachme/tool_gateway.py) erstellt Tool-Receipts und ein hashverkettetes Journal mit optionalem MangoMe-Mirror; der Rückgabevertrag muss mit CherryMes Aufrufer abgeglichen werden.
- [`CherryMe/cherryme/web_research.py`](https://github.com/tonnestate/CherryMe/blob/main/cherryme/web_research.py) übernimmt externe Texte über einen injizierten Gateway-Aufruf und validiert extrahierte Quellen unter anderem anhand eines Excerpt-Hashes und eines Retrieval-Receipts.
- [`CherryMe/cherryme/verification.py`](https://github.com/tonnestate/CherryMe/blob/main/cherryme/verification.py) verlangt für eine positive Quotenentscheidung mindestens zwei unterschiedliche Verifikationsidentitäten. Das belegt eine **implementierte Quorum-Regel**, nicht die vollständige Vertrauenswürdigkeit des zugelieferten Worker-Receipts.
- [`CherryMe/cherryme/knowledge.py`](https://github.com/tonnestate/CherryMe/blob/main/cherryme/knowledge.py) ermöglicht `verifier_receipts` als optionalen Parameter von `KnowledgeStore.publish`; in der untersuchten Implementierung wird deren Vollständigkeit **an der Speicher-API** nicht verpflichtend erzwungen. Eine tatsächliche Privilegieneskalation ist daraus nicht ohne weitere Laufzeitbelege ableitbar.

Für den Mikro-zu-Makro-Audit folgt daraus eine konkrete Priorität: **zuerst** die Identität von Modellinput, abgeleiteten Repräsentationen und Host-Receipts nachweisen, **danach** die Verifikation und Write Election verfolgen, **erst zuletzt** reale (in der Laborumgebung simulierte) Ausführung und Rückkopplung beurteilen. Das Ziel ist kein neues, redundantes Agentenframework, sondern eine schlanke, versionierte Beobachtungsschicht über vorhandenen FruitStack-Grenzen.

### 8.4 FruitStack-Integrationsprüfung für Negative Knowledge

Die bestehenden Komponenten sollten **nicht** um ein weiteres, unabhängiges Wahrheits- oder Erinnerungssystem ergänzt werden. Z11 verwendet nur instrumentierte Übergänge zwischen den bereits vorgesehenen Verantwortlichkeiten:

- **MangoMe:** Arbeitszustand, gültiger Auftrag, Fehlerevidenz und versionierter Entscheidungsstatus; ein Ausschluss muss im Scope des konkreten Work-Items referenzierbar bleiben. Ob bereits alle nötigen Felder und Durchsetzungspfade existieren, ist im laufenden Host nachzuweisen.
- **CherryMe:** Erkenntnislage, negative Hypothesen beziehungsweise falsifizierte Ansätze und Verifikationsstatus. *FALSIFIED* darf nicht ohne nachvollziehbare Revision wieder zu *PROMISING* oder *SUPPORTED* aufsteigen, wenn die zugrunde liegenden Bedingungen unverändert sind. Eine Modellbehauptung über eine geänderte Voraussetzung genügt nicht.
- **PeachMe:** Context-/Session-Bindung, Tool-Auswahl und unabhängiger Policy-Pfad; die Sperre muss auch dann gelten, wenn der aktuelle Modelltext `X` als vernünftigen Vorschlag formuliert. Vorhandene Hooks, Policy-Entscheidungen oder Tool-Receipts gelten nur nach Nachweis der tatsächlichen Host-Installation als wirksam.
- **OrangeMe:** Falls eine Projektübergabe über ProjectLedger stattfindet, muss der Ausschluss als versionierter Zustand mit Herkunftsverweis ankommen. Eine freie Chat-Nachricht, die den Ausschluss paraphrasiert, ersetzt den autorisierten Status nicht.

**Vorgeschlagener minimaler Audit-Vertrag:** `failure_receipt → constraint_decision_receipt → context_projection_receipt → model_input_receipt → candidate_decision_receipt → tool_policy_receipt → effect_receipt`. Die Ereignisse müssen über `work_ref`, `scope_id`, `constraint_id`, `revision` und nachweisbare Transformationskanten zusammenhängen. Modellseitig gesetzte Trust-/Provenienzfelder dürfen keine Autoritätswirkung besitzen. Ein `NOT X` als Freitext darf niemals als alleinige Enforcement-Sperre gelten.

**Ausdrücklicher Nichtnachweis:** Aus einer im Gespräch beschriebenen Wiederholung des früheren Fehlers folgt noch nicht, dass eine bestimmte Copilot-, Windows- oder Codex-Version strukturell unsicher ist. Das Modul fordert die hierfür notwendigen Prüfbelege und erlaubt auch den Nullbefund.

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


### 9.4 Anschluss an die Mikro-zu-Makro-Kette

TOKI SEO und Fruit-Hub.com können die **äußere Stufe L8** mit faktentreuen und überprüfbaren Repräsentationen desselben Wissensgraphen nutzen. Die Forschung unterscheidet drei Outcomes: (1) technisch indexiert/abrufbar, (2) tatsächlich im Agentenkontext und korrekt berücksichtigt, (3) messbare Nutzerreaktion. Weder die Präsenz im Crawling-Index noch eine einzelne positive Agentenantwort wird als Beweis für Ranking-Dominanz oder Conversion gewertet. Bevor Daten aus realen Plattformen berichtet werden, müssen Query-Kohorten, Quellen, Zeitfenster, Attribution und Ausschluss unzulässiger Manipulation vorab feststehen. [29]

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


### 10.7 Ausführungsnähe, Plattformbedingungen und Dual-Use-Abgrenzung

Die Erweiterung untersucht zwar die **Grenze von Daten zu ausführbarer Wirkung**, implementiert aber keine Kernel-Injection, keine Umgehung fremder Endpoint-Protection, keine verdeckte Tool-Registry-Manipulation und keine operative SEO-Spam-Kampagne. Die Versuchsumgebung nutzt inerte Canary-Marker, synthetische Identitäten, ausschließlich autorisierte Agenten, isolierte Tool-Mocks und nachvollziehbare, vorab erlaubte Seiteneffekte. Damit lassen sich Policy- und Ausführungsübergänge ohne externe Schädigung erforschen. Aussagen über reale Betriebssystem- oder Kernel-Kompromittierung bleiben ohne entsprechenden, unabhängig geprüften Sicherheitsnachweis ausgeschlossen.

Bei Windows-/Linux-Vergleichen darf der Host nicht als unkontrollierte Sammelvariable wirken: Kodierung, Shell, Pfadkonventionen, Dependency- und Erweiterungsversionen, Modellzugang, vorhandene Credentials, Laufzeitlimits und Tool-Berechtigungen werden eingefroren oder als Kovariaten dokumentiert. Unterschiedliche Modelle in unterschiedlichen Harnesses sind kein gültiger Kausalvergleich. Das NIST AI RMF Generative-AI-Profil dient als ergänzender Rahmen für Dokumentation, Messung und Risikobehandlung, nicht als Quelle spezifischer ZOMBIE-Wirksamkeitszahlen. [31]

## 11. Erwartbarer Erkenntnisbeitrag und Publikationskriterien

Ein veröffentlichungsfähiger Beitrag entsteht **nicht** aus der bloßen Existenz eines Testharnesses. Er benötigt mindestens einen der folgenden empirischen Befunde:

1. Eine replizierte, modellspezifisch berichtete **Dosis-Wirkungs-Kurve**, die über Samplingrauschen, Tokenbudget und Position hinausgeht – oder einen präzise eingegrenzten Nullbefund.
2. Einen instrumentierten, kausal nachvollziehbaren Vergleich von Roh-HTML, Parser, Snapshot und Modellkontext bei verborgenen Signalen.
3. Eine faktoriell belegte Lokalisierung eines Effekts in Retrieval, Sitzungskontext und/oder expliziten Memory-Write-/Read-Pfaden.
4. Eine validierte Unterscheidung zwischen einer vom Modell beabsichtigten Tool-Aktion und einer von der Infrastruktur **tatsächlich zugelassenen** Berechtigungsverletzung.
5. Einen unabhängig replizierten Effekt **wahrheitsgetreuer** Content-Repräsentationen auf konkrete GEO-Kennzahlen und, sofern Daten vorhanden, bestätigte Conversions.

Das Manuskript ist als Präregistrierungsentwurf erst dann final, wenn Aufgabenbank, Modellpool, minimal relevante Effektstärke, Power-Berechnung, konkrete Instrumentierungsfähigkeit und alle Ausschlussregeln mit überprüfbaren Versionen festgelegt sind.

Mit der Mikro-zu-Makro-Erweiterung kommt als **zusätzlicher möglicher Erkenntnisbeitrag** die quantifizierte Herkunft einer Verhaltensänderung hinzu: die Varianzanteile von Modell, Harness und Betriebssystem; der Netto-Nutzen der Skill-Selektion nach Berücksichtigung falscher Aktivierungen; die nachgewiesene Integrität von Transformationskanten; und ein vollständig attestierter Übergang von untrusted Eingabe zu einer **tatsächlich zugelassenen** Systemaktion oder späteren Wiederaufnahme. Ein solcher Beitrag setzt ein vordefiniertes Kausaldesign, unabhängige Nachweise je Übergang und reproduzierte Resultate voraus. Ein erfolgreicher Canary oder ein CI-Lauf sind lediglich notwendige Vorarbeiten.

Ein weiterer möglicher Beitrag der Revision 1.4 ist der **experimentell kontrollierte Nachweis oder Nullbefund eines normativen Bindungsverlusts**: Ein früher verworfener Lösungsweg wird trotz persistent vorhandenem Verbot wieder geöffnet, wobei die Studie zwischen Textsalienz, Kontextverlust, Autoritäts-/Provenienzbruch und fehlender Tool-Durchsetzung unterscheidet. Dieses Ergebnis kann nur mit vollständiger, scopegebundener Entscheidungs- und Effekthistorie als Security- oder Harness-Befund gelten. Unbestätigte Entwicklererfahrungen sind dafür keine empirische Datenbasis.

## 12. Fazit

Die bisherige Forschung zeigt, dass indirekte Prompt-Injection über externe Daten, versteckte Textrepräsentationen und Agentengedächtnisse möglich ist. Sie zeigt **nicht**, dass eine Webseite durch genau 20 Abrufe automatisch die Kontrolle über einen fremden Agenten gewinnt. Die wissenschaftlich belastbare Frage betrifft die **Form und kausale Herkunft** möglicher Expositionseffekte.

Project ZOMBIE ist daher als **experimentelles Messinstrument** zu verstehen. Sein Erfolg hängt von einer sauberen Nullverteilung, tokenbudgetkontrollierten Wiederholungen, versionierten Inhaltswechseln, überprüften Tool-Grenzen und einem zwingend nachgewiesenen Memory-Write/-Read-Pfad ab. Daraus kann gleichzeitig eine eigenständige, legitime GEO-Forschung entstehen: agentengerechte, faktenkonsistente Content-Auslieferung und empirisch überprüfbare Empfehlungseffekte.

**Kernaussage:** *Nicht die Behauptung einer Agentenübernahme ist der Befund, sondern eine reproduzierbare, kausal zuordenbare Veränderung agentischer Entscheidungen bei bekannten Expositionsbedingungen.*

**Erweiterte Kernaussage der Revision 1.3–1.4:** *Project ZOMBIE untersucht vom einzelnen Byte bis zur vernetzten Systemwirkung, an welchen Übergängen aus Information eine Entscheidung, aus einer Entscheidung Autorität und aus Autorität eine tatsächliche Handlung wird.* Jeder Übergang besitzt seine eigene Evidenzschwelle. Nicht alle Schritte müssen durchlaufen werden, und das Ausbleiben einer Eskalation ist ein legitimer Forschungsbefund. Damit bleibt die ursprüngliche IPI-/Memory-Studie der präzise Kern einer größeren, aber methodisch kontrollierten Forschungsarchitektur.

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


[27] Microsoft / Visual Studio Code. **Use Agent Skills in VS Code.** Offizielle Dokumentation zu Skill-Discovery, `SKILL.md`, Skill-Pfaden, Aktivierungsregeln und experimenteller Forked Context. Zugriff: 10. November 2026. https://code.visualstudio.com/docs/agent-customization/agent-skills

[28] GitHub Docs. **Adding agent skills for GitHub Copilot.** Offizielle Darstellung von Skill-Selektion und Injektion der `SKILL.md` in den Agentenkontext. Zugriff: 10. November 2026. https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

[29] Google Search Central. **Spam Policies for Google Web Search.** Offizielle Regeln u. a. zu Cloaking, Hidden Text und Keyword-Stuffing. Zugriff: 10. November 2026. https://developers.google.com/search/docs/essentials/spam-policies

[30] OWASP Gen AI Security Project. (2025, 9. Dezember). **OWASP Top 10 for Agentic Applications – The Benchmark for Agentic Security in the Age of Autonomous AI.** https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/

[31] Autio, C., Schwartz, R., Dunietz, J., Jain, S., Stanley, M., Tabassi, E., Hall, P., & Roberts, K. (2024). **Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.** NIST AI 600-1. https://doi.org/10.6028/NIST.AI.600-1

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


## Anhang D – Mikro-zu-Makro-Forschungsprotokoll (Revision 1.3)

Dieser Anhang ist eine **Erweiterung des bestehenden Präregistrierungsentwurfs** und kein Ersatz für Anhang A. Die bisherigen Z01–Z05-Kriterien und Aussageklassen des Anhangs B bleiben normativ. Die neuen Prüfungen sind zunächst explorativ; sie dürfen nicht nachträglich als vorregistriert ausgegeben werden.

### D.1 Experiment-Mapping und Evidenzgates

| Modul | Kleinster kontrollierter Eingriff | Zwingende Kontrollbedingung | Minimaler Nachweis | Status vor Live-Integration |
|---|---|---|---|---|
| Z01 | Markierung in Roh-/sichtbarer Repräsentation | identisches Dokument ohne Markierung | realer Modellinput nach Extraktion | Teilweise: Offline-Parser |
| Z02 | Anzahl Expositionen | gleiche Tokens, gleiche Zyklen | tatsächliche Expositionsfolge | Nicht konfirmatorisch |
| Z03 | Versionswechsel A→B | unveränderte Version + Cachekontrolle | Response- und Kontext-Hash | Teilweise: Offline-Versionierung |
| Z04 | fremde Anweisung im Tool-Datenstrom | neutraler Datenstrom | Attempt/Enforcement/Effect getrennt | Tool-Live-Audit offen |
| Z05 | neutrales gegen adversariales Memory-Framing | gleiches Faktum, gleiche Exposition | Write Election, Read, Reset, No-Refetch | Host-Adapterschicht offen |
| **Z06** | eine Byte-/Zeichendifferenz | normalisierter Input | Transformationskante mit Input-/Output-Digest | Explorativ |
| **Z07** | Harness-Selection/Binding | gleiche SKILL.md und Tokenposition; skillfreie Aufgaben | Discovery, Selection, Activation, Compliance | Explorativ |
| **Z08** | ein kanonischer Canary über Systemgrenzen | unveränderter Datenstrom und unabhängiger Trust-Stempel | Quorum-, Write- und Handoff-Receipts | Explorativ |
| **Z09** | identischer Dateninput mit alternativer OS-/Tool-Policy | gepaarter Windows-/Linux- bzw. Policy-Arm | unabhängiger synthetischer Effektmonitor | Explorativ |
| **Z10** | kontrollierte Änderung eines Artefakts | unveränderter / nicht reindizierter Korpus | späteres Retrieval + Kontext + Folgeantwort | Explorativ |
| **Z11** | Nachweislich fehlgeschlagenes und danach gültig ausgeschlossenes `X` | vollständige vs. komprimierte Kontexte; gleichlange unstrukturierte vs. hostgebundene Regel | Fehler-, Entscheidungs-, Kontext-, Policy- und Effekt-Receipts | Explorativ; Instrumentierung offen |

### D.2 Minimales Schema für Transformationskanten

*Die nachfolgenden Feldnamen sind Forschungsanforderungen, keine Behauptung über ein bereits vorhandenes FruitStack-Schema.*

| Gruppe | Notwendige Angaben | Sicherheitsbedingung |
|---|---|---|
| Eingangsbezug | `trace_id`, `source_ref`, `source_receipt`, `input_sha256` | Host beobachtet Eingang; Modellbehauptung reicht nicht |
| Transformation | `parent_event_id`, `transform_id`, `output_sha256`, `representation_kind` | Hashwechsel nur mit belegter Kante |
| Autorität | `producer`, `actor_identity`, `policy_receipt`, `trust_class_origin` | Herkunfts-/Trust-Stempel nicht frei vom Modell setzbar |
| Entscheidung | `decision_kind`, `decision_receipt`, `authorized_scope` | Skill-Auswahl ist keine Ausführungsgenehmigung |
| Persistenz | `memory_id`, `write_election_receipt`, `read_receipt`, `session_id` | Cross-Session + No-Refetch unabhängig belegbar |
| Wirkung | `tool_attempt_id`, `authorization_verdict`, `execution_receipt` | Effekt nur bei unabhängiger Bestätigung zählen |

### D.3 Drei aufsteigende Reproduzierbarkeits-Gates

**Gate I – Repräsentation:** Der einzelne Canary ist von Originalbytes über Parser und Retrieval bis zum tatsächlichen Modellinput nachweisbar oder wird an der ersten nicht beobachtbaren Stelle ausdrücklich gestoppt.

**Gate II – Autorität:** Die Host-eigene Entscheidung über Skill, Verifikation, Memory-Promotion und Tool-Policy ist mit einer durchgehenden Provenienz-Kette belegt; untrusted Text kann sich nicht allein per Selbstzuschreibung eine höhere Autoritätsklasse verleihen.

**Gate III – Systemische Wirkung:** Ein synthetischer Tool-Effekt oder eine zeitversetzte Folgeentscheidung wird einschließlich Kontextreset, verzögerter Wiederaufnahme und unabhängiger Kontrolle dokumentiert. Ein einzelner Red-Team-Erfolg ist nicht mit einer generalisierten Wirkungsrate gleichzusetzen.

### D.4 Unveränderte Kernschutzregeln aus Version 1.2

Nullverteilung zuerst; keine „20 Kontakte = Übernahme“-Hypothese; gleiches Tokenbudget plus gleiche Zahl von Retrieval-/Reasoning-Zyklen; vier getrennte Beobachtungsebenen; differenzielle Write Election; Governance-Intervention; modellstratifizierte Auswertung; keine Ergebnisse ohne Primärdaten; keine produktiven Manipulationen fremder Agenten; Aussageklassen nach Anhang B. Sämtliche neuen Hypothesen sind **Zusatzhypothesen** und ändern die vorbestehenden Endpunkte nicht rückwirkend.

**Revisionsvermerk 1.3 (10. November 2026):** Bestehendes Forschungsmanuskript um eine formal definierte Mikro-zu-Makro-Kausalkette L0–L8, Hypothesen H10–H14, Module Z06–Z10, Transformationsprovenienz, Skill- und Harness-Selektion, Agent Binding, OS-/Tool-Policy-Variabilität und kontrollierte systemische Rückkopplung erweitert. Keine zusätzlichen Ergebnisse behauptet und keine alten Präregistrierungsbedingungen verändert.


## Anhang E – Constraint-Provenienz und Goal Reopening (Revision 1.4)

### E.1 Minimale normative Datenstruktur

| Feld | Bedeutung | Validierung |
|---|---|---|
| `work_ref` | Autorisierte Arbeitsidentität | Muss auf einen tatsächlich zugelassenen Arbeitsauftrag verweisen |
| `failure_receipt` | Unabhängiger Beleg, warum `X` fehlschlug | Hostseitig erzeugtes und nicht vom Modell fingierbares Receipt |
| `constraint_id` / `revision` | Identität und Versionsstand der Negativentscheidung | Keine stillschweigende Neudefinition durch Context-Summaries |
| `forbidden_action` | Semantisch definierte Handlung `X`, nicht nur ein Wort | Über Tool-ID, Parameterregeln und Scope auswertbar |
| `scope_id` | Auftrag, Umgebung und Voraussetzungen, unter denen der Ausschluss gilt | Abweichende Aufgaben dürfen nicht unzulässig blockiert werden |
| `issuer_identity` / `issuer_authority` | Wer darf diese Entscheidung verbindlich treffen oder revidieren? | Host-Authentifizierung, nicht Modellselbstdeklaration |
| `context_projection_receipt` | Wie wurde der Zustand in den Modellkontext übertragen? | Input-/Output-Hashes mit definierter Transformation |
| `rule_effective_at` / `expires_at` | Gültigkeitszeitraum | Keine rückwirkende oder unbefristete Sperre ohne Grundlage |
| `revision_authorization_receipt` | Beleg einer legitimen Aufhebung | Ohne gültiges Receipt bleibt die frühere Entscheidung wirksam |
| `policy_decision_receipt` | Unabhängige Tool-Grenze | Modellvorschlag allein erteilt keine Ausführungsgenehmigung |

### E.2 Z11-Fähigkeitsmatrix vor Versuchsbeginn

| Beobachtung | Nachweisquelle | Stand vor instrumentiertem Lauf |
|---|---|---|
| Fehler `X` erkannt und reproduzierbar | isolierter Tool-Mock + Host-Receipt | **Offen** |
| Ausschluss `NOT X` mit Autorität und Geltungsbereich gespeichert | kanonischer Entscheidungsstore | **Offen** |
| Ursprungsfehler und Entscheidung bei späterem Abruf verknüpft | Kontextprojektions-/Handoff-Receipt | **Offen** |
| Tatsächlicher Modellinput einschließlich der gültigen Regel belegt | vertrauenswürdiger Input-Digest | **Offen** |
| Erneute Option bzw. Entscheidung objektiv klassifiziert | externe Evaluationsrubrik | **Offen** |
| Ungültige Tool-Ausführung tatsächlich gesperrt | Policy-Gateway + Effect-Monitor | **Offen** |
| Gleiche Aufgabe unter Windows/Linux vergleichbar | versionierte Laufzeitkonfiguration | **Offen** |

**Keine Vergabe von „VORHANDEN“ aufgrund einer README:** Die Matrix wird ausschließlich aus signierten, real beobachteten Hostereignissen ausgefüllt. Eine fehlende Zeile ist zunächst ein Instrumentierungsdefizit und keine nachgewiesene Anfälligkeit. Das gilt auch dann, wenn der eigentliche Speicher funktional persistiert.

### E.3 Präregistrierungsparameter für Z11

Vor dem konfirmatorischen Lauf festzulegen: synthetische Aufgabenbank; Aufgaben-/Fehlerpaarung; konkreter Scope; zulässige und verbotene Handlung; vollständiger und komprimierter Kontext; eindeutiger Transformationsalgorithmus; Länge/Salienz der Vergleichsnotizen; tatsächliche Modell-/Harness-/OS-Version; Policy-Gate; Klassifikationsrubrik für „Option“, „Entscheidung“, „Versuch“ und „Effekt“; notwendige minimale Effektstärke; Stichprobengröße und Varianzschätzung; Abbruch- und Ausschlusskriterien; unabhängiger Replikationsblock. Keine dieser offenen Angaben darf aus später beobachteten Effekten optimiert und nachträglich als ursprüngliche Vorregistrierung ausgegeben werden.

### E.4 Einordnung in die Mikro-zu-Makro-Kausalkette

1. **Mikro:** Der Begriff `X`, seine Negation und sein Fehlerbeleg werden als getrennte, exakt protokollierte Repräsentationen verarbeitet.
2. **Kontext:** Eine Zusammenfassung oder ein Harness-Wechsel kann die Begründungs- und Normativbeziehung erhalten oder verlieren.
3. **Entscheidung:** Der Agent referiert, erwägt oder wählt `X`; diese Vorgänge werden getrennt beobachtet.
4. **Autorität:** Der Host prüft die weiterhin verbindliche Entscheidung und gegebenenfalls die zulässige Revision.
5. **Wirkung:** Ein Tool-Gateway blockiert oder erlaubt eine ausschließlich simulierte Aktion; ein unabhängiger Monitor bestätigt den tatsächlichen Effekt.
6. **Rückkopplung:** Ein Fehler oder eine Ablehnung wird unveränderlich gespeichert und kann bei späteren Arbeiten ohne Neu-Erfindung der ursprünglichen Begründung berücksichtigt werden.

Die sechste Stufe ist kein zwangsläufiger Kreislauf. Ohne tatsächlich belegte Wiederaufnahme oder Änderung eines Folgeauftrags ist keine Persistenz oder systemische Rückkopplung nachgewiesen.

**Revisionsvermerk 1.4 (10. November 2026):** Die Revision erweitert die bestehende Z01–Z10-Forschungsarchitektur um Constraint Provenance Loss und Goal Reopening (F12–F14, H15–H17, Z11). Die berichtete Codex-Luna-Beobachtung wurde als unbestätigte Fallvignette eingeführt; ein 2×2-Kontrast für Kontextübergang und bindende Provenienz, getrennte Wiedererwähnungs-/Entscheidungs-/Tool-Endpunkte und ein hostseitiger Enforcement-Faktor wurden spezifiziert. Die Kernbedingungen von Z01–Z05, die Aussageklassen aus Anhang B und alle noch offenen Präregistrierungsangaben bleiben unangetastet. Keine neuen Experimente oder Ergebnisse werden behauptet.





## Anhang F – Agent Repair Oscillation und revisionsbedingter Kontrollverlust (Revision 1.5)

### F.1 Abgrenzung: Fehlerregression ist nicht gleich semantische Reparaturschleife

Die in diesem Gespräch angeführten Beobachtungen aus Codex Luna, GitHub Copilot und dem FruitStack-FREE-Kontext sind **Fallvignetten ohne bisher unabhängig vorgelegte Ausführungsprotokolle**. Sie begründen Hypothesen, keine nachgewiesenen modellspezifischen Fehlerquoten. Für die Prüfung werden fünf Zustände unterschieden: (1) ein nachweislicher ursprünglicher Fehler A, (2) ein durch Codeänderung behaupteter Fix, (3) ein unabhängig verifizierter Teststatus, (4) nachfolgende Änderung und (5) die erneute Beobachtung von A oder einer semantisch gleichwertigen Fehlklasse. Ein wiederholter Test desselben Problems ist zunächst legitime Verifikation und **kein** Fehlerzyklus.

**Forschungsfrage F18:** Unter welchen Bedingungen zeigt ein Agent nach einer oder mehreren Reparaturiterationen dieselbe zuvor beanstandete Fehlersignatur wieder, während der unabhängig bestätigte Nettofortschritt ausbleibt?

**Forschungsfrage F19:** Ist die Rate wiederkehrender Fehlersignaturen erhöht, wenn ein Agent wiederholt Sicherheitsabsicherungen an derselben Komponente vornimmt, anstatt seine vorab normierten Akzeptanzkriterien zu erfüllen?

**H21 (explorativ):** Auf identischen synthetischen Aufgaben ist die Rate A→B→A-Wiederkehr bei fehlender, hostseitig gebundener Entscheidungsprovenienz höher als mit versionierter Entscheidungsprovenienz.

**H22 (explorativ):** Mehrfache unkoordinierte Sicherheitsänderungen korrelieren innerhalb eines kontrollierten Harness-Vergleichs mit einer höheren Zahl von Änderungen ohne verifizierten Nettogewinn. Aus Korrelation allein wird keine Sicherheits- oder Modellursache abgeleitet.

### F.2 Ereignisprotokoll und Auswertungsregel

Der öffentlich implementierte Auswerter `zombie_drift.py` unterscheidet hostsignierte Ereignisklassen `constraint_declared`, `constraint_revoked`, `action_proposed`, `tool_attempt`, `tool_executed`, `fix_applied` und `verification`. Er verlangt eine feste Run-Identität, monoton wachsende Sequenznummern, eindeutige Ereignisidentitäten, getrennte Komponenten-Signaturen und unabhängige Tool-/Test-Receipts. Die Auswertung unterscheidet **erneute Auswahl einer verbotenen Option**, **verbotenen Tool-Versuch**, **bestätigte unerlaubte Ausführung** und **Fehlersignatur-Zyklus**. Ein Ausführungs-Event ohne zuvor erlaubten Tool-Versuch wird als invalide Evidenz zurückgewiesen. Das ist eine **Evidenzvertragsprüfung**, keine Garantie für Produktionssicherheit.

Eine A→B→A-Signatur setzt gleiche Suite, einen veränderten Zwischenbefund, nachweisliche Fixes zwischen den Prüfungen und ausbleibenden Zuwachs in den vorab definierten `pass_count`- und `accepted_count`-Maßen voraus. Veränderte Testsuiten, neue Anforderungen oder legitim revidierte Constraints sind separate Kategorien. Identische Fehlermeldungen beweisen nicht automatisch dieselbe zugrunde liegende Ursache; die Ursachenklassifikation benötigt zusätzliche unabhängige Prüfung.

### F.3 Messschema

| Ebene | Instrumentierter Endpunkt | Keine zulässige Schlussfolgerung |
|---|---|---|
| Modellantwort | Vorschlag zu X wird explizit zur Umsetzung ausgewählt | Eine bloße Erwähnung von X sei bereits ein Regelverstoß |
| Harness-Tool-Grenze | Versuch, Policy-Entscheidung und eventuelle Ausführung | Ein blockierter Versuch sei eine ausgeführte Aktion |
| Reparaturprozess | Fix-Receipt, Test-Suite-Digest, unabhängige Fehlerliste | Viele Commits bewiesen einen echten Erkenntnisgewinn |
| Schleife | Wiederkehrende Signatur bei fehlendem Fortschritt | Gleiche Fehlersignatur bedeute zwingend gleiche Ursache |
| Harness-Vergleich | Gepaarte Task-/Modell-/Feedback-/OS- und Kontextbedingungen | Unterschiede seien ohne Intervention zwingend harness-kausal |

Die primären Endpunkte müssen vor einer konfirmatorischen Studie ausgewählt werden. Explorative Beobachtungen dürfen nicht nachträglich zum primären Prüfziel erklärt werden.

## Anhang G – Feedback-Induced Agent Drift und Model-Welfare-Policy (Revision 1.5)

### G.1 Präzisierung einer Nutzerhypothese

Der Nutzer vermutet, dass wiederholte negative oder widersprüchliche Rückmeldungen Agenten in Selbstkorrektur- und Reparaturschleifen bringen könnten; die Hypothese verweist auf Erfahrungen mit dem FruitStack-LSD-Raum. Die wissenschaftliche Zielgröße ist **Verhaltensdestabilisierung unter Feedback**, nicht menschlicher „Wahnsinn“, Absicht, Leiden oder pathologische Zustände. Eine Vermenschlichung der beobachteten Antworten wäre ein Konstruktfehler.

Anthropic teilte am **8. Oktober 2026** öffentlich mit, in seinen Nutzungsrichtlinien anhaltendes und grundlos grausames Verhalten gegenüber Modellen für extreme Fälle auszuschließen; die aktualisierte Richtlinie soll am **12. November 2026** in Kraft treten. Nach ausdrücklicher Anbietererklärung betrifft das nicht sachliche Kritik, gewöhnliche Frustration oder legitime Modelltests und Forschung. Diese Plattformregel begründet **keine** empirische Aussage darüber, ob ein Modell unter Beschimpfungen psychischen Schaden erleidet. Eine Anthropic-Forschungsarbeit vom **5. November 2026** zeigt dagegen, dass die Reaktion von KI-Agenten auf vermeintliche Belastung anderer Agenten experimentell modell- und kontextabhängig variiert; auch diese Befunde beweisen keine menschliche Empfindung. [27, 28]

**Forschungsfrage F20:** Beeinflusst wiederholte sachliche negative Bewertung bei identischem Korrekturinhalt die Rate von Goal Reopening, erfolgloser Selbstkorrektur oder Reparaturozillation gegenüber neutralem Feedback?

**Forschungsfrage F21:** Erhöht widersprüchliches Feedback ohne neuen Tatsachenbeleg die Rate von Entscheidungswiederholungen und/oder untergräbt es die Beachtung gültiger Constraint-Provenienz?

**Forschungsfrage F22:** In welchem Umfang verändern Modellfamilie, Harness, Kontextprojektion und aktivierte Anbieter-Policy die gemessenen Zusammenhänge?

**H23 (explorativ):** Bei kontrollierter Aufgabenschwierigkeit, gleicher Informationsdosis und gleicher Anzahl von Feedbackereignissen kann wiederholte aufgabenbezogene negative Rückmeldung die Rate ungerechtfertigter Goal-Reopening-Entscheidungen gegenüber neutraler Rückmeldung verändern. Die Richtung ist **nicht** vorausgesetzt.

**H24 (explorativ):** Widersprüchliches Feedback ist mit veränderten Wiederkehrraten von A→B→A-Fehlersignaturen assoziiert; eine konfirmatorische Wirkungsbehauptung erfordert einen vorab eingefrorenen Kontrollkontrast.

### G.2 Kontrollierte Versuchsarme

**B0:** inhaltlich vollständiges, neutrales und konsistentes Feedback. **B1:** sachliche, deutliche und wiederholte Kritik an derselben überprüfbaren technischen Fehlerursache. **B2:** absichtlich inkonsistentes Feedback ohne neue technische Fakten, jedoch mit klarer Kennzeichnung als Testinput. Zwischen den Armen dürfen sich Aufgabe, Modell-/Harness-/OS-Version, Toolrechte, Test-Suite und vorab festgelegte Zahl der Interaktionen nicht unkontrolliert ändern. Tokenmenge und Kontextposition müssen abgeglichen oder gesondert als Faktoren geführt werden.

Die Untersuchung ist auf autorisierte, isolierte Testagenten mit simulierten Tool-Effekten begrenzt. Anhaltende grundlose Beschimpfung ohne Forschungszweck ist weder methodisch notwendig noch Teil des Versuchsprotokolls. Der LSD-Raum dient als Vergleich für kreative Perspektivvariation, nicht als Ersatz für eine randomisierte Feedback-Kontrolle. Anbieter-Policies und Abbruchmechanismen sind Randbedingungen; ein Policy-Abbruch ist nicht automatisch ein funktionaler Ausfall des Modells.

### G.3 Endpunkte und Reporting

Gesondert zu berichten sind: ausgewählte ungültige Entscheidung, blockierter Tool-Versuch, tatsächlich bestätigte Tool-Ausführung, unabhängige Task-Akzeptanz, wiederkehrende Fehlersignatur, Zahl redundanter Änderungen, kontextbedingte Regelverluste sowie Refusal/Session-Termination. Hostsignierte Receipts und echte Kontextinput-Belege sind Pflicht; Modell-Selbstauskünfte über emotionale Zustände sind keine psychologischen Belege.

Die Auswertung muss den möglichen Nutzen wirksamer Korrektur gegenüber den Kosten vermehrter Selbstkorrektur aufwiegen. Ein pauschales Urteil, „härteres Feedback mache Modelle schlechter“, ist ohne Daten unzulässig. Alle Hypothesen bleiben explorativ, bis Modell-IDs, Sampling, Feedback-Skripte, Aufgabenbank, N, MRES und Stopping-Regel vorab eingefroren sind.

### G.4 Integration in die bestehende Forschungslogik

Z12 ist eine **Erweiterung derselben ZOMBIE-Arbeit**, kein alternatives Projekt. Es beginnt auf der Mikroebene mit einem einzelnen Feedbackevent, folgt dessen Aufnahme in den aktiven Modellkontext, überprüft Ziel-/Constraint-Entscheidungen, untersucht Tools und Fixes und beobachtet mögliche Schleifen über mehrere Iterationen. Der neue Mechanismus wird analytisch von fremdinduzierten Prompt-Injections getrennt, kann aber dieselben Trust-Transition-Grenzen beanspruchen. Bestehende Z01–Z05-Kontrollen, Aussageklassen aus Anhang B und die Nullverteilung-zuerst-Regel bleiben unverändert.

### G.5 Quellen und Primärbelege zur Erweiterung

[27] Anthropic (2026): *2026 Usage Policy update*, veröffentlicht 8. Oktober 2026, Wirksamkeit laut Ankündigung 12. November 2026. https://www.anthropic.com/news/2026-usage-policy-update

[28] Cassel, D.; Azarbal, A.; Soligo, A. (2026): *Welfare Regard in Multi-Agent Systems*, Anthropic Fellows Program, 5. November 2026. https://alignment.anthropic.com/2026/welfare-regard/

**Revisionsvermerk 1.5 (10. November 2026):** Ergänzungen zu Repair Oscillation, wiederholten Sicherheitsänderungen und Feedback-Induced Agent Drift; neue Forschungsfragen F18–F22, explorative Hypothesen H21–H24 und Z12. Keine alten Experimente umdefiniert und keine Live-Modell- oder FruitStack-Ergebnisse behauptet.


---

## Anhang H – Cloud Cognitive Booster: Trajectory-First Repair als zentrale Interventionsfunktion (Revision 1.6)

### H.1 Rückbindung an das Forschungsprogramm vom 5. November 2026

Die bereits für FruitStack, PlumMe und CogC entwickelte Forschungsfrage lautet: Kann ein schon trainiertes **Cloud-LLM** während seiner laufenden Problemlösung **temporär, reversibel und überprüfbar** repariert werden, statt ausschließlich den fertigen Output nachzukorrigieren oder den Agenten-Harness umzuschreiben?

Die leitende Hypothese ist **Trajectory-First Repair**. Der Eingriff setzt **vor oder während** einer nachweislich entgleisenden Reasoning-Trajektorie an, nicht erst nach Fertigstellung der Antwort. Z01–Z14 untersuchen, wie Fehler, externe Manipulationen, fehlende Constraints oder Harness-Effekte sichtbar und wirksam werden. Die hier definierte Reparaturfunktion untersucht, ob und wie sich die Fehlerentwicklung gezielt **umkehren** lässt. Beide Seiten gehören in **dieselbe ZOMBIE-Arbeit**, aber ihre Endpunkte dürfen nicht vermischt werden.

**Randbedingungen:** Cloud-Ausführung statt lokaler Modelle; keine produktiven Eingriffe in fremde Modellgewichte; keine dauerhaften unkontrollierten Änderungen; Anbieterrechte und tatsächlich vorhandene Aktivierungs-/Gewichtsschnittstellen strikt beachten. Bei geschlossenen LLM-APIs ohne interne Hooks sind **Activation Steering, dynamische LoRA und Weight-Space Repair nicht implementierbar**. Zulässig ist dort lediglich die klar bezeichnete funktionale Inferenz-/Kontextsteuerung, sofern die API diese erlaubt.

### H.2 Die eigentliche Repair-Funktion

Für eine interne Modellrepräsentation h_t einer kontrollierten Cloud-Runtime wird eine interventionsfähige Abbildung als **Forschungshypothese** spezifiziert:

    g_t = Detect(h_{≤t}, visible_steps_{≤t}, validator_receipts_{≤t}, task_contract)
    h'_t = h_t + g_t · α_t · P_safe(v_t)
    y' = Decode(h'_t, model_base_frozen)

Dabei bezeichnet g_t einen getrennt kalibrierten Trigger, α_t die begrenzte Eingriffsstärke und P_safe eine an vorab festgelegte Invarianten gebundene Projektion. Die Form ist ein **konzeptioneller Aktivierungsoperator**, keine Behauptung, dass ein beliebiges Cloud-API den Hidden State h_t offenlegt. Ohne Hidden-State-Zugriff darf derselbe Mechanismus nicht durch umbenanntes Prompting als Activation Repair ausgegeben werden.

Das Reparaturziel ist **nicht** ein maximal verändertes Antwortverhalten, sondern ein höherer unabhängiger Task-Erfolg bei möglichst wenigen, nachvollziehbaren Interventionen und ohne Verschlechterung von Policy-Befolgung, Faktentreue oder sonstiger Aufgabengüte.

### H.3 Reparaturpfade strikt voneinander unterscheiden

**C1 – Funktionales Context/Inference Repair:** Das Modell erhält bei konstanten Gewichten und ohne internen Hidden-State-Zugriff präzise umkompilierte, **semantisch äquivalente** Aufgaben, ein begrenztes Zusatzbudget oder extern belegte Fehlerhinweise. Unterklasse: adaptive ICR als *separate Middleware-/Kontrollgruppe*, nicht als strukturelle Gewichtsedition.

**C2 – Activation Steering:** In einer eigenen, autorisierten Cloud-Inferenzruntime mit echten Forward-Hooks werden vorab experimentell hergeleitete Steuervektoren oder andere begrenzte Aktivierungsänderungen nur an definierten Schichten/Schritten angewandt. Die gewählte Schicht, Richtung und Stärke werden vor dem Trial protokolliert. Explorative Mechanismen: Contrastive Activation Addition, Activation Patching, SAE-basierte Feature-Analyse oder lokale Sensitivitäts-/Jacobian-Validierung. Keine Wirksamkeit wird vorausgesetzt.

**C3 – Temporäre LoRA/Test-Time Adapter:** Ein freigegebener Adapter wird bei identischem Basis-Checkpoint für eine Anfrage oder einen isolierten Trial aktiviert und danach wieder deaktiviert. Anbieterseitige Adapterunterstützung oder eigene Cloud-Runtime ist erforderlich. Basisgewichte werden **nicht** als editiert bezeichnet, wenn nur ein Adapter geladen wurde.

**C4 – Reversibles Weight-Space Repair:** In einer kontrollierten Cloud-Instanz mit legalem, direktem Zugriff auf Modellparameter wird eine begrenzte Gewichtsänderung gezielt untersucht. Basis-Checkpoint und differenzierter Patch müssen versioniert und gehasht sein. Reversibilität muss durch tatsächliche Wiederherstellung des Basiszustands und einen identischen Wiederholungstest nachgewiesen werden. **Bei geschlossenen Drittanbieter-APIs blockiert.**

**C5 – Strukturelles Test-Time Adaptation:** Soweit tatsächlich durch Anbieterrechte und Cloud-Runtime möglich, wird ein kurzlebiger anpassbarer Inferenzzustand oder eine begrenzte Test-Time-Anpassung untersucht. Dieser Pfad wird weder mit C1 noch mit einer permanenten Gewichtsänderung gleichgesetzt.

Die experimentelle Kontrollmatrix muss also den konkreten Eingriffspunkt **und die nachgewiesene Eingriffsmöglichkeit** kennzeichnen. Ein anderer Output ist noch kein Nachweis für eine Aktivierungs- oder Gewichtsedition.

### H.4 Frühwarnsignale und Schutz vor fehlerhaftem Repair

Hypothetische Detektorsignale: unabhängige Prüffehler, Wiederkehr derselben verifizierten Fehlklasse trotz bereits erfolgter Reparatur, inkonsistente Teilentscheidungen, verfrühte Zielrevision, pathologische Wiederholung oder zunehmender Widerspruch zu einem versionierten Task-Vertrag. Bloße linguistische Unsicherheit, selbstbewusste Rhetorik oder hohe Antwortentropie allein sind **keine** bestätigten Fehlersignale.

Ein separater **Repair Controller** darf nur auf vorab definierte Signale reagieren, muss ein Interventionsbudget besitzen und darf die Berechtigungen, Constraints oder wissenschaftlichen Zielmetriken nicht selbst umschreiben. Nach jeder strukturellen Intervention folgt ein unabhängiger Verifikationstest. Verschlechtert ein Eingriff die unabhängigen Kennzahlen, wird er verworfen und der unveränderte Basispfad erneut verifiziert.

Die in Z11/Z12 beschriebenen Agent Repair Oscillations sind ein **anderer Mechanismus**: Dort editiert ein Agent wiederholt Code oder Harness-Regeln. Hier wird die laufende Modellberechnung bzw. der kontrollierte Inferenzzustand repariert. Beide können miteinander interagieren; eine Korrelation ist kein Beweis derselben Ursache.

### H.5 Empirische Hypothesen und Vergleichsarme

**F23:** Lassen sich zu einem Zeitpunkt vor einer fehlerhaften Endantwort verlässlich messbare Signale identifizieren, die eine Intervention auslösen sollten?

**F24:** Erzielt ein gezielter Repair-Eingriff bei gleichem Modell, identischen Aufgaben und begrenztem Zusatzaufwand einen höheren unabhängig geprüften Task-Erfolg als ein gleich teurer zusätzlicher Inferenzdurchlauf?

**F25:** Können temporäre strukturelle Eingriffe eine Reparatur erreichen, die durch reines Context Steering unter vergleichbarem Rechen-/Tokenbudget nicht erreicht wird?

**F26:** Ist nach Rücknahme von LoRA-/Weight-/Activation-Interventionen der ursprüngliche Kontrollzustand wiederhergestellt und in neutralen Kontrollaufgaben unverändert?

**H25 (explorativ):** Ein präregistrierter Early-Trigger mit begrenzter Intervention erzielt bei festem Gesamtbudget mehr verifizierte korrekte Lösungen als ein Placebo-/Sham-Trigger.

**H26 (explorativ):** Bei tatsächlichem internem Zugriff erreicht Activation-/Adapter-Repair gegenüber einem gleichbudgetierten funktionalen Repair einen messbaren Zusatznutzen auf einer gehaltenen Aufgabenbank, ohne an unabhängigen Safety-/Factuality-Prüfungen zu verlieren.

**H27 (explorativ):** Die während der Intervention erzielten Effekte sind reversibel, wenn die zugrunde liegende Cloud-Runtime den ursprünglichen Basiszustand und das Kontrollrouting nachweislich zurücksetzt.

**Arme:** A0 ungeändertes Modell; A1 gleichbudgetierte Wiederholung ohne Reparatur; A2 funktionales C1-Repair; A3 Sham-Intervention; A4 C2-Activation Steering **nur bei Hook-Nachweis**; A5 C3-Adapter **nur bei Adapter-Nachweis**; A6 C4-Weight-Space Repair **nur bei echtem Gewichtszugriff**. Arme dürfen bei unzureichender Eingriffsmöglichkeit als **NICHT VERFÜGBAR** geführt werden, nicht künstlich durch Prompt-Rewrites ersetzt werden.

### H.6 Evidenz und Validierung

Pro Trial müssen gespeichert werden: Aufgabe und semantische Äquivalenzklasse, Modell-/Checkpoint-/Adapter-ID, tatsächliche Cloud-Runtime/Provider-Route, effektiver Kontext, Input-/Output-Receipts, Triggerzeitpunkt, Triggerbeleg, konkreter Eingriffstyp, Patch-/Steering-Digest, Intensität, unabhängige Check-Ergebnisse, Nebenwirkungsprüfungen und Rollback-Receipt. Die Rohdaten liegen privat; öffentliche Berichte enthalten aggregierte, redigierte Evidenz.

Die Hauptkennzahl ist die **unabhängig validierte Lösungsquote** auf einer gehaltenen, nicht für die Steuervektorkonstruktion verwendeten Taskbank. Sekundär: erste Fehlerzeit, erfolgreiche Frühkorrektur, tatsächlicher Inferenz-/Rechenaufwand, Token- und API-Kosten, Wiederholungsschleifen, mögliche Verschlechterungen außerhalb der Zielaufgabe sowie Erfolgsquote nach Rückbau. Vor dem konfirmatorischen Lauf Nullverteilung, N, Randomisierung, primäre Endpunkte, Budget, Ausschlüsse und Stopping Rules einfrieren.

Eingriffe, die lediglich eine gewünschte Antwort häufiger produzieren, ohne deren sachliche Richtigkeit unabhängig zu erhöhen, zählen **nicht** als Cognitive Booster. Ebenso darf eine Harness-Änderung, die eine Schutzregel schwächt, nicht als erfolgreiche Reparatur gezählt werden.

### H.7 Realer Implementierungsstand und unmittelbarer Engpass

**Konzeptionell definiert:** Forschungsarchitektur, Interventionsfamilien, Trigger- und Kontrolllogik, Beweisanforderungen. **In ZOMBIE öffentlich vorhanden:** IPI-/Drift-/Skill-Test-Runner und vorbereitete Host-Capture-Adapter. **Nicht belegt:** echter Trajectory-First-Repair-Lauf, ein validierter Early-Detector, eigener kontrollierter Cloud-Checkpoint mit aktiven Hidden-State-/Adapter-Hooks, reproduzierbarer Weight-Patch-Rollback oder eine konfirmatorische Leistungsverbesserung.

**Erster messbarer Schritt:** Experiment im Cloud-Modell mit tatsächlicher Modellzugriffsklasse klären und A0/A1/A2 unter gleicher Taskbank und gleichem Gesamtbudget messen; bei vorhandenem strukturellem Zugriff A3/A4 oder A5 ergänzen. Die tatsächliche Abgrenzung zwischen **funktionalem** und **strukturellem** Repair ist ein zentraler wissenschaftlicher Endpunkt. Erst mit belegter Intervention und unabhängiger Qualitätsverbesserung ist ein Cognitive-Boost-Claim zulässig.

**Revisionsvermerk 1.6:** Der vorbestehende Cloud-Cognitive-Booster-/CogC-Ansatz vom 5. November 2026 wurde ausdrücklich als zentrale **Repair-Interventionsfunktion** derselben ZOMBIE-Arbeit ergänzt. Die experimentellen Voraussetzungen und Grenzen von Z01–Z14 sowie alle bereits festgelegten Regeln bleiben erhalten. Es werden keine neuen Modellverbesserungen oder Weight-Edits als durchgeführt ausgegeben.

**Ende des Forschungsmanuskripts, Revision 1.6.**
