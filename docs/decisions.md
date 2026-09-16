# Decisions

Registro breve de decisiones de síntesis y desarrollo.

## 2026-09-15 — physical-state-interface
- **Decisión:** promover como núcleo activo una interfaz de estado físico y llevarla a M3 mediante un sustituto digital mínimo.
- **Evidencia:** `f1-20260915-2101`, `f1-20260915-2103`, `f3-20260915-21-passive-crack`, `f3-20260915-21-passive-rf-temp`.
- **Alternativa rechazada como núcleo:** `f1-20260915-2102` + `f3-20260915-21-event-vision`; convergencia fuerte en procesamiento temporal, pero exige hardware especializado y no existe integración directa demostrada.
- **Razón:** la ruta elegida tiene dos pares independientes de evidencia: transducción física pasiva y estado/cómputo multestable, además de un criterio de éxito simulable antes de hardware.
- **Consecuencia:** se crean `src/physical_state.py` y `tests/test_physical_state.py`; el prototipo es M3 pero permanece `created_not_executed`, por lo que no asciende a M4.
- **Descartado por ahora:** Aérotrain queda archivado por falta de convergencia funcional; Video 2000/DTF y Setun se conservan como precedentes de control/representación, no como prueba de integración.

## 2026-09-15 — event-powered state extension
- **Decisión:** extender `physical-state-interface` con una ruta evento físico -> energía de pulso -> cambio de estado persistente; mantener M3.
- **Evidencia:** `f3-20260915-22-wiegand-counter` demuestra hasta 130 nJ/pulso y un contador experimental operando con 38 nJ; `f1-20260915-2103` demuestra FSM física; `f1-20260915-22-light-programmable-mechanical-logic` demuestra lógica física reconfigurable.
- **Alternativa considerada:** activar observabilidad no-contacto por stray-flux/speckle. Se mantiene en espera porque aporta lectura rica pero requiere adquisición/procesamiento continuo y cambia menos la arquitectura central.
- **Razón:** Wiegand aporta una cadena medida de transducción + energía + registro de evento, cerrando una debilidad del prototipo anterior: el origen físico del símbolo discreto.
- **Consecuencia:** se crean `src/event_state.py` y `tests/test_event_state.py`; no se declara M4 porque los tests aún no fueron ejecutados y el modelo energético es contractual, no una simulación eléctrica.
- **Nueva línea activa M1:** `embodied-wave-computation`; la evidencia de computación mecánica reprogramable es fuerte, pero todavía falta una especificación cuantitativa única para M2.
- **Archivado:** Cybersyn/Minitel se conservan como precedentes históricos pero no se fuerzan dentro del núcleo; magnetic bubble memory queda como precedente de estado físico, no como tecnología elegida.

## 2026-09-16 — embodied-dynamics-computation
- **Decisión:** ampliar `embodied-wave-computation` a `embodied-dynamics-computation`, mantenerlo en M1 y no construir todavía un benchmark.
- **Evidencia:** `f1-20260916T00-mycelium-reservoir` y `f1-20260916T00-active-colloid-reservoir` demuestran reservoir computing mediante dinámica material/colectiva; se suman a `f1-20260915-22-wave-metamaterial-robot` sin asumir equivalencia entre mecanismos.
- **Alternativa rechazada:** promover directamente a M2/M3 por acumulación de ejemplos. Se rechaza porque los reservorios temporales y los operadores ondulatorios no comparten todavía una tarea y métrica única.
- **Razón:** la convergencia funcional aumentó, pero la evidencia contradictoria también importa: el reservorio coloidal depende de láser, microscopía y feedback digital, y el micelio presenta variabilidad entre dispositivos.
- **Consecuencia:** se eleva confianza de la línea a 0.73, se redefine su criterio de éxito y se exige una tarea común medible antes de promoción.
- **Otras decisiones:** clamp-on ultrasonic se incorpora a observabilidad legacy en espera, no activa, por fuerte dependencia de instalación y desviaciones de campo reportadas hasta 43%; Nordsieck/MADDIDA se archivan como precedente coherente de integración física→digital especializada; Pantelegraph se archiva por falta de traducción funcional al núcleo.

## 2026-09-16 — material-state extension, cycle 02
- **Decisión:** fusionar memoria molecular fotónica y memoria higromecánica persistente dentro de `physical-state-interface`; no abrir un tercer módulo.
- **Evidencia:** `f1-20260916-02-lc-photonic-memory`, `f3-20260916-02-hygromechanical-indicator`.
- **Alternativa rechazada:** crear `material-memory` como módulo independiente. Ambos hallazgos amplían el mismo problema ya activo —formar y conservar estado físico observable— y separarlos produciría redundancia.
- **Razón:** hay convergencia funcional pero no equivalencia de mecanismo: orientación molecular óptica y deformación higromecánica persistente. El criterio del núcleo se amplía de estado discreto a estado persistente verificable sin declarar nueva madurez.
- **Consecuencia:** `physical-state-interface` permanece M3; confianza 0.87. No se crea prototipo nuevo porque la evidencia no aporta todavía parámetros compatibles con el sustituto digital existente suficientes para una prueba física.

## 2026-09-16 — physical learning remains M1, cycle 02
- **Decisión:** incorporar `f1-20260916-02-flare` y `f1-20260916-02-magnetic-self-learning` a `embodied-dynamics-computation`, pero mantener M1.
- **Alternativa rechazada:** promover a M2 por diversidad de sustratos. FLARE, Hopfield magnético, reservorios y operador mecánico realizan funciones distintas y no existe todavía tarea/métrica común.
- **Razón:** el aprendizaje magnético demuestra adaptación material intrínseca y FLARE memoria temporal multiescala, ampliando la arquitectura posible; esto aumenta evidencia de computación física pero también hace más importante separar memoria, inferencia y aprendizaje.
- **Consecuencia:** confianza 0.77; no se construye benchmark hasta formular una comparación funcional única. La nueva inferencia de motor por stray flux refuerza `legacy-noninvasive-observability` pero sigue en espera por validación específica de montaje. La nueva ficha histórica de bubble memory se deduplica con el precedente ya registrado y no genera una línea nueva.
