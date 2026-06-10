import random


class SystemValidator:
    """Validates and selects proper binary representation system."""

    def __init__(self, bits: int = 8):
        self.bits = bits

    SYSTEM_RULES = {
        "U1": lambda v, b: abs(v) <= (2 ** (b - 1) - 1),
        "U2": lambda v, b: -2 ** (b - 1) <= v <= 2 ** (b - 1) - 1,
        "NKB": lambda v, b: 0 <= v <= (2 ** b - 1),
        "ZM": lambda v, b: abs(v) <= (2 ** (b - 1) - 1),

        # Bias systems (generic constraint)
        "STD BIAS": lambda v, b: -(2 ** (b-1) - 1) <= v <= -(2 ** (b-1) - 1) + (2 ** b - 1),
        "8421": lambda v, b: -b <= v <= -b + (2 ** b - 1),
        "NUDING": lambda v, b: -(3 * b + 2) <= v <= -(3 * b + 2) + (2 ** b - 1),
        "STIBITZ": lambda v, b: -(b + 3) <= v <= -(b + 3) + (2 ** b - 1),
        "DIAMOND": lambda v, b: -(27 * b + 6) <= v <= -(27 * b + 6) + (2 ** b - 1),
    }

    def is_valid(self, value: int, system: str) -> bool:
        rule = self.SYSTEM_RULES.get(system)

        if not rule:
            return False

        return rule(value, self.bits)

    def pick_valid_system(self, value: int, systems: list[str]) -> str:
        valid = [s for s in systems if self.is_valid(value, s)]

        if not valid:
            raise ValueError(f"No valid system for value={value}")

        return random.choice(valid)