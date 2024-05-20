def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def quadr(number):
    return number ** 4

def quint(number):
    return number ** 5

class MovingObject:
    def __init__(self, position):
        self.position = position

    def move_square(self):
        self.position = square(self.position)

    def move_cube(self):
        self.position = cube(self.position)

    def move_quint(self):
        self.position = quint(self.position)