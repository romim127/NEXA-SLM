# Requisitos no funcionales
| ID | Requisito | Verificación prevista |
|---|---|---|
| RNF-001 | Offline y privacidad por defecto | Instalación completa y prueba con red bloqueada |
| RNF-002 | Seguridad de entradas, IR y plantillas | Pruebas adversariales, límites, allowlist, no eval ni shell |
| RNF-003 | Integridad de distribución | Hash y procedencia del modelo/runtime, licencias y manifiestos |
| RNF-004 | Rendimiento y memoria acotados | Benchmark por perfil y hardware; umbrales pendientes |
| RNF-005 | Modularidad | Pruebas de contratos y regresión al añadir adaptadores |
| RNF-006 | Reproducibilidad | Dependencias fijadas, versiones de catálogos, CI y entornos |
| RNF-007 | Accesibilidad | Teclado, contraste, lectura de etiquetas, foco visible |
| RNF-008 | Trazabilidad | Requisito → módulo → prueba → evidencia → commit |
| RNF-009 | Portabilidad | Windows/Linux primero, macOS posterior; pruebas por plataforma |
| RNF-010 | Transparencia | Mostrar modelo, modo, fuentes, estado de validación, límites y errores |
| RNF-011 | Resiliencia | Fallback determinista ante ausencia de modelo, timeout o salida inválida |
| RNF-012 | Aislamiento | Loopback y orígenes explícitos; compiladores aislados sin red ni acceso a archivos personales |
