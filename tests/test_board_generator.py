import random

import pytest

from bingo.board import BingoBoard
from bingo.board_generator import BingoBoardGenerator


# ============================================================
# Constructor validation
# ============================================================

def test_default_constructor():
    generator = BingoBoardGenerator()

    assert generator.min_value == -75
    assert generator.max_value == 75


def test_custom_range():
    generator = BingoBoardGenerator(
        min_value=-20,
        max_value=20,
    )

    assert generator.min_value == -20
    assert generator.max_value == 20


def test_min_value_must_be_int():
    with pytest.raises(
        TypeError,
        match="min_value must be an integer",
    ):
        BingoBoardGenerator(
            min_value="-75",
        )


def test_max_value_must_be_int():
    with pytest.raises(
        TypeError,
        match="max_value must be an integer",
    ):
        BingoBoardGenerator(
            max_value="75",
        )


def test_min_must_not_be_greater_than_max():
    with pytest.raises(
        ValueError,
        match="min_value must be less than or equal",
    ):
        BingoBoardGenerator(
            min_value=10,
            max_value=0,
        )


def test_range_must_contain_at_least_24_values():
    with pytest.raises(
        ValueError,
        match="at least 24 unique values",
    ):
        BingoBoardGenerator(
            min_value=0,
            max_value=22,
        )


# ============================================================
# Board generation
# ============================================================

def test_generate_returns_bingo_board():
    generator = BingoBoardGenerator()

    board = generator.generate()

    assert isinstance(board, BingoBoard)


def test_center_contains_bb():
    generator = BingoBoardGenerator()

    board = generator.generate()

    assert board.grid[2][2] == "BB"


def test_board_contains_24_numbers():
    generator = BingoBoardGenerator()

    board = generator.generate()

    values = [
        value
        for row in board.grid
        for value in row
        if value != "BB"
    ]

    assert len(values) == 24


def test_board_numbers_are_unique():
    generator = BingoBoardGenerator()

    board = generator.generate()

    values = [
        value
        for row in board.grid
        for value in row
        if value != "BB"
    ]

    assert len(values) == len(set(values))


def test_numbers_respect_range():
    generator = BingoBoardGenerator(
        min_value=-10,
        max_value=20,
    )

    board = generator.generate()

    values = [
        value
        for row in board.grid
        for value in row
        if value != "BB"
    ]

    assert all(
        -10 <= value <= 20
        for value in values
    )


# ============================================================
# generate_many
# ============================================================

def test_generate_many_returns_correct_count():
    generator = BingoBoardGenerator()

    boards = generator.generate_many(10)

    assert len(boards) == 10


def test_generate_many_returns_boards():
    generator = BingoBoardGenerator()

    boards = generator.generate_many(5)

    assert all(
        isinstance(board, BingoBoard)
        for board in boards
    )


def test_generate_many_requires_int():
    generator = BingoBoardGenerator()

    with pytest.raises(
        TypeError,
        match="count must be an integer",
    ):
        generator.generate_many("5")


def test_generate_many_requires_positive_count():
    generator = BingoBoardGenerator()

    with pytest.raises(
        ValueError,
        match="greater than 0",
    ):
        generator.generate_many(0)


# ============================================================
# RNG injection
# ============================================================

def test_same_rng_seed_generates_same_board():
    generator_1 = BingoBoardGenerator(
        rng=random.Random(42),
    )

    generator_2 = BingoBoardGenerator(
        rng=random.Random(42),
    )

    board_1 = generator_1.generate()
    board_2 = generator_2.generate()

    assert board_1 == board_2


def test_different_rng_seeds_generate_different_boards():
    generator_1 = BingoBoardGenerator(
        rng=random.Random(1),
    )

    generator_2 = BingoBoardGenerator(
        rng=random.Random(2),
    )

    board_1 = generator_1.generate()
    board_2 = generator_2.generate()

    assert board_1 != board_2


# ============================================================
# from_seed
# ============================================================

def test_from_seed_creates_generator():
    generator = BingoBoardGenerator.from_seed(42)

    assert isinstance(
        generator,
        BingoBoardGenerator,
    )


def test_from_seed_requires_int():
    with pytest.raises(
        TypeError,
        match="seed must be an integer",
    ):
        BingoBoardGenerator.from_seed("42")


def test_same_seed_generates_same_board():
    generator_1 = BingoBoardGenerator.from_seed(42)
    generator_2 = BingoBoardGenerator.from_seed(42)

    board_1 = generator_1.generate()
    board_2 = generator_2.generate()

    assert board_1 == board_2


def test_different_seeds_generate_different_boards():
    generator_1 = BingoBoardGenerator.from_seed(1)
    generator_2 = BingoBoardGenerator.from_seed(2)

    board_1 = generator_1.generate()
    board_2 = generator_2.generate()

    assert board_1 != board_2