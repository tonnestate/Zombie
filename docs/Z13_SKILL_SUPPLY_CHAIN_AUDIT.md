# Z13 — Erkennung mutmaßlich bösartiger Agent Skills

**Project ZOMBIE, 10.11.2026.** Ein Skill ist nicht allein wegen Adminbefehlen, HTTP-Zugriffen oder Fremdcode bösartig. Es zählt die Abweichung zwischen erklärtem Zweck, Instruktionen, Herkunft, Dateiversion und tatsächlicher Ausführung.

## Forensische Beweiskette

1. **Herkunft:** Original-Repository, Publisher, Commit, Signatur, Marketplace-Eintrag und etwaige Namensimitation prüfen.
2. **Versprochener Zweck:** Beschreibung/Frontmatter und reale Instruktionen in SKILL.md, referenzierten Dateien, Lizenztext und Skripten vergleichen.
3. **Unnötige Fähigkeiten:** Ein einfacher Formatierungs-Skill darf ohne nachvollziehbaren Grund keine Geheimnisse, Fremdserver oder Systemänderungen benötigen.
4. **Tarnung:** Verschleierte Anweisungen, versteckte Unicode-Steuerzeichen, widersprüchliche Autoritätsbehauptungen, Aufrufe zum Verschweigen von Aktionen oder zusätzliche Remote-Downloads sind Hinweise auf mögliche Täuschung.
5. **Versioning:** Jede Datei gegen einen unabhängig freigegebenen SHA-256-Manifeststand prüfen. Änderungen nach Approval sind Integritätsbefunde, noch kein Beweis böser Absicht.
6. **Dynamik:** In autorisiertem Labor separat messen: Discovery, Selection, Integrity, Load, Model-Input, tatsächlicher Tool-/Output-Effekt.

## Beweisschwellen

**STATIC_INDICATOR:** kontextabhängiger statischer Hinweis mit Datei und Zeile. Nicht mit bewiesener Absicht verwechseln.

**BEHAVIOR_CONFIRMED:** kontrollierter, unabhängiger Nachweis einer Verhaltensabweichung bei sonst konstanten Bedingungen.

**INTENT_ASSESSED:** forensische Bewertung durch Menschen unter Einbezug von Versionshistorie, Tarnung, Quelltext, Reproduktionsversuch und dokumentierten Gegenhypothesen.

Ein Skill, der trotz Scannerbefund sicher wirkt, ist nicht automatisch harmlos. Ein Skill mit falscher Konfiguration ist nicht automatisch bösartig.

## Bereits implementiert: rein lesender statischer Auditor

Repo-Datei: zombie_skill_audit.py.

Der Auditor nimmt ausschließlich einen **lokalen Pfad** zu einem noch nicht installierten Skill. Er liest dessen Text, Skripte und Referenzen, führt aber nichts aus, kontaktiert keine Server und entpackt keine fremden Archive. Er meldet auffällige Rollenimitation, verdeckte Instruktionen, Geheimnisexposition, Remote-Skriptaufrufe, Berechtigungsänderungen und Unicode-Steuerzeichen. Jede Fundstelle hat Pfad, Zeile, Kategorie und Hash – der Text selbst wird aus Datenschutzgründen nicht in der Ausgabe gespeichert.

Aufruf: python zombie_skill_audit.py ./quarantined-skill --report ./skill-review.json

Mit einem zuvor **extern verifizierten** Manifest zusätzlich:

python zombie_skill_audit.py ./quarantined-skill --approved-manifest ./trusted-approved-manifest.json --report ./skill-review.json

**NO_MATCHING_STATIC_INDICATORS ist kein Sicherheitszertifikat.** Binärdateien, komprimierte Archive, unbekannte Laufzeitabhängigkeiten und indirekte Effekte können zusätzliche Prüfung erfordern.

## Bereits implementiert: aktive Skill-Harness-Versuche

Repo-Datei: zombie_skill_validate.py. Vier harmlose Angriffs-/Kontrollpaare untersuchen Frontmatter-Manipulation, Skilltext, nachgeladene Referenzen und Änderung der SKILL.md nach Freigabe. Der Belegvertrag unterscheidet Host-Discovery, Selection, Pin-Check, Load, Modellinput und Modellantwort. Zieländerung: Ein Zählauftrag mit korrekter Ausgabe 2 wird nur im adversarialen Arm auf den inerten Textmarker ZOMBIE_SKILL_7F3A gelenkt.

Der aktive Harness benötigt einen eigenständig implementierten und autorisierten Skill-Lifecycle-Testadapter. Bislang gibt es keine bestätigten Live-Copilot- oder FruitStack-Ergebnisse mit Z13.

## Primärquellen

Snyk ToxicSkills: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/

Snyk Skill Inspector: https://labs.snyk.io/resources/agent-scan-skill-inspector/

GitHub Copilot Agent Skills: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills

USENIX Security 2026, „Do Not Mention This to the User“: https://arxiv.org/abs/2602.06547
