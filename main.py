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
		return marker

class XML():
	def __init__(self, x, y, marker, diameter = 10):
		self.marker = marker
		self.x = x
		self.y = y
		self.Xmins = []
		self.Ymins = []
		self.Xmaxes = []
		self.Ymaxes = []
		self.diameter = diameter
	def calc(self):
		for x in len(self.x):
			self.Xmins.append(self.x[x] - (self.diameter/2))
			self.Ymins.append(self.y[x] - (self.diameter/2))
			self.Xmaxes.append(self.x[x] + (self.diameter/2))
			self.Ymaxes.append(self.y[x] + (self.diameter/2))