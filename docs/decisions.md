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
- **Evidencia:** `f1-20260917-1001`, `f2-20260917-1001`, `f3-20260917-1001`.
- **Alternativa rechazada:** desplazar un módulo activo por computación molecular o abrir un módulo SAW.
- **Razón:** F1 demuestra un mecanismo computacional nuevo para el grafo pero con horas de latencia y periferia de laboratorio; F3 mejora la ruta de observabilidad de vibración pero requiere contacto y lector externo; F2 es continuidad histórica de parametron ya registrado.
- **Consecuencia:** se conserva el límite de tres módulos; el incremento de evidencia de menor coste sigue siendo medir los prototipos M3 existentes.

## 2026-09-17 — cycle 11 consolidation
- **Decisión:** fusionar `f1-20260917-1101` en `embodied-dynamics-computation`; sumar `f3-20260917-1101` a `legacy-noninvasive-observability`; archivar `f2-20260917-1101` dentro de `saturable-magnetic-logic-precedent`. Sin promoción ni nuevo prototipo.
- **Evidencia:** `f1-20260917-1101`, `f2-20260917-1101`, `f3-20260917-1101`.
- **Alternativa rechazada:** promover observabilidad magnética a módulo activo o tratar ALWAC 800 como nueva línea de cómputo físico.
- **Razón:** el micelio refuerza una línea activa ya existente pero su NARMA-10 (~0.984), SNR y periferia externa no resuelven el benchmark común; la inversión magnética es funcionalmente relevante pero carece de error/resolución cuantificados en la evidencia abierta; ALWAC 800 es un precedente histórico sin traducción funcional nueva.
- **Consecuencia:** se mantienen tres módulos activos y las madureces M3/M1/M3; el siguiente incremento de evidencia sigue siendo ejecutar y medir los prototipos M3.
