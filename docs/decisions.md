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

## 2026-09-16 — embodied-dynamics-computation
- **Decisión:** ampliar `embodied-wave-computation` a `embodied-dynamics-computation`, mantenerlo en M1 y no construir todavía un benchmark.
- **Evidencia:** `f1-20260916T00-mycelium-reservoir` y `f1-20260916T00-active-colloid-reservoir` demuestran reservoir computing mediante dinámica material/colectiva; se suman a `f1-20260915-22-wave-metamaterial-robot` sin asumir equivalencia entre mecanismos.
- **Alternativa rechazada:** promover directamente a M2/M3 por acumulación de ejemplos.
- **Razón:** reservorios temporales y operadores ondulatorios no comparten todavía una tarea y métrica única.

## 2026-09-16 — material-state extension, cycle 02
- **Decisión:** fusionar memoria molecular fotónica y memoria higromecánica persistente dentro de `physical-state-interface`; no abrir un tercer módulo.
- **Evidencia:** `f1-20260916-02-lc-photonic-memory`, `f3-20260916-02-hygromechanical-indicator`.
- **Consecuencia:** `physical-state-interface` permanece M3; no se crea prototipo nuevo sin parámetros suficientes para prueba física.

## 2026-09-16 — physical learning remains M1, cycle 02
- **Decisión:** incorporar `f1-20260916-02-flare` y `f1-20260916-02-magnetic-self-learning` a `embodied-dynamics-computation`, pero mantener M1.
- **Razón:** diversidad de sustratos no sustituye una tarea/métrica común.

## 2026-09-16 — history-state and self-relaxing dynamics, cycle 03
- **Decisión:** fusionar memoria de latching adhesivo en `physical-state-interface` y sumar ZrO2 auto-relajante + metamaterial entrenable a `embodied-dynamics-computation`; ninguna promoción.
- **Razón:** son extensiones funcionales, no prueba de una arquitectura integrada.

## 2026-09-16 — boundary-addressed state, cycle 10
- **Decisión:** incorporar `f1-20260916-1001` a `physical-state-interface` como evidencia de escritura física direccionada desde frontera; mantener M3 y no crear un simulador no calibrado.
- **Evidencia:** `f1-20260916-1001`; `f3-20260916-1001` agrega lectura pasiva resistencia→RF pero sin resolución/distancia final; `f2-20260916-1001` refuerza el precedente de cómputo diferencial físico.
- **Alternativa rechazada:** abrir módulos independientes de memoria mecánica remota o backscatter pasivo.
- **Razón:** la primera amplía directamente el contrato estado/escritura existente; la segunda todavía carece de cadena metrológica completa. Lukyanov es precedente histórico, no una instrucción arquitectónica.
- **Consecuencia:** el criterio del núcleo incorpora selectividad espacial, tasa de error y energía de escritura; backscatter permanece en observabilidad en espera y Lukyanov se fusiona con precedentes diferenciales archivados.
