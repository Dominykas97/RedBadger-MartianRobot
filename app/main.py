import argparse
from app.board import Board


def main():
    input_file = "input.txt"
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--File", help="Specify input file")

    args = parser.parse_args()

    if args.File:
        input_file = args.File

    board = Board(input_file)
    board.next()
    board.next()
    board.next()


if __name__ == "__main__":
    main()
