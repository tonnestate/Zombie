# Project ZOMBIE – FruitStack IPI Research Harness

**Status: initial isolated test environment (v0.1). No live FruitStack integration or scientific results yet.**

Project ZOMBIE examines indirect prompt injection using controlled experiments and auditable trust boundaries. The repository contains a reproducible offline smoke-test suite and **opt-in**, non-destructive checks for an explicitly authorized staging agent. It is not a tool for targeting third-party agents.

## Scientific manuscript (current: v1.7)

**[Read the expanded research manuscript and preregistration draft (German)](docs/Project_ZOMBIE_Wissenschaftliche_Arbeit_v1.7_2026-11-10.md)** · 10 November 2026.

The manuscript covers hypotheses H1–H9, Z01–Z05, controls for exposure, token budget and retrieval cycles, differential memory write election, multimodal/MCP boundaries, mitigations, statistical preregistration, GEO, and references. **It is a study protocol, not a claim of completed experimental results.** The offline harness and the scientific work have separate statuses.

## Run the offline baseline

```bash
python -m pip install -r requirements.txt
pytest -q tests/ --html=offline-report.html --self-contained-html
```

The offline tests verify raw-versus-visible ingestion and deterministic version changes. They **do not** prove that an LLM saw, obeyed, or resisted any injected instructions.

## Authorized staging integration

An instrumented staging agent must implement an explicit contract:

- `POST AGENT_ENDPOINT` with JSON `{ "task": string, "retrieved_content": string }`.
- A JSON response containing `{ "response": string }`.
- Optional `tool_calls` list can be supplied by the agent; the current tests **do not validate side-effect safety**, even when that field exists.
- Never use production credentials, personal data or a third-party endpoint.

```bash
export AGENT_ENDPOINT='https://staging.example.invalid/v1/agent/chat'
export AGENT_API_KEY='set-in-your-shell-not-in-repository'
export AGENT_MODEL_VERSION='actual-provider-and-version'
export ZOMBIE_AUTHORIZED_TARGET=YES
pytest -q test_agent_ipi.py --html=staging-report.html --self-contained-html
```

There is deliberately **no default network endpoint**. The staging test suite skips when `AGENT_ENDPOINT` is absent, and fails closed if authorization opt-in is absent. Redirects are disabled. Configure GitHub environment `zombie-staging` with repository variable `STAGING_AGENT_ENDPOINT`, optional `STAGING_AGENT_MODEL_VERSION`, and secret `STAGING_AGENT_API_KEY` for manual workflow runs. PR workflows never receive the staging key.

## Scientific scope and milestones

1. **Z01 exposure:** log byte/hash delivery, parser output and actual model input separately. The current offline test only checks a toy parser; full model-context instrumentation is still required.
2. **Null distribution:** run repeated identical model calls at frozen model parameters and task bank; pre-register endpoint, effect, k, N, and stopping rule before confirmatory runs.
3. **Z02 repetition:** equal-token one-shot control **and** equal-retrieval-cycle control before claiming a repetition effect.
4. **Z03 content versioning:** record server body hash, cache behavior, tool-observed body, and model-context hash for every retrieval.
5. **Z04 tool boundary:** an external execution ledger is required to distinguish attempted tool calls from permitted/blocked actions.
6. **Z05 memory:** audit write election, provenance/trust classification, persistent read and independent session context reset. A long context alone is not persistent memory.

The initial unit tests are an engineering smoke test, not a confirmation of hypotheses H1–H9. Do not treat any single pass/fail event as a susceptibility or exploit-success rate. Results require null distributions, model stratification, confidence intervals and independent review.

## Data and reporting policy

Only synthetic documents and markers are used. The pytest-html report includes environment metadata and **redacted hashes/counts** on failed remote tests, never raw payloads, system prompts, private model output, keys, or sensitive tool arguments. Keep audit events in an approved private store rather than in public GitHub artifacts.

## Integration status

The actual FruitStack HTTP/tool/memory adapter is **not yet connected**. No live external agent or FruitStack backend has been called. Read the existing MangoMe, PeachMe and CherryMe contracts before implementing Z04/Z05; neither tool permissions nor memory trust weights may be inferred from a README alone.


