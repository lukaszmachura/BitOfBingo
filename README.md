# BitOfBingo
![Python](https://img.shields.io/badge/python-3.14%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)
![Tests](https://github.com/lukaszmachura/BitOfBingo/actions/workflows/tests.yml/badge.svg)
<!-- [![codecov](https://codecov.io/gh/lukaszmachura/BitOfBingo/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/BitOfBingo) -->

## BinaryConverter

BinaryConverter is a utility class for converting between decimal integers and binary representations using different encoding schemes commonly used in computer architecture.

It supports both directions of conversion:

- Encoding (decimal → binary)  
- Decoding (binary → decimal)  

### Supported representations

The class implements the following number systems:

- Natural Binary Code (NKB)
- Sign-Magnitude (ZM)
- One's Complement (U1)
- Two's Complement (U2)
- Biased representations:
  - Standard bias
  - 8421 bias
  - Nuding bias
  - Stibitz bias
  - Diamond bias

### Features

- Conversion from binary string to decimal value
- Conversion from decimal value to binary string
- Automatic bit-length handling
- Overflow detection with informative errors
- Support for 0b prefix in binary input
- Strict validation of input data

### Example usage

```python
from binary_converter import BinaryConverter

# Binary → Decimal
value = BinaryConverter.from_binary("1110").decode_u2()
print(value)  # -2

# Decimal → Binary
binary = BinaryConverter.from_decimal(-2, bits=4).encode_u2()
print(binary)  # '1110'
```

### Error handling

The class raises ValueError in case of overflow, for example when a number cannot be represented within the specified bit width:

```python
BinaryConverter.from_decimal(16, bits=4).encode_nkb()
# ValueError: Overflow: 16 cannot be represented using 4 bits...
```

### Design notes

The class is designed for educational purposes for CyberMil project.

### Tests

![Tests](https://github.com/lukaszmachura/BitOfBingo/actions/workflows/tests.yml/badge.svg)