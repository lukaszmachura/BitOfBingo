PYTHON=python
PIP=pip
STREAMLIT=streamlit

APP=src/binary_game/ui/app.py


# -------------------------
# SETUP
# -------------------------

install:
	$(PIP) install -e .

dev:
	$(PIP) install -e ".[dev]"


# -------------------------
# RUN APP (STREAMLIT)
# -------------------------

run:
	PYTHONPATH=src $(STREAMLIT) run $(APP)

ui:
	PYTHONPATH=src $(STREAMLIT) run $(APP)

game:
	PYTHONPATH=src $(STREAMLIT) run $(APP)

# -------------------------
# BINGO CLI
# -------------------------

bingo:
	PYTHONPATH=src $(PYTHON) -m bingo.cli generate --pages 2
	bingo --pages 2

bingo-4:
	PYTHONPATH=src $(PYTHON) -m bingo.cli generate --pages 4

bingo-10:
	PYTHONPATH=src $(PYTHON) -m bingo.cli generate --pages 10 --seed $RANDOM --out bingo_10_pages.pdf

bingo-cyber:
	PYTHONPATH=src $(PYTHON) -m bingo.cli generate --pages 30 --seed $RANDOM --out bingoCM2026.pdf

# -------------------------
# TESTS
# -------------------------

test:
	PYTHONPATH=src pytest -q

test-v:
	PYTHONPATH=src pytest -vv


# -------------------------
# COVERAGE (optional)
# -------------------------

coverage:
	PYTHONPATH=src pytest --cov=src --cov-report=term-missing


# -------------------------
# CLEAN
# -------------------------

clean:
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf src/binary_game/__pycache__
	rm -rf src/binary_game/core/__pycache__
	rm -rf src/bingo/__pycache__
	rm -rf tests/__pycache__
	rm -rf tests/.pytest_cache
	rm -rf old/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf dist
	rm -rf build
	rm -rf src/*.egg-info
	rm -rf .mypy_cache
	rm bingo.pdf
	streamlit cache clear