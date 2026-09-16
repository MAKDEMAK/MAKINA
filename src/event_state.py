"""Event-to-state surrogate for MAKINA.

Models the strongest new convergence in cycle 22:
a discrete physical event supplies enough local energy to register a persistent state change.
This is a behavioral contract, not a hardware-energy simulation.
"""

from dataclasses import dataclass


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


def run_event_pipeline(pulse_energies_nj, gate=None, counter=None):
    gate = gate or EventEnergyGate()
    counter = counter or PersistentCounter()
    trace = []
    for energy in pulse_energies_nj:
        accepted = gate.accepts(energy)
        trace.append({"pulse_nj": energy, "accepted": accepted, "state": counter.register(accepted)})
    return trace
