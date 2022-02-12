class Board():
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

        f = open(filename, "r")
        lines = f.read().splitlines()
        first_line = lines[0].split(" ")
        self.boardX = int(first_line[0])
        self.boardY = int(first_line[1])
        lines = lines[1:]
        # print(first_line)
        self.lines = lines
        # for line in lines:
        #     print(line)
        f.close()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.direction_map.get(self.direction)

    def get_status(self):
        return f"{self.x} {self.y} {self.get_direction()}"

    def next(self):
        if len(self.lines) == 0:
            print("No more instructions")
            return "No more instructions"
        first_line = self.lines[0].split(" ")
        self.x = int(first_line[0])
        self.y = int(first_line[1])
        self.direction = self.direction_map2.get(first_line[2])
        movement = self.lines[1]
        self.lines = self.lines[3:]
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
                        self.direction) == "N" and self.y < self.boardY:
                    self.y += 1
                elif self.direction_map.get(
                        self.direction) == "S" and self.y > 0:
                    self.y -= 1
                elif self.direction_map.get(
                        self.direction) == "E" and self.x < self.boardX:
                    self.x += 1
                elif self.direction_map.get(
                        self.direction) == "W" and self.x > 0:
                    self.x -= 1
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
        if f"{self.x},{self.y}" in self.scents:
            return True
        else:
            self.scents[f"{self.x},{self.y}"] = 1
            return False