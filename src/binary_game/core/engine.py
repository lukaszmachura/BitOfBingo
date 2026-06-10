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

    def __init__(self, min_value=-75, max_value=75, bits=8):
        self.min_value = min_value
        self.max_value = max_value
        self.validator = SystemValidator(bits)

    def next(self):
        value = random.randint(self.min_value, self.max_value)

        system = self.validator.pick_valid_system(
            value,
            self.SYSTEMS,
        )

        return value, system