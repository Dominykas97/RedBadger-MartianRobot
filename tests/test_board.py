import unittest

from app import Board

class TestBoard(unittest.TestCase):
    board = Board("input.txt")


    def test_board_init(self):
        self.assertEqual(self.board.x, 5, "X should be 5")
        self.assertEqual(self.board.y, 3, "Y should be 3")


if __name__ == '__main__':
    unittest.main()
