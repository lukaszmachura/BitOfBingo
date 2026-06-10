"""PDF export utilities for bingo boards."""

from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from bingo.board import BingoBoard


class BingoPdfExporter:
    """Exports bingo boards to a printable PDF document.

    Each A4 page contains six bingo boards arranged in a
    2 × 3 layout.

    Optionally, a predefined backside PDF can be inserted
    after every generated front page to support duplex
    printing.
    """

    BOARDS_PER_PAGE = 6

    def export(
        self,
        boards: list[BingoBoard],
        output_path: str | Path,
        backside_pdf: str | Path | None = None,
    ) -> None:
        """Exports boards to a PDF document.

        Args:
            boards: Boards to export.
            output_path: Destination PDF file.
            backside_pdf: Optional PDF template used as the
                reverse side of every generated page.
        """
        output_path = Path(output_path)

        front_pdf = output_path.with_suffix(".front.pdf")

        self._create_front_pages(
            boards=boards,
            output_path=front_pdf,
        )

        if backside_pdf is None:
            front_pdf.replace(output_path)
            return

        self._merge_with_backside(
            front_pdf=front_pdf,
            backside_pdf=Path(backside_pdf),
            output_path=output_path,
        )

        front_pdf.unlink(missing_ok=True)

    def _create_front_pages(
        self,
        boards: list[BingoBoard],
        output_path: Path,
    ) -> None:
        """Creates front pages containing bingo boards."""
        pdf = canvas.Canvas(
            str(output_path),
            pagesize=A4,
        )

        for index in range(
            0,
            len(boards),
            self.BOARDS_PER_PAGE,
        ):
            page_boards = boards[
                index:index + self.BOARDS_PER_PAGE
            ]

            self._draw_page(
                pdf=pdf,
                boards=page_boards,
            )

            pdf.showPage()

        pdf.save()

    def _draw_page(
        self,
        pdf: canvas.Canvas,
        boards: list[BingoBoard],
    ) -> None:
        """Draws a single A4 page."""
        positions = [
            (30, 550),
            (300, 550),
            (30, 290),
            (300, 290),
            (30, 30),
            (300, 30),
        ]

        for board, (x, y) in zip(
            boards,
            positions,
            strict=False,
        ):
            self._draw_board(
                pdf=pdf,
                board=board,
                x=x,
                y=y,
            )

    def _draw_board(
        self,
        pdf: canvas.Canvas,
        board: BingoBoard,
        x: int,
        y: int,
    ) -> None:
        """Draws a single bingo board.

        Placeholder implementation.
        """
        width = 240
        height = 220

        pdf.rect(x, y, width, height)

        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(
            x + 10,
            y + height - 15,
            f"Board #{board.board_id}",
        )

        # TODO:
        # draw 5x5 grid
        # draw values
        # draw CM marker

    def _merge_with_backside(
        self,
        front_pdf: Path,
        backside_pdf: Path,
        output_path: Path,
    ) -> None:
        """Interleaves front pages with backside pages."""
        fronts = PdfReader(str(front_pdf))
        backside = PdfReader(str(backside_pdf))

        if len(backside.pages) != 1:
            raise ValueError(
                "Backside PDF must contain exactly one page."
            )

        writer = PdfWriter()

        template_page = backside.pages[0]

        for page in fronts.pages:
            writer.add_page(page)
            writer.add_page(template_page)

        with output_path.open("wb") as file:
            writer.write(file)