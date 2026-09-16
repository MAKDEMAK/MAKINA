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
- **Evidencia:** `f1-20260916-1501` demuestra en hardware integrado sensor→codificación temporal→asociación→memoria sin ADC/procesamiento digital local; se suma a `f3-20260916-1401`, `f3-20260916T04-event-vibration`, `f1-20260915-2102` y `f1-20260916-0901`.
- **Alternativa rechazada:** promover `legacy-noninvasive-observability`; `f3-20260916-1501` refuerza stray-flux pero sigue siendo dependiente de máquina/posición y sin presupuesto de incertidumbre común.
- **Razón:** ahora existe una cadena física completa que permite formular un benchmark común de preservación de información, reducción de tráfico, latencia y energía periférica.
- **Consecuencia:** `project/temporal-in-sensor-processing.yaml` fija contrato y criterio de éxito. No M3: todavía no existe el benchmark ejecutable.
- **Deduplicación:** `f2-20260916-1501` fortalece el precedente Parametron ya archivado; no abre línea nueva.
