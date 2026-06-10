class BinaryPresenter:
    def format(self, value: int, system: str, binary: str) -> str:
        return f"""
====================
BINARY CLASSROOM
====================

System: {system}
Value:  {value}

Binary:
{binary}
"""