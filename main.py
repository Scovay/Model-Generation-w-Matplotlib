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