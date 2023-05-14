#!/usr/bin/python3
"""
Geometry module. Handle geometries rect and square
"""
    
class rect():
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

class square(rect):
    """Square class that enforce height and width equal
    """
    def __init__(self, *args, **kwargs):
        """Provide for side representation of the square or width/height repr
        """
        if kwargs.get("side", 0) != 0:
            setattr(self, "width", kwargs.get("side", 0))
            setattr(self, "height", kwargs.get("side", 0))
        else:
            assert kwargs.get("height", 0) == kwargs.get("width", 0), "Height and Width of square must be equal"
            setattr(self, "width", kwargs.get("height", 0))
            setattr(self, "height", kwargs.get("width", 0))

if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
    
    s = square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

    s = square(wdith=12, height=9)
    print(s)
    print(s.area_of_my_square())
