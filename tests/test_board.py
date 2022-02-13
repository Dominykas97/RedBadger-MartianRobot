import unittest

from app.board import Board


class TestBoard(unittest.TestCase):
    board = Board("input.txt")
    board3 = Board("moving_test.txt")

    def test1_board_init(self):
        self.assertEqual(self.board.board_x, 5, "boardX should be 5")
        self.assertEqual(self.board.board_y, 3, "boardY should be 3")

    def test2_first_robot(self):
        status = self.board.next()
        self.assertEqual(self.board.get_robot_x(), 1, "X should be 1")
        self.assertEqual(self.board.get_robot_y(), 1, "Y should be 1")
        self.assertEqual(self.board.get_direction(), "E", "Direction should be E")
        self.assertEqual(status, "1 1 E", " ")

    def test3_second_robot(self):
        status = self.board.next()
        self.assertEqual(self.board.get_robot_x(), 3, "X should be 3")
        self.assertEqual(self.board.get_robot_y(), 3, "Y should be 3")
        self.assertEqual(self.board.get_direction(), "N", "Direction should be N")
        self.assertEqual(status, "3 3 N LOST", " ")

    def test4_third_robot(self):
        status = self.board.next()
        self.assertEqual(self.board.get_robot_x(), 2, "X should be 2")
        self.assertEqual(self.board.get_robot_y(), 3, "Y should be 3")
        self.assertEqual(self.board.get_direction(), "S", "Direction should be S")
        self.assertEqual(status, "2 3 S", " ")

    def test5_nonexistant_robot(self):
        status = self.board.next()
        self.assertEqual(status, "No more instructions", "")

    def test6_nonexistant_direction(self):
        board2 = Board("broken_direction.txt")

        status = board2.next()
        self.assertEqual(status, "Can't parse non exsitant direction", "")

    def test7_movement(self):
        status = self.board3.next()
        self.assertEqual(self.board3.get_robot_x(), 0, "X should be 0")
        self.assertEqual(self.board3.get_robot_y(), 4, "Y should be 4")
        self.assertEqual(self.board3.get_direction(), "N", "Direction should be N")
        self.assertEqual(status, "0 4 N")

    def test8_turn_right(self):
        status = self.board3.next()
        self.assertEqual(self.board3.get_robot_x(), 0, "X should be 0")
        self.assertEqual(self.board3.get_robot_y(), 0, "Y should be 0")
        self.assertEqual(self.board3.get_direction(), "E", "Direction should be E")
        self.assertEqual(status, "0 0 E")

    def test9_turn_left(self):
        status = self.board3.next()
        self.assertEqual(self.board3.get_robot_x(), 0, "X should be 0")
        self.assertEqual(self.board3.get_robot_y(), 0, "Y should be 0")
        self.assertEqual(self.board3.get_direction(), "W", "Direction should be W")
        self.assertEqual(status, "0 0 W")


if __name__ == "__main__":
    unittest.main()
