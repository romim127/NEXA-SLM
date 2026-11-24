# Requisitos funcionales
Todos son objetivos de producto; no se presume implementación.
| ID | Función | Criterio de aceptación |
|---|---|---|
| RF-001 | Entrada libre en español; ejemplos secundarios | Procesa intención libre y ofrece ejemplos sin limitar entrada |
| RF-002 | Palabras clave, sinónimos, acciones, objetos, parámetros, restricciones | Resalta spans originales y normalización |
| RF-003 | Contexto y resolución semántica | Distingue sentidos y dominios; admite intención compuesta |
| RF-004 | Equivalencias multilenguaje | Devuelve implementaciones compatibles y su alcance |
| RF-005 | Lexicon comparativo | Compara palabras reservadas, operadores, símbolos, tipos, estructuras y paradigmas; equivalencia exacta, aproximada o ausente |
| RF-006 | Explicación pedagógica | Explica cada instrucción y token relevante, por qué funciona y diferencias |
| RF-007 | Visualización de código | Resaltado sintáctico y botón copiar por tarjeta |
| RF-008 | Compatibilidad | Clasifica NATIVE, LIBRARY_REQUIRED, FRAMEWORK_REQUIRED, RUNTIME_API_REQUIRED, EXTERNAL_API_REQUIRED, INDIRECT, UNSUPPORTED, UNKNOWN; dependencias y versiones |
| RF-009 | Validación | Estados independientes de sintaxis, semántica y seguridad, incluyendo NOT_RUN; integración futura ScriptGuard |
| RF-010 | SLM local | Modelo propone IR estructurada; catálogo y motor validan; fallback determinista |
| RF-011 | Instalación y ejecución offline | Instalador completo y run local sin llamadas remotas |
| RF-012 | Selección/comparación | Filtros por lenguaje/tecnología, cantidad de resultados compatibles y tarjetas comparables |
| RF-013 | Ambigüedad | Solicita aclaración o muestra alternativas etiquetadas; abstención cuando no sabe |
| RF-014 | Knowledge Base | Catálogos JSON/YAML versionados, fuentes y estado de revisión |
| RF-015 | Dataset propio | Ejemplos curados, validados, sintéticos etiquetados; evaluación independiente |
| RF-016 | Gestión local de modelos | Manifiestos, hash, licencias, detección hardware y perfiles Lite/Standard/Research |
| RF-017 | Persistencia | Historial/preferencias locales opt-in, SQLite inicial; PostgreSQL/Alembic futuro |
| RF-018 | Identidad visual | Infinito y código, contraste legible, nombre oficial, subtítulo y lema |
| RF-019 | Local retrieval | Recuperación del catálogo/lexicon y evidencia para propuestas y explicaciones |
| RF-020 | Extensibilidad | Nuevo lenguaje mediante adaptador y registro sin romper motor existente |

## Cobertura objetivo
Python, JavaScript, TypeScript, C, C++, Rust, Java, Go, C#; HTML, CSS y React; Flask como ejemplo de framework. No afirmar soporte hasta registrar y probar cada operación. Dominios: fundamentos, control de flujo, web, bases de datos, redes, ciberseguridad, archivos, sistemas, bajo nivel, paradigmas.
## Casos de aceptación iniciales
- Cambiar color de fondo web: CSS nativo; JS requiere DOM; React estiliza componente, no necesariamente body; Python/Flask genera HTML/CSS indirectamente; Rust requiere integración web; C/C++ no soportan estilo web directo.
- Centrar elemento: aclarar eje y contenedor; CSS Flexbox, JS DOM, React; explicar precondiciones.
- Botón centrado que cambia color al presionar: distinguir estado temporal CSS :active de persistente mediante eventos/estado.
- Sumar enteros y comprobar paridad: comparar sintaxis y tipos, explicar desbordamiento y diferencias semánticas.
- Rust fn sumar(a: i32, b: i32) -> i32 { a + b }: explicar fn, identificador, parámetros, dos puntos, coma, i32, flecha, llaves, operador y expresión final.
