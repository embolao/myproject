class Myproperty:
    """description"""

    def __init__(self, func):
        self.func = func

    def __get__(self, inst, owner=None):
        """docstring for __get__"""
        return self.func(inst)


class Location:
    """description"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @Myproperty
    def loc(self):
        """docstring for local"""
        return [self.x, self.y]

    def move_left(self):
        """docstring for move_left"""
        self.x -= 1

    def move_right(self):
        """docstring for move_right"""
        self.x += 1

    def move_up(self):
        """docstring for move_up"""
        self.y -= 1

    def move_down(self):
        """docstring for move_down"""
        self.y += 1

    def __repr__(self):
        """docstring for __repr__"""
        return f"{type(self).__name__}(x={self.x}, y={self.y})"
