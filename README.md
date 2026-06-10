# BitOfBingo

![Python](https://img.shields.io/badge/python-3.14%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)
![Tests](https://github.com/lukaszmachura/BitOfBingo/actions/workflows/tests.yml/badge.svg)

<!-- [![codecov](https://codecov.io/gh/lukaszmachura/BitOfBingo/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/BitOfBingo) -->

---

## 🎲 Bingo Generator (Binary Edition)

This project generates printable bingo boards with a custom binary/decimal gameplay system.

Players use standard bingo boards, while numbers can later be interpreted using binary representations.

---

## 🧱 Core Architecture

### `BingoBoard`

Represents a single bingo board.

- 5×5 grid structure
- center field is always "CM" (free space)
- contains only valid integers within configured range
- immutable board structure
- unique `board_id` for tracking and PDF export

Example:

```python
BingoBoard(
    board_id="000001",
    grid=[
        [12, -5, 44, 1, 33],
        ["CM", "CM", "CM", "CM", "CM"],
        [7, 8, 9, 10, 11],
        [12, 13, 14, 15, 16],
        [17, 18, 19, 20, 21],
    ],
)
```

---

### `BingoBoardGenerator`

Responsible for generating reproducible bingo boards.

This class is the core of the board creation logic and ensures deterministic, validated and configurable board generation.

### Features

- configurable numeric range (`min_value`, `max_value`)
- deterministic generation using `seed`
- reproducible outputs across runs
- ensures 24 unique values per board (5×5 grid with center free space)
- batch generation via `generate_many`
- internal validation of constraints and RNG safety

### Deterministic generation

The generator uses a seeded random engine so identical inputs always produce identical boards.

This is critical for:

- reproducible PDF exports
- testing consistency
- tournament fairness
- debugging

### Example usage

```python
from bingo.board_generator import BingoBoardGenerator

generator = BingoBoardGenerator.from_seed(42)

board = generator.generate()
boards = generator.generate_many(12)
```

---

## ⚙️ Configuration

The system is fully configurable while preserving deterministic behavior.

### Generator configuration

- `seed` → controls randomness
- `min_value` → minimum allowed number
- `max_value` → maximum allowed number

Example:

```python
from bingo.board_generator import BingoBoardGenerator

generator = BingoBoardGenerator.from_seed(
    seed=42,
    min_value=-75,
    max_value=75,
)
```

### Board rules

- 5×5 grid
- center cell is always "CM"
- exactly 24 numeric values per board
- no duplicates within a board
- values constrained to `[min_value, max_value]`

### PDF configuration

Handled by `BingoPdfExporter`:

- `output_path` → output PDF file
- `backside_pdf` → optional reverse page template
- layout fixed to A4 (6 boards per page)

Example:

```python
exporter.export(
    boards=boards,
    output_path="bingo.pdf",
    backside_pdf="assets/pdf/bingo75_backside.pdf",
)
```

### Reproducibility guarantee

Given the same configuration (seed, range), the system always produces identical boards and PDFs.

---

## 🧠 BinaryConverter

`BinaryConverter` is a utility for converting between decimal integers and binary representations using multiple encoding schemes.

### Supported representations

- Natural Binary Code (NKB)
- Sign-Magnitude (ZM)
- One's Complement (U1)
- Two's Complement (U2)
- Biased systems:
  - Standard bias
  - 8421 bias
  - Nuding bias
  - Stibitz bias
  - Diamond bias

### Features

- decimal ↔ binary conversion
- multiple encoding schemes
- automatic bit-width handling
- overflow detection with errors
- support for "0b" prefix input

### Example usage

```python
from binary_converter import BinaryConverter

value = BinaryConverter.from_binary("1110").decode_u2()
print(value)  # -2

binary = BinaryConverter.from_decimal(-2, bits=4).encode_u2()
print(binary)  # "1110"
```

### Error handling

Raises `ValueError` on overflow:

```python
BinaryConverter.from_decimal(16, bits=4).encode_nkb()
# ValueError: Overflow: 16 cannot be represented using 4 bits
```

### Design notes

Educational implementation for CyberMil project.

---

## 🧠 CLI

Generate printable PDFs using Typer CLI:

```bash
bingo generate --pages 2 --seed 42
```

or

```bash
bingo --pages 2 --seed 42
```

### Options

- `--pages` → number of A4 pages
- `--seed` → deterministic generation
- `--out` → output PDF file
- `--min / --max` → numeric range
- `--backside` → reverse page template

---

## 🧪 Testing

Run tests:

```bash
pytest
```

With coverage:

```bash
pytest --cov
```