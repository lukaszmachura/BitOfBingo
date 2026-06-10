# OLD CODE --- IGNORE ---
# === This module defines the `Binary` class for representing binary numbers in various encoding schemes, along with utility functions for bit manipulation. ===
# The `Binary` class provides methods to convert binary strings to decimal values based on different binary representations, such as sign-magnitude, one's complement, two's complement, and biased representations. The module also includes functions for inverting binary bits and padding binary strings to 8 bits.

class Binary:
    """Represents a binary number in various binary encoding schemes.

    The class stores a binary string (optionally provided with a ``0b`` prefix)
    and provides methods for converting it to decimal values interpreted using
    different binary representations, such as sign-magnitude, one's complement,
    two's complement, and biased representations.

    Args:
        binary_string: Binary number represented as a string.

    Raises:
        AssertionError: If the input is not a string or is empty.
    """

    def __init__(self, binary_string: str):
        self.binary_string = binary_string
        self.bit_length = len(self.binary_string)

    @property
    def binary_string(self) -> str:
        """Returns the stored binary string."""
        return self.__binary_string

    @binary_string.setter
    def binary_string(self, value: str) -> None:
        """Sets and validates the binary string.

        Args:
            value: Binary string with or without the ``0b`` prefix.

        Raises:
            TypeError: If value is not a string.
            ValueError: If the resulting string is empty.
        """
        if not isinstance(value, str):
            raise TypeError("binary_string must be a string")

        if value.startswith("0b"):
            value = value[2:]

        if not value:
            raise ValueError("binary string cannot be empty")
        
        if any(bit not in {"0", "1"} for bit in value):
            raise ValueError("binary_string must contain only '0' and '1'")

        self.__binary_string = value


    @property
    def bit_length(self) -> int:
        """Returns the number of bits."""
        return self.__bit_length

    @bit_length.setter
    def bit_length(self, value: int) -> None:
        """Sets and validates the bit length.

        Args:
            value: Number of bits.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not positive.
        """
        if not isinstance(value, int):
            raise TypeError("bit_length must be an integer")

        if value <= 0:
            raise ValueError("bit_length must be greater than 0")

        self.__bit_length = value

    def most_significant_bit(self) -> int:
        """Returns the most significant bit (MSB).

        Returns:
            The first bit of the binary number as an integer.
        """
        return int(self.binary_string[0])

    def __str__(self) -> str:
        return self.binary_string

    def __repr__(self) -> str:
        return str(self)

    def _unsigned_value_without_msb(self) -> int:
        """Converts all bits except the MSB to an unsigned integer.

        Returns:
            Decimal value represented by all bits except the MSB.
        """
        value = 0

        for i, bit in enumerate(self.binary_string[:0:-1]):
            value += int(bit) * 2**i

        return value

    def from_nkb(self) -> int:
        """Converts from natural binary code (NKB).

        Returns:
            Decimal representation of the binary number.
        """
        return (
            self.most_significant_bit() * 2 ** (self.bit_length - 1)
            + self._unsigned_value_without_msb()
        )

    def from_zm(self) -> int:
        """Converts from sign-magnitude representation.

        Returns:
            Decimal value interpreted as sign-magnitude.
        """
        return (-1) ** self.most_significant_bit() * self._unsigned_value_without_msb()

    def from_u1(self) -> int:
        """Converts from one's complement representation.

        Returns:
            Decimal value interpreted as one's complement.
        """
        return self.from_u2() + self.most_significant_bit()

    def from_u2(self) -> int:
        """Converts from two's complement representation.

        Returns:
            Decimal value interpreted as two's complement.
        """
        return (
            -self.most_significant_bit() * 2 ** (self.bit_length - 1)
            + self._unsigned_value_without_msb()
        )

    def from_bias(self, bias: int | None = None) -> int:
        """Converts from a biased representation.

        Args:
            bias: Bias value. If omitted, the standard bias
                ``2^(n-1) - 1`` is used.

        Returns:
            Decimal value after removing the bias.

        Raises:
            TypeError: If bias is not an integer.
        """
        if bias is None:
            bias = 2 ** (self.bit_length - 1) - 1
        elif not isinstance(bias, int):
            raise TypeError("bias must be an integer")

        return self.from_nkb() - bias

    def from_standard_bias(self) -> int:
        """Converts from the standard biased representation.

        Returns:
            Decimal value.
        """
        return self.from_bias()

    def from_8421(self) -> int:
        """Converts from the 8421 excess representation.

        Returns:
            Decimal value.
        """
        return self.from_bias(self.bit_length)

    def from_nuding(self) -> int:
        """Converts from the Nuding representation.

        Returns:
            Decimal value.
        """
        return self.from_bias(3 * self.bit_length + 2)

    def from_stibitz(self) -> int:
        """Converts from the Stibitz representation.

        Returns:
            Decimal value.
        """
        return self.from_bias(self.bit_length + 3)

    def from_diamond(self) -> int:
        """Converts from the Diamond representation.

        Returns:
            Decimal value.
        """
        return self.from_bias(27 * self.bit_length + 6)


def invert_binary_bits(binary_str: str) -> str:
    """Returns the bitwise inversion of a binary number.

    The function accepts a binary string with or without the ``0b`` prefix,
    pads it to 8 bits, and flips each bit (0 → 1, 1 → 0).

    Args:
        binary_str: Binary number represented as a string.

    Returns:
        An 8-bit binary string with inverted bits.
    """
    if binary_str.startswith("0b"):
        binary_str = binary_str[2:]

    binary_str = to_8_bits(binary_str)
    return "".join("1" if bit == "0" else "0" for bit in binary_str)


def to_8_bits(binary_str: str) -> str:
    """Pads a binary string to 8 bits."""
    while len(binary_str) < 8:
        binary_str = '0' + binary_str
    return binary_str