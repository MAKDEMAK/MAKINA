"""Off-device validation for the MAXINE -> XIO sampling policy."""
from pathlib import Path
import importlib.util
import math
import sys

MODULE = Path(__file__).with_name("adaptive_sampling.py")
spec = importlib.util.spec_from_file_location("adaptive_sampling", MODULE)
S = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = S
spec.loader.exec_module(S)


def test_weighted_policy_prefers_task_utility():
    rows = [
        S.Candidate("spatial", spatial_priority=1.0),
        S.Candidate("motion", temporal_change=1.0),
        S.Candidate("task", task_utility=1.0),
    ]
    weights = {"task_utility": 4, "temporal_change": 2, "spatial_priority": 1}
    assert [x.id for x in S.select_adaptive(rows, 2, weights)] == ["task", "motion"]


def test_uniform_uses_same_budget():
    rows = [S.Candidate(str(i)) for i in range(5)]
    assert [x.id for x in S.select_uniform(rows, 3)] == ["0", "2", "4"]


def test_equal_budget_can_pass_maxine_gate():
    rows = [
        S.Candidate("a", task_utility=0.10),
        S.Candidate("b", task_utility=1.00),
        S.Candidate("c", task_utility=0.20),
        S.Candidate("d", task_utility=0.90),
    ]
    result = S.compare_equal_budget(
        rows, 2,
        weights={"task_utility": 1},
        tolerances={key: 0.0 for key in S.FIELDS},
    )
    assert result["budget"] == 2
    assert result["passed"] is True
    assert result["delta"]["task_utility"] > 0


def test_gate_fails_when_other_protected_metric_is_sacrificed():
    rows = [
        S.Candidate("a", task_utility=0.1, spatial_priority=1.0),
        S.Candidate("b", task_utility=1.0, spatial_priority=0.0),
        S.Candidate("c", task_utility=0.1, spatial_priority=1.0),
    ]
    result = S.compare_equal_budget(
        rows, 1,
        weights={"task_utility": 1},
        tolerances={key: 0.0 for key in S.FIELDS},
    )
    assert result["improved"] is True
    assert result["protected_ok"] is False
    assert result["passed"] is False


def test_validation_rejects_implicit_or_bad_assumptions():
    try:
        S.compare_equal_budget([S.Candidate("a")], 1)
        raise AssertionError("comparison accepted missing tolerances")
    except ValueError:
        pass

    for value in (-0.1, 1.1, math.inf):
        try:
            S.candidate_from_mapping({"id": "bad", "task_utility": value})
            raise AssertionError("accepted invalid normalized metric")
        except ValueError:
            pass

    try:
        S.score(S.Candidate("a"), {key: 0 for key in S.FIELDS})
        raise AssertionError("accepted zero-sum weights")
    except ValueError:
        pass
