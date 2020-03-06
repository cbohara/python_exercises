class Point:
	"""3-dimensional point"""
	def __init__(self, x, y, z):
		"""Initialize x, y, and z attributes"""
		self.x, self.y, self.z = x, y, z

	def __repr__(self):
		"""Human-reable string of Point object"""
		return f"Point(x={self.x}, y={self.y}, z={self.z})"

	def __eq__(self, other):
		"""Evaluate equality"""
		return (self.x, self.y, self.z) == (other.x, other.y, other.z)

	def __add__(self, other):
		"""Return copy of Point with valued shifted by each other"""
		return Point(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		"""Return copy of Point with values shifted by each other"""
		return Point(self.x - other.x, self.y - other.y, self.z - other.z)

	def __mul__(self, scalar):
		"""Return new copy of our Point, scaled by a given value"""
		return Point(scalar*self.x, scalar*self.y, scalar*self.z)

	def __rmul__(self, scalar):
		"""Method used if left object does not have __mul__ implemented"""
		return self.__mul__(scalar)

	def __iter__(self):
		"""Make the Point object iterable"""
		yield self.x
		yield self.y
		yield self.z
