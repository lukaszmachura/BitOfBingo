
import pytest
from binums import Binary, to_8_bits, invert_binary_bits


def test_invert_binary_bits():
    assert invert_binary_bits("0b1010") == "11110101"
    assert invert_binary_bits("1010") == "11110101"
    assert invert_binary_bits("00000000") == "11111111"
    assert invert_binary_bits("11111111") == "00000000"


def test_to_8_bits():
    assert to_8_bits("1010") == "00001010"
    assert to_8_bits("11111111") == "11111111"
    assert to_8_bits("00000000") == "00000000"


def test_initialization():
    binary = Binary("1010")

    assert binary.binary_string == "1010"
    assert binary.bit_length == 4


def test_initialization_with_0b_prefix():
    binary = Binary("0b1010")

    assert binary.binary_string == "1010"
    assert binary.bit_length == 4


def test_binary_string_must_be_string():
    with pytest.raises(TypeError):
        Binary(1010)


def test_binary_string_cannot_be_empty():
    with pytest.raises(ValueError):
        Binary("")


def test_binary_string_must_contain_only_bits():
    with pytest.raises(ValueError):
        Binary("1021")


def test_str():
    binary = Binary("1010")

    assert str(binary) == "1010"


def test_repr():
    binary = Binary("1010")

    assert repr(binary) == "1010"


def test_most_significant_bit_zero():
    binary = Binary("0110")

    assert binary.most_significant_bit() == 0


def test_most_significant_bit_one():
    binary = Binary("1110")

    assert binary.most_significant_bit() == 1


def test_from_nkb():
    binary = Binary("10011001")

    assert binary.from_nkb() == 153


def test_from_zm_positive():
    binary = Binary("01100110")

    assert binary.from_zm() == 102


def test_from_zm_negative():
    binary = Binary("10011001")

    assert binary.from_zm() == -25


def test_from_u2_positive():
    binary = Binary("01100110")

    assert binary.from_u2() == 102


def test_from_u2_negative():
    binary = Binary("1110")

    assert binary.from_u2() == -2


def test_from_u1_positive():
    binary = Binary("01100110")

    assert binary.from_u1() == 102


def test_from_u1_negative():
    binary = Binary("1110")

    assert binary.from_u1() == -1


def test_from_bias_default():
    binary = Binary("01100110")

    assert binary.from_bias() == -25


def test_from_bias_custom():
    binary = Binary("01100110")

    assert binary.from_bias(5) == 97


def test_from_bias_requires_integer():
    binary = Binary("01100110")

    with pytest.raises(TypeError):
        binary.from_bias("5")


def test_from_standard_bias():
    binary = Binary("01100110")

    assert binary.from_standard_bias() == -25


def test_from_8421():
    binary = Binary("01100110")

    assert binary.from_8421() == 94


def test_from_nuding():
    binary = Binary("01100110")

    assert binary.from_nuding() == 76


def test_from_stibitz():
    binary = Binary("10011001")

    assert binary.from_stibitz() == 142


def test_from_diamond():
    binary = Binary("10011001")

    assert binary.from_diamond() == -69