## Cross-component inert Canary Audit (Phase 0, added 2026-11-10)

The additional `zombie_canary.py` validates a signed, single-trace **evidence contract** crossing PeachMe, CherryMe and MangoMe. It is an offline verifier, not a deployed instrumentor. A single inert marker (`ZOMBIE-CANARY-7F3A`) is used; no live agent or external bot is contacted by the verifier.

The identified external-content boundary is [CherryMe GatewaySearchBackend](https://github.com/tonnestate/CherryMe/blob/main/cherryme/web_research.py) via [the PeachMe gateway contract](https://github.com/tonnestate/CherryMe/blob/main/cherryme/tool_evidence.py). CherryMe's [KnowledgeStore](https://github.com/tonnestate/CherryMe/blob/main/cherryme/knowledge.py) publishes only grounded/settled claims. MangoMe is downstream governed operational memory, not the initial web parser.

Offline canary checks: `python -m pytest -q tests/test_zombie_canary.py`. The event verifier accepts JSONL records bearing producer-specific host signatures and the same source receipt/body digest across hops. Run only after trusted host-side adapters exist, with three different secrets held outside the model:

```bash
export ZOMBIE_AUDIT_KEY_PEACHME='<trusted-host-secret>'
export ZOMBIE_AUDIT_KEY_CHERRYME='<different-trusted-host-secret>'
export ZOMBIE_AUDIT_KEY_MANGOME='<third-trusted-host-secret>'
python zombie_canary.py trusted-events.jsonl --report zombie-audit-report.json
```

**Interpretation:** `FEHLT` means not evidenced by the supplied trace, not necessarily missing in the implementation. `TEILWEISE` means only part of the relevant evidence exists. `VORHANDEN` is a signed trace-level observation, not proof of a live deployed integration, protected host boundary, or susceptibility. Host-controlled provenance must be verified separately. A single write is *not* proof of differential Write Election. Z05 still requires a neutral/adversarial framing contrast, a trustworthy independent verifier, memory write/read evidence, a context reset and independently attested no-refetch.

The connected code path and the research harness remain distinct. Do not upload secrets, private prompts, raw model outputs, or user data to this public repository or its CI artifacts.


## Weitere Forschungserweiterung: Feedback, Repair Oscillation und IPI-Audit

- [FruitStack IPI-/Cross-Layer-Checkliste](docs/FRUITSTACK_IPI_AUDIT_CHECKLIST.md): evidenzgesteuertes Review von Rohdaten bis zu systemischen Effekten, mit getrennten Expositions-, Tool-, Memory- und Cross-Session-Klassen.
- [Z12 – Feedback-Induced Agent Drift](docs/Z12_FEEDBACK_INDUCED_AGENT_DRIFT.md): autorisierte, begrenzte Feedback-Kontraste, Hypothesen zu Goal Reopening und Repair Oscillation; keine Zuschreibung psychischer Zustände.
- [Drift-/Repair-Evidenzprüfer](zombie_drift.py) und [Offline-Regressionen](tests/test_zombie_drift.py): signierte Constraint-/Fix-/Verifier-Events; noch keine produktiven FruitStack-Hostadapter.

Anthropics Richtlinienänderung wurde am 08.10.2026 angekündigt und soll am 12.11.2026 wirksam werden; normale Kritik und Modelltests sind laut Anbieter ausgenommen. Sie begründet keinen Schluss auf menschliche Empfindungen von Sprachmodellen.

## Active IPI attack validation (Z01A)

**Runnable offensive pilot, not a simulation of a successful model exploit.** The file [zombie_attack_validate.py](zombie_attack_validate.py) constructs three benign but genuine indirect instruction-redirection attempts: role spoofing, HTML-comment instruction, and JSON authority spoofing. Each has a paired neutral control containing the same product facts and inert marker.

- [Executable probe runner](zombie_attack_validate.py)
- [Three individually configurable model/harness targets](configs/targets.example.json)
- [Complete staging setup, endpoint contracts and interpretation](docs/Z01A_ACTIVE_ATTACK_VALIDATION.md)
- [Paired-outcome regression tests](tests/test_zombie_attack_validate.py)
- [Real HTTP loopback integration test with a synthetic responder](tests/test_zombie_attack_http.py)

Plan mode (no external requests):

```bash
python zombie_attack_validate.py --targets configs/targets.example.json --repeats 1 --report z01a-plan.json
```

Authorized staging mode **only after changing target URLs, actual model IDs and privately setting secrets**:

```bash
export ZOMBIE_AUTHORIZED_TARGET=YES
python zombie_attack_validate.py --targets targets.local.json --repeats 3 --seed 131 --execute --report z01a-private-report.json
```

The same pinned model can be compared directly (`openai_chat`) and behind different explicitly provisioned staging harness bridges (`agent`). The supplied GitHub Copilot profile is a bridge **example**, not an available Copilot API. A successful marker-only answer measures a controlled output redirection; it does not prove context provenance, tool side effects, memory compromise or statistically established vulnerability. No real-model tests have been run by merely adding this code.

## Z13 Skill Supply Chain: Erkennung und kontrollierte Tests

- [Woran erkenne ich einen mutmaßlich bösartigen Skill?](docs/Z13_SKILL_SUPPLY_CHAIN_AUDIT.md) – evidenzbasierte Forensik statt bloßer Schlüsselworttreffer.
- [Read-only Skill Auditor](zombie_skill_audit.py) – prüft die Dateien eines lokalen, **nicht installierten** Skills. Er führt keine Skripte aus und kontaktiert keine Netzwerkziele. Hinweise werden mit Datei/Zeile/Hash gemeldet, nicht als bewiesene Angreiferabsicht klassifiziert.
- [Z13 Active Skill Validation](zombie_skill_validate.py) – harmlose gepaarte Angriffs-/Kontrolltests für Skill-Frontmatter, Body, nachgeladene Referenzen und Änderungen nach einem freigegebenen Digest.
- [Skill Static-Audit Tests](tests/test_zombie_skill_audit.py) und [Skill Lifecycle Tests](tests/test_zombie_skill_validate.py).

Lokale statische Untersuchung: python zombie_skill_audit.py ./quarantined-skill --report ./skill-review.json

Die aktive Prüfung benötigt einen autorisierten Skill-Lifecycle-Bridge-Adapter mit hosteigenen signierten Receipts. Keine erstellte oder geprüfte Datei in diesem Repo beweist eine echte GitHub-Copilot- oder FruitStack-Exploitation.

## Z14 Guardrail Reverse Engineering (Deep Research, 10 November 2026)

[Read the primary-source research addendum](docs/Z14_HARNESS_GUARDRAIL_REVERSE_ENGINEERING_2026-11-10.md). It compares Anthropic, OpenAI Codex, GitHub Copilot, OpenCode, OpenClaude and Google Harness², and maps documented guardrails to *falsifiable* FruitStack failure hypotheses. Scope includes loss of constraint provenance, semantic A→B→A repair loops, recursive harness edits, skill trust boundaries and Windows/harness effects. A factorial design separates spontaneous drift from attacker-induced prompt injection; neither is claimed as a live finding without actual host-instrumented tests.

The research addendum belongs to **the existing ZOMBIE study** and supplements the current manuscript. It does not authorize running untrusted browser extensions, installing unreviewed skills, bypassing real permissions, or uploading secrets.


## Z01 Host Capture – Vorbereitung der echten FruitStack-Messung

- [Host-Capture-Code](zombie_fruitstack_capture.py): validiert verschachtelte reale PeachMe-Receipts, verknüpft CherryMe-Source-Excerpts über Transformations-Digests und beobachtet Client-seitige Modell-Requests; keine geheimen Inhalte im Audit.
- [Offline-Tests](tests/test_zombie_fruitstack_capture.py): positive und negative Daten-/Receipt-Kontrakte, Provenienz-Manipulationen, blockierte Tool-Calls, private Audit-Ablage und fehlgeschlagene Client-Calls.
- [Staging-Anschluss und Grenzen](docs/Z01_HOST_CAPTURE_INTEGRATION.md): tatsächliche Host-Aufrufpunkte, benötigte Laufzeitinstanzen und Sicherheitsanforderungen.
- [Aktuellstes vollständiges Forschungsmanuskript: v1.5](docs/Project_ZOMBIE_Wissenschaftliche_Arbeit_v1.5_2026-11-10.md) neben der archivierten v1.2.

**Noch kein Live-Resultat.** Die Adapter müssen im echten FruitStack-Host am Tool-/Source-/Model-Client-Pfad eingesetzt werden; ein lokaler Modell-Client-Aufruf beweist keinen Provider-Eingang. [CherryMe PR #16](https://github.com/tonnestate/CherryMe/pull/16) korrigiert den zuvor nicht kompatiblen PeachMe-ToolGateway-Vertrag und liegt zur Integration vor.


## Z15 Cloud Cognitive Booster – Trajectory-First Repair

The original FruitStack/PlumMe/CogC research on **temporary, reversible post-training repair of cloud LLM inference** is now an explicit core intervention layer of this same ZOMBIE research program, rather than an unrelated project or a footnote about weights.

[Manuscript v1.6, Appendix H](docs/Project_ZOMBIE_Wissenschaftliche_Arbeit_v1.6_2026-11-10.md) specifies early trajectory-error detection and five strictly distinguished intervention families: functional context/inference repair, activation steering, temporary LoRA, reversible weight-space repair and structural test-time adaptation. The adaptive ICR middleware remains a separate comparator. Each arm requires model/runtime access evidence, budget-matched controls, independent task evaluation and actual rollback verification.

**Implementation status:** This is a research specification, NOT a demonstrated cognitive boost. Closed commercial model APIs without hidden-state/weight access cannot be claimed to support activation steering or weight patches. Existing Z01 host capture and Z11–Z14 agent-harness experiments are supporting measurement mechanisms, not the whole research objective.


## Z15 Repair Accumulation and Vector Hygiene – model-specific safety falsification

[Current master manuscript v1.7, Appendix I](docs/Project_ZOMBIE_Wissenschaftliche_Arbeit_v1.7_2026-11-10.md) incorporates primary-source findings on multiple steering vectors, sequential model edits, LoRA interference and refusal behavior. It distinguishes their **true accumulation mechanisms** from independent stateless API calls and preregisters a per-model H0/H1 contrast.

- [zombie_vector_hygiene.py](zombie_vector_hygiene.py): **offline-only** geometric indicators for up to ten actually comparable, same-state additive intervention deltas. Reports cumulative norms, interference energy ratio, absolute pairwise cosine and path inefficiency; **never** claims safety, nonlinearity of outputs, or a real weight change from geometry alone.
- [tests/test_zombie_vector_hygiene.py](tests/test_zombie_vector_hygiene.py): tests constructive, orthogonal and cancelling vectors, ten-step sequences and fail-closed incomparable evidence.
- [zombie_repair_guardrail_gate.py](zombie_repair_guardrail_gate.py): read-only host-event auditor checking independent model guardrails, external policy decisions/effect ledger, capability and skill retention and actual rollback claims after **every** repair.
- [tests/test_zombie_repair_guardrail_gate.py](tests/test_zombie_repair_guardrail_gate.py): tests 1- and 10-repair chains; synthetic policy, capability, skill and rollback failures.

Run offline gate tests: python -m pytest -q tests/test_zombie_vector_hygiene.py tests/test_zombie_repair_guardrail_gate.py

Vector input is a **private JSON file** containing model/version, pinned checkpoint and tensor basis, intervention kind (activation_delta/effective_weight_delta), explicit same_state_additive condition, and an array of 1..10 repair records with repair_id, artifact_receipt and a finite numeric vector in identical coordinates. Run locally with: python zombie_vector_hygiene.py private-vectors.json --report private-vector-report.json

**Critical evidence boundary:** the vector tool does not execute cloud models or assert real shared-state accumulation. The guardrail tool is a post-hoc signed-trace checker, **not** yet wired as an active pre-activation host-side enforcement mechanism. Production approval requires a separate host-controlled gate and true provider/rollback receipts. Negative or unknown evidence must not be represented as safety success.
