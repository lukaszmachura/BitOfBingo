import random
from .system_validator import SystemValidator


class BinaryGameEngine:
    SYSTEMS = [
        "U1",
        "U2",
        "NKB",
        "ZM",
        "STD BIAS",
        "8421",
        "NUDING",
        "STIBITZ",
        "DIAMOND",
    ]

    def __init__(self, min_value: int = -75, max_value: int = 75, bits: int = 8, seed: int | None = None):
        self.min_value = min_value
        self.max_value = max_value
        self._available_values = list(range(min_value, max_value + 1))

        if seed is None:
            seed = random.randint(0, 2**32 - 1)
        self.rng = random.Random(seed)
        self.rng.shuffle(self._available_values)

        self.validator = SystemValidator(bits)

    def next(self) -> tuple[int, str]:
        if not self._available_values:
            raise RuntimeError("No more values available.")
        
        value = self._available_values.pop()
        system = self.validator.pick_valid_system(
            value,
            self.SYSTEMS,
        )

        print(f"Generated value: {value}, System: {system}, Remaining values: {len(self._available_values)}")
        return value, system
    
    def reset(self) -> None:
        self.rng = random.Random(random.randint(0, 2**32 - 1))
        self._available_values = list(range(self.min_value, self.max_value + 1))
        self.rng.shuffle(self._available_values)
