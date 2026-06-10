"""Binary number conversion utilities."""

from __future__ import annotations


class BinaryConverter:
    """Converts between decimal integers and binary representations.

    Examples:
        >>> BinaryConverter.from_binary("1110").decode_u2()
        -2

        >>> BinaryConverter.from_decimal(-2, bits=4).encode_u2()
        '1110'
    """

    def __init__(
        self,
        binary_string: str | None = None,
        decimal_value: int | None = None,
        bits: int | None = None,
    ) -> None:
        self.binary_string = binary_string
        self.decimal_value = decimal_value
        self.bits = bits

    # ------------------------------------------------------------------
    # Factory methods
    # ------------------------------------------------------------------

    @classmethod
    def from_binary(cls, binary_string: str) -> "BinaryConverter":
        """Creates a converter from a binary string.

        Args:
            binary_string: Binary number with or without a ``0b`` prefix.

        Returns:
            A configured converter instance.

        Raises:
            TypeError: If binary_string is not a string.
            ValueError: If binary_string is empty or invalid.
        """
        if not isinstance(binary_string, str):
            raise TypeError("binary_string must be a string")

        if binary_string.startswith("0b"):
            binary_string = binary_string[2:]

        if not binary_string:
            raise ValueError("binary_string cannot be empty")

        if any(bit not in {"0", "1"} for bit in binary_string):
            raise ValueError(
                "binary_string must contain only '0' and '1'"
            )

        return cls(
            binary_string=binary_string,
            bits=len(binary_string),
        )

    @classmethod
    def from_decimal(
        cls,
        decimal_value: int,
        bits: int,
    ) -> "BinaryConverter":
        """Creates a converter from a decimal integer.

        Args:
            decimal_value: Decimal value to encode.
            bits: Number of bits.

        Returns:
            A configured converter instance.

        Raises:
            TypeError: If arguments have invalid types.
            ValueError: If bits is not positive.
        """
        if not isinstance(decimal_value, int):
            raise TypeError("decimal_value must be an integer")

        if not isinstance(bits, int):
            raise TypeError("bits must be an integer")

        if bits <= 0:
            raise ValueError("bits must be greater than 0")

        return cls(
            decimal_value=decimal_value,
            bits=bits,
        )

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------

    def _require_binary(self) -> None:
        if self.binary_string is None:
            raise ValueError(
                "This operation requires a binary source."
            )

    def _require_decimal(self) -> None:
        if self.decimal_value is None:
            raise ValueError(
                "This operation requires a decimal source."
            )

    def _check_unsigned_range(self) -> None:
        max_value = (1 << self.bits) - 1

        if not 0 <= self.decimal_value <= max_value:
            raise ValueError(
                f"Overflow: {self.decimal_value} cannot be represented "
                f"using {self.bits} bits in an unsigned representation "
                f"(valid range: 0..{max_value})."
            )

    def _check_sign_magnitude_range(self) -> None:
        min_value = -(2 ** (self.bits - 1) - 1)
        max_value = 2 ** (self.bits - 1) - 1

        if not min_value <= self.decimal_value <= max_value:
            raise ValueError(
                f"Overflow: {self.decimal_value} cannot be represented "
                f"using {self.bits} bits in sign-magnitude format "
                f"(valid range: {min_value}..{max_value})."
            )

    def _check_ones_complement_range(self) -> None:
        min_value = -(2 ** (self.bits - 1) - 1)
        max_value = 2 ** (self.bits - 1) - 1

        if not min_value <= self.decimal_value <= max_value:
            raise ValueError(
                f"Overflow: {self.decimal_value} cannot be represented "
                f"using {self.bits} bits in one's complement format "
                f"(valid range: {min_value}..{max_value})."
            )

    def _check_twos_complement_range(self) -> None:
        min_value = -(2 ** (self.bits - 1))
        max_value = 2 ** (self.bits - 1) - 1

        if not min_value <= self.decimal_value <= max_value:
            raise ValueError(
                f"Overflow: {self.decimal_value} cannot be represented "
                f"using {self.bits} bits in two's complement format "
                f"(valid range: {min_value}..{max_value})."
            )

    def _check_bias_range(self, bias: int) -> None:
        min_value = -bias
        max_value = (1 << self.bits) - 1 - bias

        if not min_value <= self.decimal_value <= max_value:
            raise ValueError(
                f"Overflow: {self.decimal_value} cannot be represented "
                f"using {self.bits} bits with bias={bias} "
                f"(valid range: {min_value}..{max_value})."
            )

    # ------------------------------------------------------------------
    # Binary helpers
    # ------------------------------------------------------------------

    def _msb(self) -> int:
        return int(self.binary_string[0])

    def _unsigned_without_msb(self) -> int:
        value = 0

        for index, bit in enumerate(self.binary_string[:0:-1]):
            value += int(bit) * (2**index)

        return value

    # ------------------------------------------------------------------
    # Decode (binary -> decimal)
    # ------------------------------------------------------------------

    def decode_nkb(self) -> int:
        """Decodes natural binary code."""
        self._require_binary()

        return (
            self._msb() * 2 ** (self.bits - 1)
            + self._unsigned_without_msb()
        )

    def decode_zm(self) -> int:
        """Decodes sign-magnitude representation."""
        self._require_binary()

        return (
            (-1) ** self._msb()
        ) * self._unsigned_without_msb()

    def decode_u2(self) -> int:
        """Decodes two's complement representation."""
        self._require_binary()

        return (
            -self._msb() * 2 ** (self.bits - 1)
            + self._unsigned_without_msb()
        )

    def decode_u1(self) -> int:
        """Decodes one's complement representation."""
        self._require_binary()

        return self.decode_u2() + self._msb()

    def decode_bias(self, bias: int | None = None) -> int:
        """Decodes a biased representation."""
        self._require_binary()

        if bias is None:
            bias = 2 ** (self.bits - 1) - 1

        return self.decode_nkb() - bias

    def decode_standard_bias(self) -> int:
        return self.decode_bias()

    def decode_8421(self) -> int:
        return self.decode_bias(self.bits)

    def decode_nuding(self) -> int:
        return self.decode_bias(3 * self.bits + 2)

    def decode_stibitz(self) -> int:
        return self.decode_bias(self.bits + 3)

    def decode_diamond(self) -> int:
        return self.decode_bias(27 * self.bits + 6)

    # ------------------------------------------------------------------
    # Encode (decimal -> binary)
    # ------------------------------------------------------------------

    def encode_nkb(self) -> str:
        """Encodes as natural binary code."""
        self._require_decimal()
        self._check_unsigned_range()

        return format(
            self.decimal_value,
            f"0{self.bits}b",
        )

    def encode_zm(self) -> str:
        """Encodes as sign-magnitude representation."""
        self._require_decimal()
        self._check_sign_magnitude_range()

        sign = "1" if self.decimal_value < 0 else "0"

        magnitude = format(
            abs(self.decimal_value),
            f"0{self.bits - 1}b",
        )

        return sign + magnitude

    def encode_u1(self) -> str:
        """Encodes as one's complement representation."""
        self._require_decimal()
        self._check_ones_complement_range()

        if self.decimal_value >= 0:
            return format(
                self.decimal_value,
                f"0{self.bits}b",
            )

        positive = format(
            abs(self.decimal_value),
            f"0{self.bits}b",
        )

        return "".join(
            "1" if bit == "0" else "0"
            for bit in positive
        )

    def encode_u2(self) -> str:
        """Encodes as two's complement representation."""
        self._require_decimal()
        self._check_twos_complement_range()

        value = self.decimal_value

        if value < 0:
            value = (1 << self.bits) + value 

        return format(
            value,
            f"0{self.bits}b",
        )

    def encode_bias(self, bias: int | None = None) -> str:
        """Encodes using a biased representation."""
        self._require_decimal()

        if bias is None:
            bias = 2 ** (self.bits - 1) - 1

        self._check_bias_range(bias)

        encoded = self.decimal_value + bias

        return format(
            encoded,
            f"0{self.bits}b",
        )

    def encode_standard_bias(self) -> str:
        return self.encode_bias()

    def encode_8421(self) -> str:
        return self.encode_bias(self.bits)

    def encode_nuding(self) -> str:
        return self.encode_bias(3 * self.bits + 2)

    def encode_stibitz(self) -> str:
        return self.encode_bias(self.bits + 3)

    def encode_diamond(self) -> str:
        return self.encode_bias(27 * self.bits + 6)