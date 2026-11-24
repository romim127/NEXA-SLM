# Contratos de módulos
Contratos de diseño, pendientes de implementación y pruebas.
| Ruta | Entrada | Salida / responsabilidad |
|---|---|---|
| backend/app/api | Texto y opciones | Respuesta tipada, errores, límites y loopback |
| backend/app/core | Configuración | Config validada, rutas y límites |
| backend/app/schemas | Datos externos | Esquemas tipados y validación |
| backend/app/nlp | Texto | Keywords, spans, acciones, objetos, restricciones |
| backend/app/ai | Texto + evidencia | Propuesta IR no confiable; estado de proveedor |
| backend/app/ai/providers | Petición acotada | Propuesta estructurada o error/fallback |
| backend/app/ai/prompts | Contexto validado | Instrucciones versionadas |
| backend/app/ai/retrieval | Conceptos | Entradas del catálogo con procedencia |
| backend/app/ai/memory | Preferencias autorizadas | Contexto local opt-in |
| backend/app/ai/guardrails | Salida del modelo | Validación estructural, límites y rechazo |
| backend/app/semantic | NLP + propuesta + catálogo | Intención resuelta o aclaración |
| backend/app/ir | Intención | IR independiente del lenguaje |
| backend/app/registry | Catálogos | Lenguajes, versiones, tecnologías, capacidades |
| backend/app/compatibility | IR + registry | Clasificación, alcance, dependencias y razones |
| backend/app/adapters | IR + capacidad | Representación específica por lenguaje |
| backend/app/generators | Adaptación + plantilla | Código textual; nunca ejecución |
| backend/app/validators | Código + contexto | Sintaxis y semántica separadas, evidencia |
| backend/app/security | Código + IR | Hallazgos estáticos, gravedad y límites |
| backend/app/explainers | Código + lexicon | Tokens, explicaciones, diferencias, dependencias |
| backend/app/database | Datos opt-in | Persistencia local |
| backend/app/services | Petición | Orquestación, timeout, trazabilidad |
| frontend/src/features/intent | Entrada usuario | Petición y aclaraciones |
| frontend/src/features/keywords | Spans | Resaltado |
| frontend/src/features/equivalences | Resultados | Filtros, tarjetas, copiar |
| frontend/src/features/lexicon | Conceptos | Comparación |
| frontend/src/features/explanation | Tokens | Explicación interactiva |
| frontend/src/features/validation | Estados | Evidencia y límites visibles |
| frontend/src/features/settings | Preferencias | Modelo, modo y privacidad |
| knowledge | Entradas revisadas | Catálogo versionado y fuentes |
| models/runtime/installers | Manifiestos y binarios | Distribución verificada y local |
| training | Ejemplos autorizados | Dataset, evaluación y adaptadores de modelo |
## Universal IR
Campos objetivo: schema_version, operation_id, domain, keywords/spans, parameters tipados, constraints, target, environment, ambiguities, evidence. El contrato dataclass actual es preliminar.
## Resultado
Por implementación: lenguaje, tecnología, versión/entorno, compatibilidad, dependencias, alcance, snippet, explicación por token, referencias, estados de sintaxis/semántica/seguridad y errores. UNKNOWN y UNSUPPORTED no deben producir código inventado. NOT_RUN nunca equivale a PASS.
