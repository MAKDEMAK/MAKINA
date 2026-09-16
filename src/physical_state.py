"""Minimal digital surrogate for MAKINA's physical-state interface.

This does not claim a hardware integration. It tests the design contract:
continuous physical proxy -> hysteretic discrete state -> deterministic state memory.
"""

from dataclasses import dataclass


@dataclass
class HystereticTernaryQuantizer:
    """Map a normalized scalar to {-1, 0, +1} with hysteresis."""
    enter: float = 0.60
    release: float = 0.40
    state: int = 0

    def update(self, value: float) -> int:
        if self.state == 0:
            if value >= self.enter:
                self.state = 1
            elif value <= -self.enter:
                self.state = -1
        elif self.state == 1 and value <= self.release:
            self.state = 0
        elif self.state == -1 and value >= -self.release:
            self.state = 0
        return self.state


@dataclass
class PhysicalFSM:
    """Small state machine whose memory persists between observations."""
    state: int = 0

    def step(self, symbol: int) -> int:
        if symbol not in (-1, 0, 1):
            raise ValueError("symbol must be -1, 0, or 1")
        # Saturating accumulator: a compact surrogate for persistent physical state.
        self.state = max(-2, min(2, self.state + symbol))
        return self.state


def run_pipeline(values, quantizer=None, machine=None):
    q = quantizer or HystereticTernaryQuantizer()
    fsm = machine or PhysicalFSM()
    output = []
    for value in values:
        symbol = q.update(value)
        output.append({"input": value, "symbol": symbol, "state": fsm.step(symbol)})
    return output
