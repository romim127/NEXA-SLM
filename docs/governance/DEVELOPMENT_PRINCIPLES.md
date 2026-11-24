# NextGenAI Infinity — principios de ingeniería
Estado: directrices ratificadas en conversación del 24 de noviembre de 2026.

1. Complete by design: documentar la arquitectura, árbol sin abreviar, requisitos, contratos, dependencias y decisiones desde el minuto cero.
2. Implementación incremental: diseñar completo no equivale a implementar todo en una versión. Nunca presentar scaffolding como funcional.
3. Local intelligence: inferencia integrada, sin dependencia obligatoria de servicios externos.
4. Knowledge ownership: catálogo, reglas y datasets versionados propios; respetar licencias y procedencia.
5. Security by design: validar entradas y salidas; no ejecutar código generado automáticamente.
6. No silent changes: no eliminar, renombrar, simplificar ni sustituir módulos sin aprobación explícita; silencio no constituye aprobación.
7. Traceable evolution: registrar cambios, pruebas, commit, rama y estado real; comprobar árbol remoto tras publicar.
8. Human control: AI assists. Human verifies. Human decides.
9. No knowledge loss: convertir cada idea aceptada en requisito trazable antes de implementar; repositorio como fuente de verdad independiente de chats.
10. Conservar regresiones cubiertas y funcionalidades previas. Cada lote debe indicar alcance, archivos, pruebas, limitaciones y decisiones pendientes.

Aplicación a futuros repositorios: copiar/adaptar esta política al iniciar cada proyecto; no afirmar que ya se instaló en otros repositorios.
