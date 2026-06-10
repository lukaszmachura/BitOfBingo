# test_binary_converter.py

import pytest

from src.binary_converter import BinaryConverter


# ============================================================
# Factory methods
# ============================================================

def test_from_binary():
    converter = BinaryConverter.from_binary("1010")

    assert converter.binary_string == "1010"
    assert converter.bits == 4


def test_from_binary_with_prefix():
    converter = BinaryConverter.from_binary("0b1010")

    assert converter.binary_string == "1010"
    assert converter.bits == 4


def test_from_binary_invalid_type():
    with pytest.raises(TypeError):
        BinaryConverter.from_binary(1010)


def test_from_binary_empty():
    with pytest.raises(ValueError):
        BinaryConverter.from_binary("")


def test_from_binary_invalid_character():
    with pytest.raises(ValueError):
        BinaryConverter.from_binary("1021")


def test_from_decimal():
    converter = BinaryConverter.from_decimal(10, bits=8)

    assert converter.decimal_value == 10
    assert converter.bits == 8


def test_from_decimal_invalid_type():
    with pytest.raises(TypeError):
        BinaryConverter.from_decimal("10", bits=8)


def test_from_decimal_invalid_bits_type():
    with pytest.raises(TypeError):
        BinaryConverter.from_decimal(10, bits="8")


def test_from_decimal_invalid_bits():
    with pytest.raises(ValueError):
        BinaryConverter.from_decimal(10, bits=0)


# ============================================================
# Decode
# ============================================================

def test_decode_nkb():
    assert (
        BinaryConverter.from_binary("1010").decode_nkb()
        == 10
    )


def test_decode_zm_positive():
    assert (
        BinaryConverter.from_binary("0110").decode_zm()
        == 6
    )


def test_decode_zm_negative():
    assert (
        BinaryConverter.from_binary("1110").decode_zm()
        == -6
    )


def test_decode_u2_positive():
    assert (
        BinaryConverter.from_binary("0110").decode_u2()
        == 6
    )


def test_decode_u2_negative():
    assert (
        BinaryConverter.from_binary("1110").decode_u2()
        == -2
    )


def test_decode_u2_minimum_value():
    assert (
        BinaryConverter.from_binary("1000").decode_u2()
        == -8
    )


def test_decode_u2_maximum_value():
    assert (
        BinaryConverter.from_binary("0111").decode_u2()
        == 7
    )


def test_decode_u1_positive():
    assert (
        BinaryConverter.from_binary("0110").decode_u1()
        == 6
    )


def test_decode_u1_negative():
    assert (
        BinaryConverter.from_binary("1110").decode_u1()
        == -1
    )


def test_decode_standard_bias():
    assert (
        BinaryConverter.from_binary("1000")
        .decode_standard_bias()
        == 1
    )


def test_decode_nuding():
    assert (
        BinaryConverter.from_binary("1111")
        .decode_nuding()
        == 1
    )


# ============================================================
# Encode NKB
# ============================================================

def test_encode_nkb():
    assert (
        BinaryConverter.from_decimal(10, bits=4)
        .encode_nkb()
        == "1010"
    )


def test_encode_nkb_zero():
    assert (
        BinaryConverter.from_decimal(0, bits=4)
        .encode_nkb()
        == "0000"
    )


def test_encode_nkb_maximum():
    assert (
        BinaryConverter.from_decimal(15, bits=4)
        .encode_nkb()
        == "1111"
    )


def test_encode_nkb_overflow():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            16,
            bits=4,
        ).encode_nkb()


def test_encode_nkb_negative():
    with pytest.raises(ValueError):
        BinaryConverter.from_decimal(
            -1,
            bits=4,
        ).encode_nkb()


# ============================================================
# Encode ZM
# ============================================================

def test_encode_zm_positive():
    assert (
        BinaryConverter.from_decimal(6, bits=4)
        .encode_zm()
        == "0110"
    )


def test_encode_zm_negative():
    assert (
        BinaryConverter.from_decimal(-6, bits=4)
        .encode_zm()
        == "1110"
    )


def test_encode_zm_positive_limit():
    assert (
        BinaryConverter.from_decimal(7, bits=4)
        .encode_zm()
        == "0111"
    )


def test_encode_zm_negative_limit():
    assert (
        BinaryConverter.from_decimal(-7, bits=4)
        .encode_zm()
        == "1111"
    )


def test_encode_zm_overflow_positive():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            8,
            bits=4,
        ).encode_zm()


def test_encode_zm_overflow_negative():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            -8,
            bits=4,
        ).encode_zm()


# ============================================================
# Encode U1
# ============================================================

def test_encode_u1_positive():
    assert (
        BinaryConverter.from_decimal(6, bits=4)
        .encode_u1()
        == "0110"
    )


def test_encode_u1_negative():
    assert (
        BinaryConverter.from_decimal(-1, bits=4)
        .encode_u1()
        == "1110"
    )


def test_encode_u1_positive_limit():
    assert (
        BinaryConverter.from_decimal(7, bits=4)
        .encode_u1()
        == "0111"
    )


def test_encode_u1_negative_limit():
    assert (
        BinaryConverter.from_decimal(-7, bits=4)
        .encode_u1()
        == "1000"
    )


def test_encode_u1_overflow():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            -8,
            bits=4,
        ).encode_u1()


# ============================================================
# Encode U2
# ============================================================

