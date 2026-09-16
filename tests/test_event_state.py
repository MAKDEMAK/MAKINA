from src.event_state import EventEnergyGate, PeakThresholdMemory, PersistentCounter, run_event_pipeline


def test_energy_gate_uses_experimental_counter_threshold():
    gate = EventEnergyGate()
    assert not gate.accepts(37.9)
    assert gate.accepts(38.0)
    assert gate.accepts(130.0)


def test_single_bit_counter_persists_and_wraps():
    counter = PersistentCounter(bits=1)
    assert [counter.register(x) for x in [True, False, True, True]] == [1, 1, 0, 1]


def test_subthreshold_pulses_do_not_change_state():
    trace = run_event_pipeline([10.0, 37.9, 38.0, 20.0])
    assert [x["state"] for x in trace] == [0, 0, 1, 1]


def test_reported_wiegand_maximum_has_energy_margin():
    gate = EventEnergyGate(required_nj=38.0)
    assert gate.accepts(130.0)
    assert 130.0 / 38.0 > 3.4


def test_peak_threshold_memory_latches_highest_crossing():
    memory = PeakThresholdMemory(thresholds=(20.0, 50.0, 100.0, 250.0))
    assert [memory.register(x) for x in (10.0, 55.0, 30.0, 120.0, 80.0)] == [0, 2, 2, 3, 3]


def test_peak_threshold_memory_reset_and_top_level():
    memory = PeakThresholdMemory(thresholds=(20.0, 50.0, 100.0, 250.0))
    assert memory.register(300.0) == 4
    memory.reset()
    assert memory.state == 0


def test_peak_threshold_memory_rejects_invalid_thresholds():
    try:
        PeakThresholdMemory(thresholds=(20.0, 20.0, 50.0))
    except ValueError:
        pass
    else:
        raise AssertionError("non-increasing thresholds must be rejected")
