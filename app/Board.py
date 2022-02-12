class Board():
    id = 1
    lines = []
    direction_map = {
        0:"N",
        1:"E",
        2:"S",
        3:"W",
    }
    direction_map2 = {
        "N":0,
        "E":1,
        "S":2,
        "W":3,
    }
    scents = {}
    def __init__(self, filename):

        f = open(filename,"r")
        lines = f.read().splitlines()
        first_line = lines[0].split(" ")
        self.boardX = int(first_line[0])
        self.boardY = int(first_line[1])
        lines = lines[1:]
        print(first_line)
        # print(lines[2].encode('raw_unicode_escape'))
        self.lines = lines
        for line in lines:
            print(line)
        f.close()

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_direction(self):
        return self.direction_map.get(self.direction)

    
    def next(self):
        first_line = self.lines[0].split(" ")
        self.x = int(first_line[0])
        self.y = int(first_line[1])
        self.direction = self.direction_map2.get(first_line[2])
        movement = self.lines[1]
        self.lines = self.lines[3:]
        print(f"INIT: {self.x} {self.y} {self.get_direction()}")

#  0 
# 3 1 
#  2
        for move in movement:
            if move == "L":
                if self.direction > 0:
                    self.direction -= 1
                else:
                    self.direction = 3
            if move == "R":
                if self.direction < 3:
                    self.direction += 1
                else:
                    self.direction = 0
            print(self.direction)
            if move == "F":
                if self.direction == 0:
                    if self.y < self.boardY:
                        self.y += 1
                    else:
                        if self.scents.get(f"{self.x},{self.y}") == 1:
                            pass
                        else:
                            self.scents[f"{self.x},{self.y}"] = 1
                            return f"{self.x} {self.y} {self.get_direction()} LOST"
                if self.direction == 2:
                    if self.y > 0:
                        self.y -= 1
                    else:
                        if self.scents.get(f"{self.x},{self.y}") == 1:
                            pass
                        else:
                            self.scents[f"{self.x},{self.y}"] = 1
                            return f"{self.x} {self.y} {self.get_direction()} LOST"
                if self.direction == 1:
                    if self.x < self.boardX:
                        self.x += 1
                    else:
                        if self.scents.get(f"{self.x},{self.y}") == 1:
                            pass
                        else:
                            self.scents[f"{self.x},{self.y}"] = 1
                            return f"{self.x} {self.y} {self.get_direction()} LOST"
                if self.direction == 3:
                    if self.x > 0:
                        self.x -= 1
                    else:
                        if self.scents.get(f"{self.x},{self.y}") == 1:
                            pass
                        else:
                            self.scents[f"{self.x},{self.y}"] = 1
                            return f"{self.x} {self.y} {self.get_direction()} LOST"

            print(move)
            print(f"{self.x} {self.y} {self.get_direction()}")
        return f"{self.x} {self.y} {self.get_direction()}"