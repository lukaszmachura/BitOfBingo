from binary_converter import BinaryConverter


class BinaryGameConverter:
    """Adapter over existing BinaryConverter."""

    def __init__(self, bits: int = 8):
        self.bits = bits

    def encode(self, value: int, system: str) -> str:
        """Converts decimal value into binary representation."""

        converter = BinaryConverter.from_decimal(value, bits=self.bits)

        if system == "U2":
            return converter.encode_u2()

        if system == "U1":
            return converter.encode_u1()

        if system == "NKB":
            return converter.encode_nkb()

        if system == "ZM":
            return converter.encode_zm()

        if system == "BIAS":
            return converter.encode_bias()

        if system == "STD BIAS":
            return converter.encode_standard_bias()

        if system == "8421":
            return converter.encode_8421()

        if system == "NUDING":
            return converter.encode_nuding()

        if system == "STIBITZ":
            return converter.encode_stibitz()

        if system == "DIAMOND":
            return converter.encode_diamond()

        raise ValueError(f"Unknown system: {system}")