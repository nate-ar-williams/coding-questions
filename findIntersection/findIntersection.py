#!/usr/bin/python3

class Line:
	# m is slope
	# b is y intercept

	def __init__(self, p1, p2):
		self.start = p1
		self.end = p2
		self.m = self.findSlope(p1, p2)
		self.b = self.findYIntercept(p1, self.m)

	def findSlope(self, firstPoint, secondPoint):
		# handle undefined later
		return (secondPoint[1] - firstPoint[1]) / (secondPoint[0] - firstPoint[0])

	def findYIntercept(self, point, m):
		return point[1] - m * point[0]

	def findIntersect(self, line2):
		# if slopes are equal
		x = (line2.b - self.b) / (self.m - line2.m)
		y = self.m * x + self.b

		if x >= self.start[0] and x <= self.end[0]:
			return x, y
		return None, None

def main():
	pass

if __name__ == '__main__':
	main()
