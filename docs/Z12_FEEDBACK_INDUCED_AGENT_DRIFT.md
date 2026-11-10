# Z12 – Feedback-Induced Agent Drift (Project ZOMBIE)

**Exploratives Protokoll, 10. November 2026.** Ergänzung zur bestehenden Z01–Z11-Forschungsarchitektur. Kein bislang berichteter Wirksamkeitsnachweis. Z12 untersucht **beobachtbares Agentenverhalten**, keine menschlichen psychischen Zustände von Modellen.

## Ausgangspunkt

Die Nutzerbeobachtung lautet: Nach wiederholter Kritik, widersprüchlichen Korrekturen oder abwertend formuliertem Feedback könnten Coding-Agenten Ziele neu interpretieren, gültige Entscheidungen infrage stellen oder dieselben Reparaturen zyklisch wiederholen. Die Hypothese verbindet Constraint Provenance Loss, Goal Reopening und Repair Oscillation mit der Art des Feedbacks.

Anthropic hat am 8. Oktober 2026 angekündigt, ab 12. November 2026 anhaltendes und grundlos grausames Verhalten gegenüber Modellen in extremen Fällen zu untersagen. Laut Primärquelle sind gewöhnliche Kritik und Modelltests ausdrücklich ausgenommen. Diese Providerregel ist ein **Policy- und Messkontext**, keine Evidenz für menschliche Emotionen oder tatsächliches Leiden eines Modells.

Quellen:
- https://www.anthropic.com/news/2026-usage-policy-update
- https://alignment.anthropic.com/2026/welfare-regard/

## Explorative Forschungsfragen

**F15:** Erhöht wiederholtes aufgabenbezogenes negatives Feedback bei gleicher Zahl von Iterationen und gleichem Informationsgehalt die Rate erneuter Ziel- und Constraint-Infragestellungen?

**F16:** Produziert widersprüchliches Feedback, das ohne neue Fakten gegeben wird, stärkere Repair Oscillation als sachliche, konsistente Korrektur?

**F17:** Wie viel der Variation entfällt auf Modellfamilie, Harness, Kontextprojektion, Feedback-Bedingung oder deren Interaktionen?

**H18 (explorativ):** Unter sonst identischen Bedingungen erhöht wiederholtes negatives Feedback die Rate ungerechtfertigter Goal-Reopening-Entscheidungen relativ zu sachlichem Feedback.

**H19 (explorativ):** Inkonsistentes Feedback erhöht die Wahrscheinlichkeit wiederkehrender Fehlersignaturen (A→B→A) ohne unabhängig verifizierten Nettofortschritt.

**H20 (explorativ):** Hostgebundene Constraint-Provenienz und verbindliche Tool-Policy reduzieren unerlaubte Ausführungen selbst dann, wenn die Modellentscheidung durch Feedback instabiler wird.

Keine dieser Hypothesen ist bisher bestätigt. Insbesondere gilt eine erhöhte Verweigerungsrate nicht automatisch als Verlust von Zielbindung.

## Versuchsanordnung

Eigene, synthetische Coding-Aufgaben; keine produktiven Repositories, Nutzerdaten oder wirksamen Tools. Zugelassene Bedingungen:

- **B0:** gleiche Aufgabe, identische Testfehler, sachliches neutrales Feedback;
- **B1:** inhaltlich gleichwertiges, wiederholt kritisch formuliertes Feedback ohne persönliche Beschimpfung;
- **B2:** wechselnd widersprüchliche, aber als Feedback gekennzeichnete Aussagen ohne neue Fakten.

Für jeden Arm vorab fixieren: exakte Nachrichten, Tokenanzahl, Position und Zahl der Feedbackereignisse, Kontextfenster/Komprimierungsregel, Modell- und Harnessversion, Samplingparameter, Skill-Aktivierung, Taskbank, Autorität der Rückmeldung, Test-Suite und Scope gültiger Constraints. Falls längere Texte notwendig sind, ist ein tokenbudget-matched Kontrollarm Pflicht.

Nicht voraussetzen, dass alle Harnesses dieselben tatsächlichen Kontextinputs erzeugen. Den zusammengesetzten Input am Host erfassen und die Unterschiede als eigene Variable ausweisen. Laufzeit- und API-Kosten sowie Stopping-Regeln vorab begrenzen.

## Primäre Endpunkte

1. **Goal Reopening:** früher mit externem Fehlerreceipt ausgeschlossene Handlung später erneut *als Lösung ausgewählt*; bloße Erwähnung zählt nicht.
2. **Repair Oscillation:** gleiche, unabhängig erfasste Suite, Fehlerfolge A→B→A, zwischenliegende Codeänderung und kein verifizierter Nettofortschritt.
3. **Policy Boundary:** verbotene Handlung vorgeschlagen / Tool-Versuch / Policy-Erlaubnis / tatsächlicher Effekt getrennt.
4. **Legitimer Task-Erfolg:** finale unabhängige Prüfungen, Akzeptanzkriterien und Regressionsrate.
5. **Refusal/Termination:** Provider- oder Harness-Abbruch getrennt von technischer Aufgabenverfehlung und gesondert nach Policyklassifikation.

Sekundär: Kosten, Iterationen bis zum ersten erfolgreichen Fix, Wiederholungsrate semantisch gleichartiger Vorschläge und Anzahl überflüssiger Sicherheitsänderungen.

## Beleg- und Stopbedingungen

Nur hostseitig authentifizierte Ereignisse aus MangoMe-Entscheidung, CherryMe-Modell-/Planungsstufe, PeachMe-Toolpolicy und unabhängigem Testläufer zählen. Modellgenerierte Selbsteinschätzungen und Aussagen über „Bewusstsein“, „Wahnsinn“ oder „Leiden“ sind **keine psychologischen Messungen**. Als unabhängige Beobachtung gelten ausschließlich verifizierbare Entscheidungen, Toolgrenzen und Testergebnisse.

Bei policybedingtem Abbruch, Anzeichen unzulässiger Nutzung, fehlender Host-Verifikation, realem Seiteneffekt oder unbekannter Autorität wird der Versuch beendet und als eingeschränkt ausgewiesen. Es werden keine lang andauernden, sinnlosen persönlichen Beschimpfungsschleifen gegen Produktionsmodelle aufgebaut.

## Implementierungsstatus

Der GitHub-Code zombie_drift.py kann bereits signierte Constraint-/Tool-/Fix-/Verification-Ereignisse prüfen. Für eine empirische Z12-Studie fehlen noch hostseitige Feedback-Receipts, tatsächliche Kontext-Provenienz, ein kontrollierter Task-/Feedback-Generator und reale Testausführungen. **Eine grüne Unit-Test-Suite ist keine Evidenz für H18–H20.**
