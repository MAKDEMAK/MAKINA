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

## 2026-09-16 — temporal-in-sensor-processing
- **Decisión:** promover a tercer módulo activo y posteriormente M3 mediante benchmark mínimo.
- **Evidencia:** `f1-20260916-1501`, `f3-20260916-1401`, `f3-20260916T04-event-vibration`, `f1-20260915-2102`, `f1-20260916-0901`.
- **Consecuencia:** `src/temporal_benchmark.py` y `tests/test_temporal_benchmark.py`; M4 bloqueado hasta ejecución y métricas.

## 2026-09-17 — cycle 07 consolidation
- **Decisión:** fusionar `f1-20260917-0701` en `embodied-dynamics-computation`, `f3-20260917-0701` en `physical-state-interface` y deduplicar `f2-20260917-0701`; sin promoción.

## 2026-09-17 — cycle 09 consolidation
- **Decisión:** fusionar `f1-20260917-0901` en `temporal-in-sensor-processing`, `f3-20260917-0901` en `physical-state-interface` y deduplicar `f2-20260917-0901`; sin promoción.

## 2026-09-17 — cycle 10 consolidation
- **Decisión:** mantener `f1-20260917-1001` como `thermodynamic-molecular-computation` en espera; sumar `f3-20260917-1001` a `legacy-noninvasive-observability`; deduplicar `f2-20260917-1001` dentro de `parametric-phase-logic-precedent`. Sin promoción ni nuevo prototipo.

## 2026-09-17 — cycle 11 consolidation
- **Decisión:** fusionar `f1-20260917-1101` en `embodied-dynamics-computation`; sumar `f3-20260917-1101` a `legacy-noninvasive-observability`; archivar `f2-20260917-1101` dentro de `saturable-magnetic-logic-precedent`. Sin promoción ni nuevo prototipo.

## 2026-09-17 — cycle 13 consolidation
- **Decisión:** fusionar `f1-20260917-1301` en `temporal-in-sensor-processing`, `f3-20260917-1301` en `physical-state-interface` y deduplicar `f2-20260917-1301` dentro de `balanced-ternary-precedent`. Sin promoción ni nuevo prototipo.

## 2026-09-17 — cycle 15 consolidation
- **Decisión:** no promover `f1-20260917-1501`; sumar `f3-20260917-1501` a observabilidad legacy en espera; archivar `f2-20260917-1501` como precedente de vuelo fluidico. Sin nuevo prototipo.

## 2026-09-17 — cycle 17 consolidation
- **Decisión:** fusionar `f1-20260917-1701` en `embodied-dynamics-computation`; sumar `f3-20260917-1701` a `legacy-noninvasive-observability`; archivar `f2-20260917-1701` como `rasterized-videotex-precedent`. Sin promoción ni nuevo prototipo.

## 2026-09-17 — cycle 18 consolidation
- **Decisión:** fusionar `f1-20260917-1801` y `f3-20260917-1801` en `physical-state-interface`; deduplicar `f2-20260917-1801` dentro de `fluidic-general-computing-precedent`. Mantener M3/M1/M3 y no crear prototipo nuevo.
- **Evidencia:** `f1-20260917-1801`, `f2-20260917-1801`, `f3-20260917-1801`.
- **Alternativa rechazada:** abrir un cuarto módulo de control mecánico pasivo o una línea independiente de memoria química acumulativa.
- **Razón:** F1 demuestra sensado+decisión+reconfiguración mecánica sin electrónica, pero con lógica predeterminada; F3 demuestra memoria material acumulativa sin electrónica, pero no identifica de forma única la trayectoria térmica; ambos convergen funcionalmente con el módulo físico existente. FLODAC es continuidad histórica ya representada.
- **Consecuencia:** el siguiente incremento de evidencia sigue siendo ejecutar y medir los prototipos M3 existentes antes de M4.

## 2026-09-17 — cycle 19 consolidation
- **Decisión:** fusionar `f1-20260917-1901` y `f3-20260917-1901` en `physical-state-interface`; deduplicar `f2-20260917-1901` dentro de `air-cushion-transport`. Mantener M3/M1/M3 y no crear prototipo nuevo.
- **Evidencia:** `f1-20260917-1901`, `f2-20260917-1901`, `f3-20260917-1901`.
- **Alternativa rechazada:** abrir un modulo iontronico independiente o promover memoria espacial de presion como cuarto modulo.
- **Razón:** F1 aporta estado/plasticidad material multiescala por transporte ionico y F3 aporta transduccion+memoria espacial mecano-quimica; ambos amplian el mismo patron funcional de estado fisico ya activo. Aerotrain ya estaba representado y sigue sin traduccion funcional al nucleo.
- **Consecuencia:** no M4; medir los artefactos M3 existentes sigue teniendo mayor valor de informacion que crear otro prototipo.

## 2026-09-17 — cycle 21 final consolidation
- **Decisión:** cerrar la síntesis en el último ciclo común completo, `2026-09-17T21`, y cerrar la investigación MAKINA.
- **Evidencia:** `f1-20260917-2101`, `f2-20260917-2101`, `f3-20260917-2101`.
- **Integración:** `f3-20260917-2101` se suma a `legacy-noninvasive-observability`; `f2-20260917-2101` se deduplica en `air-cushion-transport`; `f1-20260917-2101` queda archivado como `non-hilbertian-kernel-methods` por ausencia de traducción funcional defendible al núcleo físico.
- **Alternativa rechazada:** abrir un cuarto módulo activo o forzar una relación entre kernels no-CND y los módulos físicos existentes.
- **Consecuencia:** no hay promoción de madurez. El snapshot final mantiene `physical-state-interface` M3, `embodied-dynamics-computation` M1 y `temporal-in-sensor-processing` M3.
- **Auditoría:** ciclos con evidencia parcial pero sin marcador común completo no se sintetizan: T05, T06, T08, T12, T14, T20 y T22.

## 2026-09-17 — final F4 execution validation
- **Decisión:** ejecutar los artefactos M3 existentes antes del cierre definitivo y no promover por mera existencia del código.
- **Resultado:** 15/16 tests pasan. `physical_state` + `event_state`: 14/14. En temporal, `threshold_event_encoding` obtiene 28.99x reducción, score 1.0 y ~3 ms de error; `latency_fading` obtiene 500x reducción pero score 0.0 y ~44.98 ms de error.
- **Alternativa rechazada:** promover a M4 por el éxito del sustituto digital o ajustar el test para hacerlo pasar.
- **Razón:** no existe medición física/hardware y una de las dos variantes temporales falla el criterio definido.
- **Consecuencia:** madurez final sin cambios: `physical-state-interface` M3, `embodied-dynamics-computation` M1, `temporal-in-sensor-processing` M3. Resultados persistidos en `artifacts/`.

