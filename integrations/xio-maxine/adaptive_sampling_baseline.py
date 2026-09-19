#!/usr/bin/env python3
"""XIO↔MAXINE passive adaptive sampling prototype.

Derived from frozen MAXINE M2 specification without modifying MAXINE. This is a
camera-agnostic policy artifact: it selects regions/frames from normalized
metrics under a finite budget and retains an equal-budget uniform control.
It does not capture/upload images and is not proof of deployment on Xiaomi.
"""
from __future__ import annotations
import argparse, json, math
from dataclasses import asdict, dataclass
from pathlib import Path

FIELDS = ("spatial_priority", "temporal_change", "spectral_information", "adaptation_state", "task_utility")

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
    return Candidate(str(row["id"]), **{key: _finite01(row.get(key, 0.0)) for key in FIELDS})

def score(candidate, weights=None):
    weights = weights or {key: 1.0 for key in FIELDS}
    positive = {key: max(0.0, float(weights.get(key, 0.0))) for key in FIELDS}
    denominator = sum(positive.values())
    if denominator <= 0:
        raise ValueError("at least one positive weight required")
    return sum(getattr(candidate, key) * positive[key] for key in FIELDS) / denominator

def select_adaptive(candidates, budget, weights=None):
    if budget < 0: raise ValueError("budget must be >= 0")
    return sorted(candidates, key=lambda item: (-score(item, weights), item.id))[:min(budget, len(candidates))]

def select_uniform(candidates, budget):
    if budget < 0: raise ValueError("budget must be >= 0")
    n, b = len(candidates), min(budget, len(candidates))
    if b == 0: return []
    if b == n: return list(candidates)
    indices = [round(i * (n - 1) / (b - 1)) for i in range(b)] if b > 1 else [0]
    return [candidates[i] for i in indices]

def self_test():
    rows = [Candidate("a", task_utility=1), Candidate("b", temporal_change=1), Candidate("c"), Candidate("d", spatial_priority=1)]
    weights = {"task_utility": 3, "temporal_change": 2, "spatial_priority": 1}
    assert [x.id for x in select_adaptive(rows, 2, weights)] == ["a", "b"]
    assert len(select_uniform(rows, 2)) == 2
    assert len(select_adaptive(rows, 99)) == 4

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", nargs="?", type=Path)
    p.add_argument("--budget", type=int, default=1)
    p.add_argument("--strategy", choices=("adaptive", "uniform"), default="adaptive")
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    if a.self_test:
        self_test(); print("self-test: ok"); return 0
    if a.input is None: p.error("input required unless --self-test")
    rows = [candidate_from_mapping(json.loads(line)) for line in a.input.read_text(encoding="utf-8").splitlines() if line.strip()]
    selected = select_adaptive(rows, a.budget) if a.strategy == "adaptive" else select_uniform(rows, a.budget)
    print(json.dumps({"schema":"xio-maxine-adaptive-sampling-v1","strategy":a.strategy,"budget":a.budget,"candidate_count":len(rows),"processed_sample_count":len(selected),"selected":[asdict(x) for x in selected],"provenance":{"maxine_source":"project/modules/adaptive-visual-sampling/spec.yaml","implementation_target":"ligereza/vibecodeine/xio","physical_xiaomi_validation":False}}, indent=2))
    return 0

if __name__ == "__main__": raise SystemExit(main())
