from src.physical_state import HystereticTernaryQuantizer, PhysicalFSM, run_pipeline


def test_hysteresis_rejects_threshold_noise():
    q = HystereticTernaryQuantizer()
    seq = [0.0, 0.55, 0.59, 0.58, 0.61, 0.55, 0.45, 0.41]
    states = [q.update(v) for v in seq]
    assert states == [0, 0, 0, 0, 1, 1, 1, 1]


def test_release_returns_to_neutral():
    q = HystereticTernaryQuantizer()
    assert q.update(0.7) == 1
    assert q.update(0.5) == 1
    assert q.update(0.39) == 0


def test_fsm_persists_and_saturates():
    fsm = PhysicalFSM()
    assert [fsm.step(x) for x in [1, 1, 1, 0, -1]] == [1, 2, 2, 2, 1]


def test_pipeline_is_deterministic():
    values = [0.0, 0.7, 0.5, 0.3, -0.7, -0.5, -0.3]
    assert run_pipeline(values) == run_pipeline(values)
