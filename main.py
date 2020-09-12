import numpy as np
import matplotlib.pyplot as plt

class Curves():
	def __init__(self, plots = [0, 10], numOfPoints = 21, yIntercept = 0, slope = 2):
		self.point1 = plots[0]
		self.point2 = plots[1]
		self.numOfPoints = numOfPoints
		self.yIntercept = float(yIntercept)
		self.slope = slope
	def createAxis(self):
		self.x = np.linspace(self.point1,self.point2, num = self.numOfPoints)
		self.y = self.slope * self.x + self.yIntercept
	def write(self, color = 'blue', marker = 'o'):
		plt.scatter(self.x, self.y, c = color, marker = marker)