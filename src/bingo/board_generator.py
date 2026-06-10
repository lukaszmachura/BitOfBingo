"""Bingo board generation utilities."""

from __future__ import annotations

import random

from bingo.board import BingoBoard


class BingoBoardGenerator:
    """Generates custom bingo boards.

    The generated board:

    - contains 25 fields,
    - uses "CM" in the center field,
    - contains 24 unique integers,
    - draws numbers from a configurable range.
    """

    def __init__(
        self,
        min_value: int = -75,
        max_value: int = 75,
        rng: random.Random | None = None,
    ) -> None:
        """Initializes the generator.

        Args:
            min_value: Minimum value that can appear on a board.
            max_value: Maximum value that can appear on a board.
            rng: Optional random number generator.

        Raises:
            TypeError: If min_value or max_value are not integers.
            ValueError: If min_value is greater than max_value.
            ValueError: If the range contains fewer than 24 unique values.
        """
        if not isinstance(min_value, int):
            raise TypeError("min_value must be an integer")

        if not isinstance(max_value, int):
            raise TypeError("max_value must be an integer")

        if min_value > max_value:
            raise ValueError(
                "min_value must be less than or equal to max_value"
            )

        available_numbers = max_value - min_value + 1

        if available_numbers < 24:
            raise ValueError(
                "The range must contain at least 24 unique values"
            )

        self.min_value = min_value
        self.max_value = max_value
        self._rng = rng or random.Random()
        self._board_counter = 0

    def _next_board_id(self) -> str:
        self._board_counter += 1
        return f"{self._board_counter:06d}"

    @classmethod
    def from_seed(
        cls,
        seed: int,
        min_value: int = -75,
        max_value: int = 75,
    ) -> "BingoBoardGenerator":
        """Creates a generator with a fixed random seed.

        Args:
            seed: Seed used to initialize the random number generator.
            min_value: Minimum value that can appear on a board.
            max_value: Maximum value that can appear on a board.

        Returns:
            A configured BingoBoardGenerator instance.

        Raises:
            TypeError: If seed is not an integer.
        """
        if not isinstance(seed, int):
            raise TypeError("seed must be an integer")

        return cls(
            min_value=min_value,
            max_value=max_value,
            rng=random.Random(seed),
        )

    def generate(self) -> BingoBoard:
        """Generates a single bingo board.

        Returns:
            A valid BingoBoard instance.
        """
        numbers = self._generate_numbers()

        grid: list[list[int | str]] = []
        index = 0

        for row in range(5):
            current_row: list[int | str] = []

            for col in range(5):
                if row == 2 and col == 2:
                    current_row.append("CM")
                else:
                    current_row.append(numbers[index])
                    index += 1

            grid.append(current_row)

        return BingoBoard(
                board_id=self._next_board_id(),
                grid=grid,
                )

    def generate_many(
        self,
        count: int,
    ) -> list[BingoBoard]:
        """Generates multiple bingo boards.

        Args:
            count: Number of boards to generate.

        Returns:
            A list of BingoBoard instances.

        Raises:
            TypeError: If count is not an integer.
            ValueError: If count is less than 1.
        """
        if not isinstance(count, int):
            raise TypeError("count must be an integer")

        if count < 1:
            raise ValueError(
                "count must be greater than 0"
            )

        return [
            self.generate()
            for _ in range(count)
        ]

    def _generate_numbers(self) -> list[int]:
        """Generates 24 unique integers.

        Returns:
            A list containing 24 unique integers sampled
            from the configured range.
        """
        return self._rng.sample(
            range(
                self.min_value,
                self.max_value + 1,
            ),
            k=24,
        )