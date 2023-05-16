#!/usr/bin/python3
"""
Geometry module. Handle geometries rect and square
"""


class square():
    """Rectangle class. Height and Width my be different.
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize the rectangle class
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Permitter of the square
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Square representation
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
