"""Red Badger Martian Robots exercise solution"""

from typing import Optional

direction_map: dict[int, str] = {
    0: "N",
    1: "E",
    2: "S",
    3: "W",
}
direction_map2: dict[str, int] = {
    "N": 0,
    "E": 1,
    "S": 2,
    "W": 3,
}
BROKEN = "No more instructions"
NON_EXISTANT_DIRECTION = "Can't parse non exsitant direction"


class Board:
    """Martian robot game"""

    lines: list[str] = []
    scents: dict[str, int] = {}

    def __init__(self, filename: str):

        with open(filename, "r", encoding="utf-8") as file:
            lines = file.read().splitlines()
            first_line: list = lines[0].split(" ")
            self.board_x: int = int(first_line[0])
            self.board_y: int = int(first_line[1])
            self.lines: list[str] = lines[1:]
        self.robot_x: int
        self.robot_y: int
        self.direction: int
        self.lost: bool = False

    def get_robot_x(self) -> int:
        """Gets robot's x coordinate."""
        return self.robot_x

    def set_robot_x(self, new_x: int) -> None:
        """Sets robot's x coordinate."""
        self.robot_x = new_x

    def get_robot_y(self) -> int:
        """Gets robot's y coordinate."""
        return self.robot_y

    def set_robot_y(self, new_y: int) -> None:
        """Sets robot's y coordinate."""
        self.robot_y = new_y

    def get_direction(self) -> Optional[str]:
        """Gets robot's direction.
        Possible values: ["N","E","S","W"]."""
        return direction_map.get(self.direction)

    def set_direction(self, new_direction: str) -> None:
        """Sets robot's direction internally as a integer.
        Possible values: [0, 1, 2, 3]."""
        self.direction = direction_map2.get(new_direction, -1)

    def get_status(self) -> str:
        """Gets robot's x, y coordinates and direction as string.
        If the robot got lost, " LOST" will be added to the end
        For example: "1 1 N"."""
        status = f"{self.robot_x} {self.robot_y} {self.get_direction()}"
        if self.lost:
            status += " LOST"
        return status

    def get_next_robot_instructions(self) -> str:
        """Gets next robot movement from file in memory"""

        if len(self.lines) == 0:
            return BROKEN
        first_line = self.lines[0].split(" ")
        self.set_robot_x(int(first_line[0]))
        self.set_robot_y(int(first_line[1]))
        if len(first_line[2]) == 1 and first_line[2] in "NEWS":
            self.set_direction(first_line[2])
        else:
            return NON_EXISTANT_DIRECTION
        movement: str = self.lines[1]
        self.lines = self.lines[3:]
        return movement

    def next(self) -> str:
        """Processes next robot movement"""
        movement: str = self.get_next_robot_instructions()
        if movement in [BROKEN, NON_EXISTANT_DIRECTION]:
            print(movement)
            return movement
        self.lost = False
        # print(f"INIT: {self.get_status()}")

        #  0
        # 3 1
        #  2
        for move in movement:
            scent: bool = True
            if move == "L":
                self.direction = (self.direction + 4 - 1) % 4
            if move == "R":
                self.direction = (self.direction + 1) % 4
            if move == "F":
                if (
                    direction_map.get(self.direction) == "N"
                    and self.robot_y < self.board_y
                ):
                    self.robot_y += 1
                elif direction_map.get(self.direction) == "S" and self.robot_y > 0:
                    self.robot_y -= 1
                elif (
                    direction_map.get(self.direction) == "E"
                    and self.robot_x < self.board_x
                ):
                    self.robot_x += 1
                elif direction_map.get(self.direction) == "W" and self.robot_x > 0:
                    self.robot_x -= 1
                else:
                    scent = self.check_present_scent()

            # print(self.direction)
            # print(move)
            # print(f"{self.x} {self.y} {self.get_direction()}")

            if not scent:
                self.lost = True
                break
        print(self.get_status())
        return self.get_status()

    def check_present_scent(self) -> bool:
        """Checks if scent is present in scents dictionary.
        If not, it is added for future use"""
        if f"{self.robot_x},{self.robot_y}" in self.scents:
            return True
        self.scents[f"{self.robot_x},{self.robot_y}"] = 1
        return False
