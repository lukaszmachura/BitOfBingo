import pytest

from bingo.board import BingoBoard


def valid_grid():
    """Returns a valid bingo board grid."""
    return [
        [-12, 5, 44, 61, -33],
        [17, -1, 70, -22, 11],
        [3, 50, "CM", -45, 28],
        [10, -8, 19, 72, -60],
        [-75, 32, 14, -17, 75],
    ]


# ============================================================
# Construction
# ============================================================

def test_create_valid_board():
    board = BingoBoard(board_id="test", grid=valid_grid())

    assert board.grid == valid_grid()


def test_board_size_property():
    board = BingoBoard(board_id="test", grid=valid_grid())

    assert board.size == 5


def test_as_rows():
    board = BingoBoard(board_id="test", grid=valid_grid())

    assert board.as_rows() == valid_grid()


# ============================================================
# Structure validation
# ============================================================

def test_too_few_rows():
    grid = valid_grid()[:-1]

    with pytest.raises(
        ValueError,
        match="exactly 5 rows",
    ):
        BingoBoard(board_id="test", grid=grid)


def test_too_many_rows():
    grid = valid_grid()
    grid.append([1, 2, 3, 4, 5])

    with pytest.raises(
        ValueError,
        match="exactly 5 rows",
    ):
        BingoBoard(board_id="test", grid=grid)


def test_row_too_short():
    grid = valid_grid()
    grid[0] = [1, 2, 3, 4]

    with pytest.raises(
        ValueError,
        match="exactly 5 values",
    ):
        BingoBoard(board_id="test", grid=grid)


def test_row_too_long():
    grid = valid_grid()
    grid[0] = [1, 2, 3, 4, 5, 6]

    with pytest.raises(
        ValueError,
        match="exactly 5 values",
    ):
        BingoBoard(board_id="test", grid=grid)


# ============================================================
# Center marker validation
# ============================================================

def test_missing_center_marker():
    grid = valid_grid()
    grid[2][2] = 0

    with pytest.raises(
        ValueError,
        match="center field",
    ):
        BingoBoard(board_id="test", grid=grid)


def test_wrong_center_marker():
    grid = valid_grid()
    grid[2][2] = "FREE"

    with pytest.raises(
        ValueError,
        match="center field",
    ):
        BingoBoard(board_id="test", grid=grid)


# ============================================================
# Value validation
# ============================================================

def test_non_integer_value():
    grid = valid_grid()
    grid[0][0] = "abc"

    with pytest.raises(
        TypeError,
        match="integers",
    ):
        BingoBoard(board_id="test", grid=grid)


def test_value_below_range():
    grid = valid_grid()
    grid[0][0] = -76

    with pytest.raises(
        ValueError,
        match=r"\[-75, 75\]",
    ):
        BingoBoard(board_id="test", grid=grid)


def test_value_above_range():
    grid = valid_grid()
    grid[0][0] = 76

    with pytest.raises(
        ValueError,
        match=r"\[-75, 75\]",
    ):
        BingoBoard(board_id="test", grid=grid)


def test_range_limits_are_allowed():
    grid = valid_grid()
    grid[0][0] = -75
    grid[4][4] = 75

    board = BingoBoard(board_id="test", grid=grid)

    assert board.grid[0][0] == -75
    assert board.grid[4][4] == 75


# ============================================================
# String representation
# ============================================================

def test_string_representation_contains_cm():
    board = BingoBoard(board_id="test", grid=valid_grid())

    output = str(board)

    assert "CM" in output


def test_string_representation_contains_numbers():
    board = BingoBoard(board_id="test", grid=valid_grid())

    output = str(board)

    assert "-12" in output
    assert "75" in output


def test_repr_uses_dataclass_default():
    board = BingoBoard(board_id="test", grid=valid_grid())

    assert "BingoBoard" in repr(board)

