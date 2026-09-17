# Decisions

Registro breve de decisiones de síntesis y desarrollo.

## 2026-09-15 — physical-state-interface
- **Decisión:** promover como núcleo activo una interfaz de estado físico y llevarla a M3 mediante un sustituto digital mínimo.
- **Evidencia:** `f1-20260915-2101`, `f1-20260915-2103`, `f3-20260915-21-passive-crack`, `f3-20260915-21-passive-rf-temp`.
- **Alternativa rechazada como núcleo:** `f1-20260915-2102` + `f3-20260915-21-event-vision`; convergencia fuerte en procesamiento temporal, pero exige hardware especializado y no existe integración directa demostrada.
- **Razón:** la ruta elegida tiene dos pares independientes de evidencia: transducción física pasiva y estado/cómputo multestable, además de un criterio de éxito simulable antes de hardware.
- **Consecuencia:** se crean `src/physical_state.py` y `tests/test_physical_state.py`; el prototipo es M3 pero permanece `created_not_executed`, por lo que no asciende a M4.

## 2026-09-15 — event-powered state extension
- **Decisión:** extender `physical-state-interface` con una ruta evento físico -> energía de pulso -> cambio de estado persistente; mantener M3.
- **Evidencia:** `f3-20260915-22-wiegand-counter`, `f1-20260915-2103`, `f1-20260915-22-light-programmable-mechanical-logic`.
- **Alternativa:** observabilidad no-contacto por stray-flux/speckle permanece en espera.
- **Consecuencia:** `src/event_state.py` y `tests/test_event_state.py`; no M4 sin ejecución.

## 2026-09-16 — embodied-dynamics-computation
- **Decisión:** ampliar a `embodied-dynamics-computation`, mantener M1.
- **Evidencia:** `f1-20260916T00-mycelium-reservoir`, `f1-20260916T00-active-colloid-reservoir`, `f1-20260915-22-wave-metamaterial-robot`.
- **Razón:** falta tarea y métrica común.

## 2026-09-16 — material-state extension, cycle 02
- **Decisión:** fusionar memoria molecular fotónica e higromecánica en `physical-state-interface`; no abrir módulo.
- **Evidencia:** `f1-20260916-02-lc-photonic-memory`, `f3-20260916-02-hygromechanical-indicator`.

## 2026-09-16 — physical learning remains M1, cycle 02
- **Decisión:** incorporar `f1-20260916-02-flare` y `f1-20260916-02-magnetic-self-learning` a `embodied-dynamics-computation`, mantener M1.

## 2026-09-16 — history-state and self-relaxing dynamics, cycle 03
- **Decisión:** fusionar latching adhesivo en `physical-state-interface` y sumar ZrO2 + metamaterial entrenable a `embodied-dynamics-computation`; sin promoción.

## 2026-09-16 — boundary-addressed state, cycle 10
- **Decisión:** incorporar `f1-20260916-1001` a `physical-state-interface`; mantener M3.
- **Alternativa rechazada:** abrir módulos independientes de memoria mecánica remota o backscatter pasivo.
- **Razón:** amplía directamente el contrato estado/escritura; backscatter carece de cadena metrológica completa.

## 2026-09-16 — temporal-in-sensor-processing, cycle 15
- **Decisión:** promover `temporal-in-sensor-processing` de espera a tercer módulo activo M2 y crear su especificación funcional.
- **Evidencia:** `f1-20260916-1501`, `f3-20260916-1401`, `f3-20260916T04-event-vibration`, `f1-20260915-2102`, `f1-20260916-0901`.
- **Alternativa rechazada:** promover `legacy-noninvasive-observability`; sigue dependiente de máquina/posición y sin presupuesto de incertidumbre común.
- **Consecuencia:** `project/temporal-in-sensor-processing.yaml`; no M3 hasta benchmark ejecutable.

## 2026-09-16 — temporal benchmark prototype, cycle 17
- **Decisión:** implementar el benchmark mínimo y promover `temporal-in-sensor-processing` a M3 `created_not_executed`.
- **Evidencia usada:** la cadena acumulada del módulo; `f1-20260916-1701` y `f3-20260916-1701` refuerzan por separado discretización e integración física, pero se fusionan en `physical-state-interface` y no son causa de la promoción temporal.
- **Alternativa rechazada:** abrir una línea fluidica desde `f2-20260916-1701`; FLODAC es precedente fuerte pero no aporta una necesidad funcional nueva y su velocidad fue una limitación documentada.
- **Razón:** el siguiente paso de menor coste era convertir la especificación M2 ya existente en código reproducible con referencia uniforme, encoding por umbral y encoding por latencia+estado desvaneciente.
- **Consecuencia:** `src/temporal_benchmark.py` y `tests/test_temporal_benchmark.py`. M4 queda bloqueado hasta ejecutar tests/benchmark y registrar métricas; energía de hardware permanece explícitamente no medida.

## 2026-09-17 — cycle 07 consolidation
- **Decisión:** fusionar `f1-20260917-0701` en `embodied-dynamics-computation`, `f3-20260917-0701` en `physical-state-interface` y deduplicar `f2-20260917-0701` dentro del precedente cryotron; sin promoción de madurez ni cuarto módulo.
- **Evidencia:** `f1-20260917-0701`, `f2-20260917-0701`, `f3-20260917-0701`.
- **Alternativa rechazada:** abrir un módulo específico de resonador temporal o memoria tiempo-temperatura.
- **Razón:** ambos mecanismos nuevos encajan en contratos activos existentes; el resonador aún no comparte benchmark ejecutado y el TTI no reconstruye un historial térmico único. El cryotron es evidencia histórica redundante.
- **Consecuencia:** se mantiene el límite de tres módulos y se prioriza medir artefactos M3 existentes.
