"""Red Badger Martian Robots exercise solution"""


class Board():
    """Martian robot game"""
    lines = []
    direction_map = {
        0: "N",
        1: "E",
        2: "S",
        3: "W",
    }
    direction_map2 = {
        "N": 0,
        "E": 1,
        "S": 2,
        "W": 3,
    }
    scents = {}

    def __init__(self, filename):

        with open(filename, "r", encoding='utf-8') as file:
            lines = file.read().splitlines()
            first_line = lines[0].split(" ")
            self.board_x = int(first_line[0])
            self.board_y = int(first_line[1])
            self.lines = lines[1:]
        self.robot_x = None
        self.robot_y = None
        self.direction = None

    def get_robot_x(self):
        """Gets robot's x coordinate."""
        return self.robot_x

    def set_robot_x(self, new_x):
        """Sets robot's x coordinate."""
        self.robot_x = new_x

    def get_robot_y(self):
        """Gets robot's y coordinate."""
        return self.robot_y

    def set_robot_y(self, new_y):
        """Sets robot's y coordinate."""
        self.robot_y = new_y

    def get_direction(self):
        """Gets robot's direction. Possible values: ["N","E","S","W"]."""
        return self.direction_map.get(self.direction)

    def set_direction(self, new_direction):
        """Sets robot's direction as a integer. Possible values: [0, 1, 2, 3]."""
        self.direction = self.direction_map2.get(new_direction)

    def get_status(self):
        """Gets robot's x, y coordinates and direction as string. For example: "1 1 N"."""
        return f"{self.robot_x} {self.robot_y} {self.get_direction()}"

    def get_next_robot_instructions(self):
        """Gets next robot movement from file in memory"""

        if len(self.lines) == 0:
            print("No more instructions")
            return "No more instructions"
        first_line = self.lines[0].split(" ")
        self.set_robot_x(int(first_line[0]))
        self.set_robot_y(int(first_line[1]))
        self.set_direction(first_line[2])
        movement = self.lines[1]
        self.lines = self.lines[3:]
        return movement

    def next(self):
        """Processes next robot movement"""
        movement = self.get_next_robot_instructions()
        if movement == "No more instructions":
            return movement
        # print(f"INIT: {self.get_status()}")

        #  0
        # 3 1
        #  2
        for move in movement:
            if move == "L":
                self.direction = (self.direction + 4 - 1) % 4
            if move == "R":
                self.direction = (self.direction + 1) % 4
            scent = -1
            if move == "F":
                if self.direction_map.get(
                        self.direction) == "N" and self.robot_y < self.board_y:
                    self.robot_y += 1
                elif self.direction_map.get(
                        self.direction) == "S" and self.robot_y > 0:
                    self.robot_y -= 1
                elif self.direction_map.get(
                        self.direction) == "E" and self.robot_x < self.board_x:
                    self.robot_x += 1
                elif self.direction_map.get(
                        self.direction) == "W" and self.robot_x > 0:
                    self.robot_x -= 1
                else:
                    scent = self.check_present_scent()

            # print(self.direction)
            # print(move)
            # print(f"{self.x} {self.y} {self.get_direction()}")

            if not scent:
                print(f"{self.get_status()} LOST")
                return f"{self.get_status()} LOST"
        print(self.get_status())
        return self.get_status()

    def check_present_scent(self):
        """Checks if scent is present in scents dictionary. If not, it is added for the future"""
        if f"{self.robot_x},{self.robot_y}" in self.scents:
            return True
        self.scents[f"{self.robot_x},{self.robot_y}"] = 1
        return False
