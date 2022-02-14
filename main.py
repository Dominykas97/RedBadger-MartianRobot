import argparse

from app.board import Board
from app.constants import BROKEN


def main():
    input_file = "input.txt"
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--File", help="Specify input file")

    args = parser.parse_args()

    if args.File:
        input_file = args.File

    board = Board(input_file)
    while status := board.next():
        if status == BROKEN:
            break


if __name__ == "__main__":
    main()
