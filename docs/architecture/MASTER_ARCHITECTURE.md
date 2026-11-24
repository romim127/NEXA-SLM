# NEXA-SLM — Semantic Intelligence Model
*Specialized Programming Intent Reasoning*

Documento maestro v0.1.0. Arquitectura objetivo, no afirmación de implementación.
## Alcance
Herramienta de ayuda al desarrollador, no IDE ni traductor mecánico de código. Interpretar intención humana, detectar conceptos y mostrar implementaciones compatibles explicadas. Base de conocimiento propia, IA local opcional en ejecución pero incluida en distribución completa.
## Capas
- Presentación: React/TypeScript/Vite; entrada, keywords, equivalencias, lexicon, explicación, validación, settings.
- API interna: FastAPI loopback; contratos Pydantic previstos; servicios de orquestación.
- NLP: reglas léxicas, sinónimos, contexto; spaCy candidato posterior.
- IA: proveedor determinista, llama.cpp candidato de producción, Ollama laboratorio; prompts, retrieval, guardrails, memoria opt-in, gestión de modelo y hardware.
- Semantic Core y Universal IR: operaciones, parámetros, restricciones, contexto, ambigüedad y evidencia.
- Registry y Compatibility: lenguaje/versión/entorno/dependencias; capacidades registradas.
- Syntax Engine: adaptadores y generadores Python inicialmente, Rust futuro; plantillas validadas.
- Validation y Security: AST, parsers, Tree-sitter y compiladores aislados candidatos; ScriptGuard futuro.
- Explain Engine: conocimiento versionado, explicación por token, diferencias y alcance.
- Persistencia: SQLite inicial, PostgreSQL/Alembic futuro.
- Distribución: modelos, runtime, manifiestos, licencias, instaladores y lanzadores; Windows/Linux primero.
- Investigación: datasets raw/curated/validated/synthetic, evaluación, benchmarks, fine-tuning, LoRA y experimentos.
- Infraestructura: Docker opcional, CI GitHub Actions, pytest/Vitest propuestos.
## Referencias normativas
[Árbol completo](PROJECT_TREE.md) · [Contratos](MODULE_CONTRACTS.md) · [Flujo](DATA_FLOW.md) · [Requisitos funcionales](../requirements/FUNCTIONAL_REQUIREMENTS.md) · [Política local](../governance/LOCAL_FIRST_AI_POLICY.md) · [Seguridad](../security/THREAT_MODEL.md).
## Decisiones abiertas
Versiones exactas de stack, modelo y cuantización, licencias, perfiles RAM y latencia, esquema IR definitivo, interfaz de ScriptGuard y mecanismo de aislamiento. No son aprobaciones implícitas.
