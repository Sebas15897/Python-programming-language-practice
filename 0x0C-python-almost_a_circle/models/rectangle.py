#!/usr/bin/python3
"""Import"""
from models.base import Base


class Rectangle(Base):
	"""docstring for Rectangle"""
	def __init__(self, width, heigth, x, y):
		super().__init__(id)
		self.width = width
		self.heigth = heigth
		self.x = x
		self.y = y

	@property
	def width(self):
		"""Width"""
		return self._width

	@property
	def heigth(self):
		"""Heigth"""
		return self._heigth

	@property
	def x(self):
		"""X"""
		return self._x

	@property
	def y(self):
		"""Y"""
		return self._y

	@width.setter
	def width(self, value):
		"""Setter"""
		if type(value) is not int:
			raise typeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value

	@heigth.setter
	def heigth(self, value):
		"""Setter"""
		if type(value) is not int:
			raise typeError("heigth must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__heigth = value

	@x.setter
	def x(self, value):
		"""setter"""
		if type(value) is not int:
			raise typeError("x must be an integer")
		if value < 0:
			raise ValueError("x must b >= 0")
		self.__x = value

	@y.setter
	def y(self, value):
		"""setter"""
		if type(value) is not int:
			raise typeError("y must be an integer")
		if value < 0:
			raise typeError("y must b >= 0")
		self.__y = value
