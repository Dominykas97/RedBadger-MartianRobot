class Board():
    id = 1
    def __init__(self, filename):

        f = open(filename,"r")
        lines = f.read().splitlines()
        first_line = lines[0].split(" ")
        self.x = int(first_line[0])
        self.y = int(first_line[1])
        lines = lines[1:]
        print(first_line)
        for line in lines:
            print(line)