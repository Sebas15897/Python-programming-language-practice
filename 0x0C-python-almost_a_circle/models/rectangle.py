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
      
