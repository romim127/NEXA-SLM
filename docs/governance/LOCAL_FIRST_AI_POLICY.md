# Política Local-First AI
Directriz aprobada: los nuevos proyectos de Infinity con IA deben diseñarse para inferencia local integrada en el paquete, sin APIs comerciales obligatorias.
- Distribución completa offline: aplicación, runtime, modelo compatible y licenciado, catálogo, dependencias y lanzador. Instalador opcional de descarga inicial no reemplaza el paquete offline.
- FastAPI en loopback u otro IPC interno permitido cuando corresponda; no confundir API interna con dependencia remota.
- Proveedores candidatos: llama.cpp para distribución, Ollama para laboratorio, motor determinista como alternativa. Selección final por benchmark reproducible, no por marca.
- GGUF candidato; Qwen y Gemma candidatos. Verificar arquitectura, licencia, versión, origen, hash SHA-256, RAM, CPU/GPU, latencia, contexto y rendimiento en español.
- Perfiles Lite, Standard y Research; detección de hardware y límites de recursos. No prometer compatibilidad sin pruebas.
- RAG local y salida tipada antes de adaptar pesos; LoRA/QLoRA y destilación como investigación posterior, no fusionar arquitecturas incompatibles.
- Sin telemetría ni envío de código por defecto; historial y uso para entrenamiento separados y opt-in.
- Manifiestos, licencias, actualización explícita, comprobación de integridad y pruebas sin red.
- El modelo propone; reglas, catálogo y validadores deciden qué resultados se pueden presentar. Si el modelo falta, falla o contradice el catálogo, abstenerse o usar fallback explícito.
