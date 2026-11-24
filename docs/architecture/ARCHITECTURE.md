# NEXA Semantic-Code / NEXA-SLM
Status: foundation, not a working implementation.

```mermaid
flowchart TD
 UI[React + TypeScript] --> API[FastAPI loopback]
 API --> NLP[Keyword Engine]
 API --> SLM[Local SLM optional]
 NLP --> CORE[Semantic Core]
 SLM --> CORE
 KB[Versioned Knowledge Base] --> CORE
 CORE --> IR[Typed Universal IR]
 IR --> COMP[Compatibility Engine]
 KB --> COMP
 COMP --> GEN[Language Adapters and Syntax Engine]
 GEN --> VAL[Syntax Semantic Security Validation]
 VAL --> EX[Explain Engine]
 KB --> EX
 EX --> UI
```

Modular Python monolith; optional llama.cpp production runtime, Ollama research provider, deterministic fallback. Local retrieval, schema-constrained output, no cloud dependency. SQLite history opt-in; PostgreSQL and Alembic later. Rust adapters optional. Model selection is pending benchmarks; no weights included. No generated code executed automatically. Validation must expose separate syntax, behavior and security statuses, including NOT_RUN. Unknown intent or compatibility must abstain. Ambiguous intent must request clarification or present explicitly labeled alternatives.
