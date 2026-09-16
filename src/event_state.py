"""Event-to-state surrogates for MAKINA.

Behavioral contracts for physical mechanisms that convert transient inputs into
persistent discrete state. These models do not simulate device energetics.
"""

from dataclasses import dataclass, field


@dataclass
class EventEnergyGate:
    required_nj: float = 38.0

    def accepts(self, pulse_nj: float) -> bool:
        if pulse_nj < 0:
            raise ValueError("pulse energy must be non-negative")
        return pulse_nj >= self.required_nj


@dataclass
class PersistentCounter:
    bits: int = 1
    state: int = 0

    @property
    def modulus(self) -> int:
        return 1 << self.bits

    def register(self, event: bool) -> int:
        if event:
            self.state = (self.state + 1) % self.modulus
        return self.state


@dataclass
class PeakThresholdMemory:
    """Latch the highest threshold crossed by a transient scalar input.

    State 0 means no threshold has been crossed; state N means thresholds
    0..N-1 have been exceeded. Lower later inputs cannot erase the peak state.
    """

    thresholds: tuple[float, ...] = field(default_factory=lambda: tuple(20 + i * (230 / 9) for i in range(10)))
    state: int = 0

    def __post_init__(self) -> None:
        if not self.thresholds or any(b <= a for a, b in zip(self.thresholds, self.thresholds[1:])):
            raise ValueError("thresholds must be non-empty and strictly increasing")

    def register(self, value: float) -> int:
        crossed = sum(value >= threshold for threshold in self.thresholds)
        self.state = max(self.state, crossed)
        return self.state

    def reset(self) -> None:
        self.state = 0


def run_event_pipeline(pulse_energies_nj, gate=None, counter=None):
    gate = gate or EventEnergyGate()
    counter = counter or PersistentCounter()
    trace = []
    for energy in pulse_energies_nj:
        accepted = gate.accepts(energy)
        trace.append({"pulse_nj": energy, "accepted": accepted, "state": counter.register(accepted)})
    return trace
