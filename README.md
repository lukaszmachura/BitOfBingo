![Python](https://img.shields.io/badge/python-3.14%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-in%20development-yellow.svg)
![Tests](https://github.com/lukaszmachura/BitOfBingo/actions/workflows/tests.yml/badge.svg)
<!-- [![codecov](https://codecov.io/gh/lukaszmachura/BitOfBingo/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/BitOfBingo) -->

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 450" width="220" height="auto">
  <defs>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3A86FF" />
      <stop offset="100%" stop-color="#0056B3" />
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#70E000" />
      <stop offset="100%" stop-color="#005F73" />
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0056B3" />
      <stop offset="100%" stop-color="#005F73" />
    </linearGradient>
    <filter id="dropShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#001524" flood-opacity="0.15" />
    </filter>
  </defs>
  <style>
    .stroke-weight { stroke-width: 12; stroke-linecap: round; stroke-linejoin: round; }
    .white-stroke { stroke: #FFFFFF; }
    .text-main { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 900; text-anchor: middle; }
    .text-number { font-family: 'Courier New', monospace; font-weight: bold; fill: #FFFFFF; font-size: 34px; text-anchor: middle; }
  </style>
  <g filter="url(#dropShadow)">
    <path d="M 130,70 A 65,65 0 0,1 270,70 A 55,55 0 0,1 325,120 A 55,55 0 0,1 280,215 L 325,215 A 15,15 0 0,1 340,230 L 340,400 A 20,20 0 0,1 320,420 L 80,420 A 20,20 0 0,1 60,400 L 60,230 A 15,15 0 0,1 75,215 L 120,215 A 55,55 0 0,1 75,120 A 55,55 0 0,1 130,70 Z" fill="#FFFFFF" />
  </g>
  <g transform="translate(0, 5)">
    <path d="M 200,85 A 45,45 0 0,0 155,100 A 40,40 0 0,0 120,135 A 35,35 0 0,0 135,185 A 40,40 0 0,0 200,200 Z" fill="url(#blueGrad)" />
    <path d="M 200,85 A 45,45 0 0,1 245,100 A 40,40 0 0,1 280,135 A 35,35 0 0,1 265,185 A 40,40 0 0,1 200,200 Z" fill="url(#greenGrad)" />
    <line x1="200" y1="85" x2="200" y2="200" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" />
    <path d="M 160,115 A 15,15 0 0,0 145,135" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.6" stroke-linecap="round"/>
    <path d="M 175,175 A 20,20 0 0,1 150,160" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.6" stroke-linecap="round"/>
    <path d="M 240,115 A 15,15 0 0,1 255,135" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.6" stroke-linecap="round"/>
    <path d="M 225,175 A 20,20 0 0,0 250,160" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.6" stroke-linecap="round"/>
    <text x="165" y="152" class="text-number">01</text>
    <text x="235" y="152" class="text-number">26</text>
  </g>
  <path d="M 80,230 A 10,10 0 0,1 90,220 L 310,220 A 10,10 0 0,1 320,230 L 320,395 A 15,15 0 0,1 305,410 L 95,410 A 15,15 0 0,1 80,395 Z" fill="url(#textGrad)" />
  <text x="200" y="285" class="text-main" font-size="46" fill="#FFFFFF">Bit of</text>
  <text x="200" y="375" class="text-main" font-size="72" fill="#FFFFFF" letter-spacing="1">BINGO</text>
  <circle cx="105" cy="245" r="5" fill="#70E000" />
  <circle cx="295" cy="245" r="5" fill="#3A86FF" />
</svg>

# Bit Of Bingo
Bit Of Bingo Game is an educational application designed as a playful blend of a classroom tool and a bingo-style game. While its core purpose is to support learning of binary number representations, it does so in a deliberately game-like and engaging format.

At its heart, this is a **bingo-inspired learning system** that encourages students to actively “decode” numbers from different binary representation systems into decimal values found on printed cards. This constant switching between representations is intended to keep the brain engaged and active.

The system includes:
- 9 different binary representation systems (natural binary code, U1, U2, sign-magnitude, standrd bias, 8421, NUDING, STIBITZ, DIAMOND)
- a module for generating printable A4 bingo sheets (6 boards per page) along with reference formulas for binary-to-decimal conversion
- a random number generation module (like in Bingo) combined with a web-based presentation layer (Streamlit) for classroom use
- a structured workflow for projecting tasks, revealing answers, and moving quickly between exercises

The application is designed not only for teaching, but also for creating a competitive and engaging classroom atmosphere. Teachers are strongly encouraged to introduce small rewards or prizes for students to increase motivation and turn learning into a game-like experience.


## 🚀 Quick Start

### Installation

```bash
pip install -e .
```

### Generate 2 pages PDF and save to `bingo.pdf`

```bash
bingo
```

### Generate 4 pages PDF and save to `bingo.pdf`

```bash
bingo generate --pages 4
```

### Generate 10 pages PDF and save to `bingo_10_pages.pdf`

```bash
bingo generate --pages 10 --out bingo_10_pages.pdf
```

### Start Bingo Lotery via WEB APP
```bash
make game
```
and now go to http://localhost:8501/ to see your game

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
        [-13, 9, 0, -1, 74],
        [7, 8, "CM", 10, 11],
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


## 🎓 Classroom / Presentation Mode

The Binary Game includes a presentation mode designed for classroom use or projection on a screen.

### 🧠 Purpose

This mode enables:
- random generation of a decimal value and encoding system
- large, high-visibility binary representation display
- controlled reveal of the decimal value (DEC)
- fast navigation to the next task

---

### 📺 UI (Presentation Mode)

In Streamlit presentation mode, the interface displays:

- the selected number system (e.g. `U2`, `NKB`, `ZM`, `Standard BIAS`, `Nuding`, `Diamond`, `Stibitz`, `8421`)
- the binary representation (large and readable format)
- control buttons:
  - Show Answer — reveals the decimal value
  - Next — generates a new task

---

### Presentation Styling (Large Display Mode)

For classroom projection, it is recommended to increase font sizes:

```python
st.markdown(
    """
    <style>
    .stCode {
        font-size: 36px !important;
        line-height: 1.4;
    }

    code {
        font-size: 36px !important;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)
```

#### Recommended Presentation Settings

* font size: 30–40px (binary display)
* fullscreen browser mode
* minimal UI distractions (hide sidebar if needed)
* one task per screen

⸻

###  Typical Classroom Flow

1. The teacher starts the application
2. The system generates:
    * a binary representation of a random decimal number
    * a number system encoding
3. Students analyze the binary representation
4. Clicking Show DEC reveals the correct answer
5. Clicking Next moves to the next task