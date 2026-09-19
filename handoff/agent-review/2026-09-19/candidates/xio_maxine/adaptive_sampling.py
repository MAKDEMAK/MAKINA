#!/usr/bin/env python3
"""Adaptive observation policy for XIO, derived from MAXINE M2.

Selects optional visual observations under a finite budget.
It is camera-agnostic and intended for off-device validation before Android wiring.

It MUST NOT remove required calibration frames such as showcontrol/automap.py
Hadamard steps. Adaptive selection is only for observations allowed to be skipped.
"""
from __future__ import annotations

import math
from dataclasses import asdict, dataclass

FIELDS = (
    "spatial_priority",
    "temporal_change",
    "spectral_information",
    "adaptation_state",
    "task_utility",
)

MAXINE_SOURCE = "MAKDEMAK/MAXINE:project/modules/adaptive-visual-sampling/spec.yaml"
MAKINA_PROTOTYPE = "MAKDEMAK/MAKINA:integrations/xio-maxine/adaptive_sampling_baseline.py"
CANONICAL_TARGET = "ligereza/XIO:xio/vision/adaptive_sampling.py"


@dataclass(frozen=True)
class Candidate:
    id: str
    spatial_priority: float = 0.0
    temporal_change: float = 0.0
    spectral_information: float = 0.0
    adaptation_state: float = 0.0
    task_utility: float = 0.0


def _finite01(value):
    x = float(value)
    if not math.isfinite(x) or not 0.0 <= x <= 1.0:
        raise ValueError("metrics must be finite numbers in [0,1]")
    return x


def candidate_from_mapping(row):
    if "id" not in row:
        raise ValueError("candidate id required")
    return Candidate(
        id=str(row["id"]),
        **{key: _finite01(row.get(key, 0.0)) for key in FIELDS},
    )


def normalize_weights(weights=None):
    raw = weights or {key: 1.0 for key in FIELDS}
    out = {}
    for key in FIELDS:
        value = float(raw.get(key, 0.0))
        if not math.isfinite(value):
            raise ValueError("weights must be finite")
        out[key] = max(0.0, value)
    total = sum(out.values())
    if total <= 0:
        raise ValueError("at least one positive weight required")
    return {key: value / total for key, value in out.items()}


def score(candidate, weights=None):
    weights = normalize_weights(weights)
    return sum(getattr(candidate, key) * weights[key] for key in FIELDS)


def select_adaptive(candidates, budget, weights=None):
    budget = int(budget)
    if budget < 0:
        raise ValueError("budget must be >= 0")
    ranked = sorted(candidates, key=lambda item: (-score(item, weights), item.id))
    return ranked[: min(budget, len(ranked))]


def select_uniform(candidates, budget):
    budget = int(budget)
    if budget < 0:
        raise ValueError("budget must be >= 0")
    n = len(candidates)
    count = min(budget, n)
    if count == 0:
        return []
    if count == n:
        return list(candidates)
    if count == 1:
        return [candidates[0]]
    indices = [round(i * (n - 1) / (count - 1)) for i in range(count)]
    return [candidates[i] for i in indices]


def retained_metrics(selected):
    if not selected:
        return {key: 0.0 for key in FIELDS}
    n = float(len(selected))
    return {key: sum(getattr(item, key) for item in selected) / n for key in FIELDS}


def compare_equal_budget(candidates, budget, *, weights=None, tolerances=None):
    """MAXINE gate: improve >=1 metric while protecting all others by tolerance."""
    if tolerances is None:
        raise ValueError("explicit tolerances required for MAXINE comparison")
    checked = {}
    for key in FIELDS:
        value = float(tolerances.get(key, 0.0))
        if not math.isfinite(value) or value < 0:
            raise ValueError("tolerances must be finite and >= 0")
        checked[key] = value

    adaptive = select_adaptive(candidates, budget, weights)
    uniform = select_uniform(candidates, budget)
    am = retained_metrics(adaptive)
    um = retained_metrics(uniform)
    delta = {key: am[key] - um[key] for key in FIELDS}
    protected_ok = all(delta[key] >= -checked[key] for key in FIELDS)
    improved = any(delta[key] > checked[key] for key in FIELDS)

    return {
        "schema": "xio-maxine-adaptive-comparison-v1",
        "budget": int(budget),
        "adaptive_ids": [item.id for item in adaptive],
        "uniform_ids": [item.id for item in uniform],
        "adaptive_metrics": am,
        "uniform_metrics": um,
        "delta": delta,
        "tolerances": checked,
        "protected_ok": protected_ok,
        "improved": improved,
        "passed": protected_ok and improved,
        "provenance": {
            "maxine_source": MAXINE_SOURCE,
            "makina_prototype": MAKINA_PROTOTYPE,
            "canonical_target": CANONICAL_TARGET,
            "physical_xiaomi_validation": False,
        },
    }


def build_manifest(rows, budget, *, strategy="adaptive", weights=None):
    candidates = [candidate_from_mapping(row) for row in rows]
    if strategy == "adaptive":
        selected = select_adaptive(candidates, budget, weights)
    elif strategy == "uniform":
        selected = select_uniform(candidates, budget)
    else:
        raise ValueError("strategy must be 'adaptive' or 'uniform'")
    return {
        "schema": "xio-adaptive-observation-v1",
        "strategy": strategy,
        "budget": int(budget),
        "candidate_count": len(candidates),
        "selected_count": len(selected),
        "selected": [asdict(item) for item in selected],
        "provenance": {
            "maxine_source": MAXINE_SOURCE,
            "makina_prototype": MAKINA_PROTOTYPE,
            "canonical_target": CANONICAL_TARGET,
            "physical_xiaomi_validation": False,
        },
        "constraints": {
            "camera_capture_implemented_here": False,
            "safe_to_skip_required_calibration_frames": False,
        },
    }
