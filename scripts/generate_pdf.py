from bingo.board_generator import BingoBoardGenerator
from bingo.pdf_exporter import BingoPdfExporter


def main() -> None:
    generator = BingoBoardGenerator.from_seed(42)

    # 2 strony A4 = 12 plansz (6 na stronę)
    boards = generator.generate_many(12)

    exporter = BingoPdfExporter()

    exporter.export(
        boards=boards,
        output_path="bingo.pdf",
        backside_pdf="assets/pdf/bingo75_backside.pdf",
    )


if __name__ == "__main__":
    main()