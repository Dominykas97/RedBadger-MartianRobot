import unittest

from app import Board

class TestBoard(unittest.TestCase):
    board = Board("input.txt")


    def test_board_init(self):
        self.assertEqual(self.board.boardX, 5, "boardX should be 5")
        self.assertEqual(self.board.boardY, 3, "boardY should be 3")

    def test_first_robot(self):
        status = self.board.next()
        self.assertEqual(self.board.get_x(), 1, "X should be 1")
        self.assertEqual(self.board.get_y(), 1, "Y should be 1")
        self.assertEqual(self.board.get_direction(), "E", "Direction should be E")
        self.assertEqual(status, "1 1 E", " ")

    def test_second_robot(self):
        status = self.board.next()
        self.assertEqual(self.board.get_x(), 3, "X should be 3")
        self.assertEqual(self.board.get_y(), 3, "Y should be 3")
        self.assertEqual(self.board.get_direction(), "N", "Direction should be N")
        self.assertEqual(status, "3 3 N LOST", " ")

    def test_third_robot(self):
        status = self.board.next()
        self.assertEqual(self.board.get_x(), 2, "X should be 2")
        self.assertEqual(self.board.get_y(), 3, "Y should be 3")
        self.assertEqual(self.board.get_direction(), "S", "Direction should be S")
        self.assertEqual(status, "2 3 S", " ")

if __name__ == '__main__':
    unittest.main()
