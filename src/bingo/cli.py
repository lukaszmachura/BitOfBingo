"""CLI for Bingo PDF generator."""

from __future__ import annotations

import typer

from bingo.board_generator import BingoBoardGenerator
from bingo.pdf_exporter import BingoPdfExporter

app = typer.Typer(help="Bingo PDF generator with binary number game.")


#print("CLI MODULE LOADED")
#print("APP CREATED:", app)

@app.command()
def generate(
    seed: int = typer.Option(42, help="Random seed for reproducible output"),
    pages: int = typer.Option(2, help="Number of A4 pages (6 boards per page)"),
    out: str = typer.Option("bingo.pdf", help="Output PDF file"),
    min_value: int = typer.Option(-75, help="Minimum value in board"),
    max_value: int = typer.Option(75, help="Maximum value in board"),
    backside: str = typer.Option(
        "assets/pdf/bingo75_backside.pdf",
        help="Backside PDF template",
    ),
) -> None:
    """Generate Bingo PDF file."""

    generator = BingoBoardGenerator.from_seed(
        seed=seed,
        min_value=min_value,
        max_value=max_value,
    )

    boards = generator.generate_many(pages * 6)

    exporter = BingoPdfExporter()

    exporter.export(
        boards=boards,
        output_path=out,
        backside_pdf=backside,
    )

    typer.echo(f"Generated {pages} pages -> {out}")
