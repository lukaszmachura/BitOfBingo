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


# -------------------------
# BINGO CLI
# -------------------------

bingo:
	PYTHONPATH=src $(PYTHON) -m bingo.cli generate --pages 2

bingo-4:
	PYTHONPATH=src $(PYTHON) -m bingo.cli generate --pages 4

bingo-10:
	PYTHONPATH=src $(PYTHON) -m bingo.cli generate --pages 10


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
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf dist
	rm -rf build