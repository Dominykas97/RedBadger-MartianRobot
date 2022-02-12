import unittest

from app import Board

class TestBoard(unittest.TestCase):
    board = Board("input.txt")


    def test_board_init(self):
        self.assertEqual(self.board.boardX, 5, "boardX should be 5")
        self.assertEqual(self.board.boardY, 3, "boardY should be 3")

    def test_first_robot(self):
        self.board.next()
        self.assertEqual(self.board.x, 1, "X should be 1")
        self.assertEqual(self.board.y, 1, "Y should be 1")
        self.assertEqual(self.board.get_direction(), "E", "Direction should be E")


if __name__ == '__main__':
    unittest.main()
