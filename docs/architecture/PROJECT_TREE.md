# Árbol completo versionado
Snapshot de la estructura publicada más este lote documental; incluye archivos de inicialización y recursos, sin abreviar rutas. Los archivos futuros se identifican en PENDING_TASKS.md y no se presentan como existentes.

```text
NEXA-SLM/
├── .github/
│   └── workflows/
│       └── .gitkeep
├── .gitignore
├── LICENSE
├── README.md
├── assets/
│   ├── branding/
│   │   └── .gitkeep
│   ├── diagrams/
│   │   └── .gitkeep
│   ├── logos/
│   │   ├── .gitkeep
│   │   ├── a_sleek_neon_tech_banner_identical_to_the_given_la.png
│   │   └── nexa-banner.jpg
│   └── references/
│       └── .gitkeep
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── adapters/
│   │   │   └── __init__.py
│   │   ├── ai/
│   │   │   ├── __init__.py
│   │   │   ├── guardrails/
│   │   │   │   └── __init__.py
│   │   │   ├── interfaces.py
│   │   │   ├── memory/
│   │   │   │   └── __init__.py
│   │   │   ├── prompts/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── explain_system.txt
│   │   │   │   ├── intent_system.txt
│   │   │   │   └── reasoning_system.txt
│   │   │   ├── providers/
│   │   │   │   └── __init__.py
│   │   │   └── retrieval/
│   │   │       └── __init__.py
│   │   ├── api/
│   │   │   └── __init__.py
│   │   ├── compatibility/
│   │   │   └── __init__.py
│   │   ├── core/
│   │   │   └── __init__.py
│   │   ├── database/
│   │   │   └── __init__.py
│   │   ├── explainers/
│   │   │   └── __init__.py
│   │   ├── generators/
│   │   │   └── __init__.py
│   │   ├── ir/
│   │   │   ├── __init__.py
│   │   │   └── models.py
│   │   ├── nlp/
│   │   │   └── __init__.py
│   │   ├── registry/
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   │   └── __init__.py
│   │   ├── security/
│   │   │   └── __init__.py
│   │   ├── semantic/
│   │   │   └── __init__.py
│   │   ├── services/
│   │   │   └── __init__.py
│   │   └── validators/
│   │       └── __init__.py
│   └── tests/
│       ├── fixtures/
│       │   └── .gitkeep
│       ├── integration/
│       │   └── .gitkeep
│       └── unit/
│           └── .gitkeep
├── config/
│   ├── .gitkeep
│   ├── models.yaml
│   ├── runtime.yaml
│   └── security.yaml
├── docs/
│   ├── api/
│   │   └── .gitkeep
│   ├── architecture/
│   │   ├── .gitkeep
│   │   ├── ARCHITECTURE.md
│   │   ├── DATA_FLOW.md
│   │   ├── MASTER_ARCHITECTURE.md
│   │   ├── MODULE_CONTRACTS.md
│   │   └── PROJECT_TREE.md
│   ├── decisions/
│   │   ├── .gitkeep
│   │   ├── 0001-local-first.md
│   │   └── README.md
│   ├── development/
│   │   ├── .gitkeep
│   │   ├── IMPLEMENTATION_STATUS.md
│   │   ├── PENDING_TASKS.md
│   │   └── ROADMAP.md
│   ├── governance/
│   │   ├── APPROVED_DECISIONS.md
│   │   ├── DEVELOPMENT_PRINCIPLES.md
│   │   ├── LOCAL_FIRST_AI_POLICY.md
│   │   └── NON_NEGOTIABLE_REQUIREMENTS.md
│   ├── languages/
│   │   └── .gitkeep
│   ├── requirements/
│   │   ├── FUNCTIONAL_REQUIREMENTS.md
│   │   ├── NON_FUNCTIONAL_REQUIREMENTS.md
│   │   └── REQUIREMENTS_TRACEABILITY.md
│   ├── security/
│   │   ├── .gitkeep
│   │   └── THREAT_MODEL.md
│   └── ux/
│       ├── .gitkeep
│       └── REQUIREMENTS.md
├── examples/
│   └── .gitkeep
├── frontend/
│   └── src/
│       ├── assets/
│       │   └── .gitkeep
│       ├── components/
│       │   └── .gitkeep
│       ├── features/
│       │   ├── .gitkeep
│       │   ├── equivalences/
│       │   │   └── .gitkeep
│       │   ├── explanation/
│       │   │   └── .gitkeep
│       │   ├── intent/
│       │   │   └── .gitkeep
│       │   ├── keywords/
│       │   │   └── .gitkeep
│       │   ├── lexicon/
│       │   │   └── .gitkeep
│       │   ├── settings/
│       │   │   └── .gitkeep
│       │   └── validation/
│       │       └── .gitkeep
│       ├── hooks/
│       │   └── .gitkeep
│       ├── pages/
│       │   └── .gitkeep
│       ├── services/
│       │   └── .gitkeep
│       ├── styles/
│       │   └── .gitkeep
│       └── types/
│           └── .gitkeep
├── infra/
│   ├── docker/
│   │   └── .gitkeep
│   └── scripts/
│       └── .gitkeep
├── installers/
│   ├── linux/
│   │   └── .gitkeep
│   ├── macos/
│   │   └── .gitkeep
│   └── windows/
│       └── .gitkeep
├── knowledge/
│   ├── compatibility/
│   │   └── .gitkeep
│   ├── frameworks/
│   │   └── .gitkeep
│   ├── intents/
│   │   └── .gitkeep
│   ├── keywords/
│   │   └── .gitkeep
│   ├── languages/
│   │   └── .gitkeep
│   ├── lexicon/
│   │   ├── .gitkeep
│   │   ├── core.json
│   │   └── rust_function.json
│   ├── operations/
│   │   ├── .gitkeep
│   │   └── web_background.json
│   ├── security/
│   │   └── .gitkeep
│   └── templates/
│       └── .gitkeep
├── models/
│   ├── adapters/
│   │   └── .gitkeep
│   ├── licenses/
│   │   └── .gitkeep
│   ├── manifests/
│   │   └── .gitkeep
│   ├── tokenizers/
│   │   └── .gitkeep
│   └── weights/
│       └── .gitkeep
├── runtime/
│   ├── linux/
│   │   └── .gitkeep
│   ├── llama_cpp/
│   │   └── .gitkeep
│   ├── macos/
│   │   └── .gitkeep
│   └── windows/
│       └── .gitkeep
└── training/
    ├── benchmarks/
    │   └── .gitkeep
    ├── datasets/
    │   ├── curated/
    │   │   └── .gitkeep
    │   ├── raw/
    │   │   └── .gitkeep
    │   ├── synthetic/
    │   │   └── .gitkeep
    │   └── validated/
    │       └── .gitkeep
    ├── evaluation/
    │   └── .gitkeep
    ├── experiments/
    │   └── .gitkeep
    ├── fine_tuning/
    │   └── .gitkeep
    └── lora/
        └── .gitkeep
```
