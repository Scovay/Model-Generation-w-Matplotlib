import numpy as np
import matplotlib.pyplot as plt
import random as rand
import time

seed = time.ctime()
rand.seed(seed)


class Curves():
	def __init__(self, plot1 = 0, plot2 = 10, numOfPoints = 21, yIntercept = 0, slope = 2):
		self.point1 = plot1
		self.point2 = plot2
		self.numOfPoints = numOfPoints
		self.yIntercept = float(yIntercept)
		self.slope = slope
	def createAxis(self):
		self.x = np.linspace(self.point1,self.point2, num = self.numOfPoints)
		self.y = self.slope * self.x + self.yIntercept
		return self.x, self.y
	def write(self, color = 'blue', marker = 'o'):
		plt.scatter(self.x, self.y, c = color, marker = marker)
		plt.show()

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
	def writeToXML(self):
		with open("line.xml", "w") as f:
			f.write("<annotation>\n")
			f.write("\t<folder>XML</folder>\n")
			f.write("\t<filename>shape.png</filename>\n")
			f.write("\t<path>/XML</path>\n")
			f.write("\t<source>\n\t\t<database>Unknown</database>\n\t</source>\n")
			f.write("<size>\n\t\t<width>640</width>\n\t\t<height>640</height>\n\t\t<depth>3</depth>\n\t</size>\n\n")
			for x in len(self.x):
				f.write("\t<object>\n")
				f.write("\t\t<name>{}~{}</name>\n".format(self.marker, x+1))
				f.write("\t\t<pose>Unspecified</pose>\n")
				f.write("\t\t<truncated>1</truncated>\n")
				f.write("\t\t<difficult>0</difficult>\n")
				f.write("\t\t<bndbox>\n")
				f.write("\t\t\t<xmin>{}</xmin>\n".format(self.Xmins[x]))
				f.write("\t\t\t<ymin>{}</ymin>\n".format(self.Ymins[x]))
				f.write("\t\t\t<xmax>{}</xmax>\n".format(self.Xmaxes[x]))
				f.write("\t\t\t<ymax>{}</ymax>\n".format(self.Xmaxes[x]))
				f.write("\t\t</bndbox>\n")
				f.write("\t</object>\n\n")
			f.write("</annotation>")

class Graph():
	def __init__(self, color = "white", width = 10, height = 6):
		plt.figure(figsize=(width,height),facecolor = color)
		self.colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
		self.markers = ['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']
	def setupCurve(self):
		plot1 = int(input("Enter point 1: "))
		plot2 = int(input("Enter point 2: "))
		numOfPoints = int(input("Enter the number of points: "))
		yIntercept = int(input("Enter the Y intercept: "))
		slope = int(input("Enter the slope: "))
		if not (plot1 or plot2 or numOfPoints or yIntercept or slope):
			plot1 = 0
			plot2 = rand.randint(10, 25)
			numOfPoints = rand.randint(20, 50)
			yIntercept = rand.randint(0, 10)
			slope = rand.randint()
			self.curve = Curves(plot1, plot2, numOfPoints, yIntercept, slope)
		else:
			self.curve = Curves(plot1, plot2, numOfPoints, yIntercept, slope)
	def setupXML(self):
		self.XML = XML(self.x, self.y, self.marker)
	def runCurve(self):
		self.x, self.y = self.curve.createAxis()
		color = input("Enter your color: ")
		self.marker = input("Enter your marker code: ")
		if not (color or self.marker):
			colorIndex = rand.randint(0,len(self.colors))
			markerIndex = rand.randint(0,len(self.markers))
			color = self.colors(colorIndex)
			self.marker = self.markers(markerIndex)
		
		self.curve.write(color, self.marker)
	def runXML(self):
		self.XML.calc()
		self.XML.writeToXML()

