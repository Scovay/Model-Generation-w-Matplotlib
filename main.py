import numpy as np
import matplotlib.pyplot as plot

class Curves():
	def __init__(self, plots = [0, 10], numOfPoints = 21, yIntercept = 0.0, slope = 2):
		self.point1 = plots[0]
		self.point2 = plots[1]
		self.numOfPoints = numOfPoints
		self.yIntercept = yIntercept
		self.slope = slope
	