def test_encode_u2_positive():
    assert (
        BinaryConverter.from_decimal(6, bits=4)
        .encode_u2()
        == "0110"
    )


def test_encode_u2_negative():
    assert (
        BinaryConverter.from_decimal(-2, bits=4)
        .encode_u2()
        == "1110"
    )


def test_encode_u2_minimum():
    assert (
        BinaryConverter.from_decimal(-8, bits=4)
        .encode_u2()
        == "1000"
    )


def test_encode_u2_maximum():
    assert (
        BinaryConverter.from_decimal(7, bits=4)
        .encode_u2()
        == "0111"
    )


def test_encode_u2_overflow_positive():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            8,
            bits=4,
        ).encode_u2()


def test_encode_u2_overflow_negative():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            -9,
            bits=4,
        ).encode_u2()


# ============================================================
# Bias
# ============================================================

def test_encode_standard_bias():
    assert (
        BinaryConverter.from_decimal(1, bits=4)
        .encode_standard_bias()
        == "1000"
    )


def test_decode_bias():
    assert (
        BinaryConverter.from_binary("1000")
        .decode_bias()
        == 1
    )


def test_encode_custom_bias():
    assert (
        BinaryConverter.from_decimal(5, bits=4)
        .encode_bias(5)
        == "1010"
    )


def test_decode_custom_bias():
    assert (
        BinaryConverter.from_binary("1010")
        .decode_bias(5)
        == 5
    )


def test_bias_overflow():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            20,
            bits=4,
        ).encode_nuding()


# ============================================================
# Wrong source type
# ============================================================

def test_decode_requires_binary():
    converter = BinaryConverter.from_decimal(
        5,
        bits=4,
    )

    with pytest.raises(ValueError):
        converter.decode_u2()


def test_encode_requires_decimal():
    converter = BinaryConverter.from_binary(
        "1110"
    )

    with pytest.raises(ValueError):
        converter.encode_u2()


# ============================================================
# Additional bias representations
# ============================================================

def test_encode_8421():
    assert (
        BinaryConverter.from_decimal(6, bits=4)
        .encode_8421()
        == "1010"
    )


def test_decode_8421():
    assert (
        BinaryConverter.from_binary("1010")
        .decode_8421()
        == 6
    )


def test_encode_stibitz():
    assert (
        BinaryConverter.from_decimal(3, bits=4)
        .encode_stibitz()
        == "1010"
    )


def test_decode_stibitz():
    assert (
        BinaryConverter.from_binary("1010")
        .decode_stibitz()
        == 3
    )


def test_encode_diamond():
    assert (
        BinaryConverter.from_decimal(-68, bits=7)
        .encode_diamond()
        == "1111111"
    )


def test_decode_diamond():
    assert (
        BinaryConverter.from_binary("1111111")
        .decode_diamond()
        == -68
    )


# ============================================================
# Edge cases for custom bias representations
# ============================================================

def test_encode_nuding_upper_limit():
    # bits=4 => bias=14
    # max = 15 - 14 = 1
    assert (
        BinaryConverter.from_decimal(1, bits=4)
        .encode_nuding()
        == "1111"
    )


def test_encode_nuding_lower_limit():
    # bits=4 => bias=14
    # min = -14
    assert (
        BinaryConverter.from_decimal(-14, bits=4)
        .encode_nuding()
        == "0000"
    )


def test_encode_nuding_positive_overflow():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            2,
            bits=4,
        ).encode_nuding()


def test_encode_nuding_negative_overflow():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            -15,
            bits=4,
        ).encode_nuding()


def test_encode_stibitz_upper_limit():
    # bits=4 => bias=7
    # max = 15 - 7 = 8
    assert (
        BinaryConverter.from_decimal(8, bits=4)
        .encode_stibitz()
        == "1111"
    )


def test_encode_stibitz_lower_limit():
    # bits=4 => bias=7
    assert (
        BinaryConverter.from_decimal(-7, bits=4)
        .encode_stibitz()
        == "0000"
    )


def test_encode_stibitz_overflow():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            9,
            bits=4,
        ).encode_stibitz()


def test_encode_8421_upper_limit():
    # bits=4 => bias=4
    # max = 15 - 4 = 11
    assert (
        BinaryConverter.from_decimal(11, bits=4)
        .encode_8421()
        == "1111"
    )


def test_encode_8421_lower_limit():
    assert (
        BinaryConverter.from_decimal(-4, bits=4)
        .encode_8421()
        == "0000"
    )


def test_encode_8421_overflow():
    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            12,
            bits=4,
        ).encode_8421()


def test_encode_diamond_upper_limit():
    bits = 7
    bias = 27 * bits + 6
    maximum = (2 ** bits) - 1 - bias

    assert (
        BinaryConverter.from_decimal(
            maximum,
            bits=bits,
        ).encode_diamond()
        == "1111111"
    )


def test_encode_diamond_lower_limit():
    bits = 7
    bias = 27 * bits + 6

    assert (
        BinaryConverter.from_decimal(
            -bias,
            bits=bits,
        ).encode_diamond()
        == "0000000"
    )


def test_encode_diamond_overflow():
    bits = 7
    bias = 27 * bits + 6
    maximum = (2 ** bits) - 1 - bias

    with pytest.raises(ValueError, match="Overflow"):
        BinaryConverter.from_decimal(
            maximum + 1,
            bits=bits,
        ).encode_diamond()