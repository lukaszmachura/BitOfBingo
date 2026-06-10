from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class BingoBoard:
    """Represents a single bingo board.

    Attributes:
        grid: A 5x5 grid containing integers and a central
            marker ("BB") in the middle field.
    """
    board_id: str
    grid: list[list[int | str]]

    @property
    def size(self) -> int: # type: ignore
        """Returns board size."""
        return 5

    def __post_init__(self) -> None:
        """Validates board structure and values."""
        if len(self.grid) != 5:
            raise ValueError(
                "A bingo board must contain exactly 5 rows."
            )

        for row in self.grid:
            if len(row) != 5:
                raise ValueError(
                    "Each row must contain exactly 5 values."
                )

        if self.grid[2][2] != "BB":
            raise ValueError(
                "The center field must contain 'BB'."
            )

        for row_index, row in enumerate(self.grid):
            for col_index, value in enumerate(row):

                if row_index == 2 and col_index == 2:
                    continue

                if not isinstance(value, int):
                    raise TypeError(
                        "Board values must be integers."
                    )

                if not -75 <= value <= 75:
                    raise ValueError(
                        "Board values must be in range [-75, 75]."
                    )

    @property
    def size(self) -> int:
        """Returns board size."""
        return 5

    def as_rows(self) -> list[list[int | str]]:
        """Returns board rows."""
        return self.grid

    def __str__(self) -> str:
        """Returns a human-readable representation."""
        lines = []

        for row in self.grid:
            lines.append(
                " ".join(f"{str(value):>4}" for value in row)
            )

        return "\n".join(lines)
    


if __name__ == "__main__":
    board = BingoBoard(
        board_id="test",
        grid=[
            [-75, 32, 14, -17, 75],
            [-75, 32, 14, -17, 75],
            [-75, 32, "BB", -17, 75],
            [-75, 32, 14, -17, 75],
            [-75, 32, 14, -17, 75],
        ],
    )

    print(board)