#!/usr/bin/python3
"""import"""
from models.base import Base


class Rectangle(Base):
    """doctrings for base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """comments of atributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @property
    def x(self):
        """x"""
        return self.__x

    @property
    def y(self):
        """y"""
        return self.__y

    @width.setter
    def width(self, value):
        """width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
    	"""return the area of the rectangle"""
    	return self.__width * self.__height
    
    def display(self):
        """ print the display of the rectangle to the stdout """
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)
   
    def update(self, *args, **kwargs):
        "update the rectangle"
        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']
        else:
            if len(args) < 1:
                return
            self.id = args[0]
            if len(args) < 2:
                return
            self.__width = args[1]
            if len(args) < 3:
                return
            self.__height = args[2]
            if len(args) < 4:
                return
            self.__x = args[3]
            if len(args) < 5:
                return
            self.__y = args[4]
 
    def to_dictionary(self):
    	"dict"
    	d = {}
    	d.setdefault('id', self.id)
        d.setdefault('width', self.__width)
        d.setdefault('height', self.__height)
        d.setdefault('x', self.__x)
        d.setdefault('y', self.__y)
        return d
