# Flujo de datos
```mermaid
flowchart TD
 U[Entrada humana] --> A[API interna]
 A --> N[NLP y keywords]
 A --> R[Retrieval local]
 K[Knowledge Base] --> R
 R --> L[SLM local]
 L --> G[Guardrails]
 N --> S[Semantic Core]
 G --> S
 K --> S
 S --> Q{Ambigüedad o desconocido}
 Q -->|Sí| C[Aclarar o abstenerse]
 Q -->|No| I[Universal IR tipada]
 I --> M[Registry y Compatibility]
 K --> M
 M -->|Compatible| T[Adaptadores y generación]
 M -->|No soportado o desconocido| D[Explicar limitación]
 T --> V[Validación sintáctica y semántica]
 V --> X[Auditoría estática]
 X --> E[Explain Engine]
 K --> E
 E --> O[Respuesta UI]
 C --> O
 D --> O
 O --> H[Historial opt-in]
```
La inferencia no tiene acceso a shell ni red obligatoria. La base de conocimiento aporta evidencia, no instrucciones ejecutables. El motor determinista puede resolver sin SLM. Cada etapa conserva identificador de petición, versión de catálogo/modelo y estado de error; historial no guarda datos por defecto. Las comparaciones mantienen alcance y dependencias por tecnología.
