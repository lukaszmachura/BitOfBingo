.PHONY: install test cov clean pdf run

# ------------------------------------------------------------
# Setup
# ------------------------------------------------------------

install:
	pip install -e .[dev]


# ------------------------------------------------------------
# Tests
# ------------------------------------------------------------

test:
	pytest


cov:
	pytest --cov --cov-report=term-missing


# ------------------------------------------------------------
# Project run (example placeholder)
# ------------------------------------------------------------

run:
	python -m bingo.pdf_exporter


# ------------------------------------------------------------
# PDF generation shortcut (docelowo rozbudujesz)
# ------------------------------------------------------------

pdf:
	python -c "from bingo.board_generator import BingoBoardGenerator; from bingo.pdf_exporter import BingoPdfExporter; \
gen = BingoBoardGenerator.from_seed(42); boards = gen.generate_many(12); \
BingoPdfExporter().export(boards, 'bingo.pdf', backside_pdf='assets/pdf/bingo75_backside.pdf')"


# ------------------------------------------------------------
# Cleanup
# ------------------------------------------------------------

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf dist
	rm -rf build
	find . -type d -name "__pycache__" -exec rm -rf {} +