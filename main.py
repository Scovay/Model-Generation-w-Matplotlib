''' ============================================
===     Author: Jonathan Xu & Jinming Xu     ===
============================================ '''

'''
    This piece of module was designed to use matplotlib to generate images and their XML files to make 
    datasets to train a simple tensorflow modle that could detect shapes and their colors with transfer
    learning. This was used as a forerunner of a more advanced model using transfer learning to build an
    autonomous lawnmower called Handibot.
'''

# Module Imports
import numpy as np
import matplotlib.pyplot as plt
import random as rand
import time

# Generates a seed based on the current time for a completely new random set
seed = time.ctime()
rand.seed(seed)

class Curve():

    def __init__(self):
        print("Initiating Curve...")

        # All the color's avalible
        self.colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "yellow"]
    
        # All the marker's avalible
        self.markers = ['o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X']

    def generate(self, typeOfCurve = 1):
        print("Generating Curve...")

        # This randomly creates numpy x array varibles
        startPoint = 0
        endPoint = rand.randint(10, 30)
        numOfPoints = rand.randint(20, 30)

        # Generates the numpy x array to generate the matplotlib model
        self.x = np.linspace(startPoint, endPoint, num = numOfPoints)

        # This if statment is designed to generate the numpy y array
        if typeOfCurve == 1:
            yIntercept = rand.randint(0, 10)
            slope = rand.randint(-5, 5)
            self.y = slope * self.x + yIntercept
        elif typeOfCurve == 2:
            amplitude = rand.randint(1, 5)
            period = rand.randint(5,10)
            self.y = amplitude*np.sin(self.x*period)

        # Randomly selects the color and marker out of a list
        colorIndex = rand.randint(0,len(self.colors)-1)
        markerIndex = rand.randint(0,len(self.markers)-1)
        self.color = self.colors[colorIndex]
        self.marker = self.markers[markerIndex]

        return self

class XML():

    def __init__(self, filename):
        # Defines the x's and y's of each curve
        self.filename = filename
        self.xx = []
        self.yy = []

        # Creates a dictionary with the marker and it's symbol

        self.markerDictionary = {
            'o':"circle", 
            'v':"triangle_down", 
            '^':"triangle_up", 
            '<':"triangle_left", 
            '>':"triangle_right", 
            '8':"octagon", 
            's':"square", 
            'p':"pentagon", 
            '*':"star", 
            'h':"hexagon1",
            'H':"hexagon2", 
            'D':"diamond", 
            'd':"thin_diamond", 
            'P':"plus", 
            'X':"Cross"
        }

    def write(self, curves):
        print("Writing out xml file...")

        # The with statement opens the file
        with open(self.filename, "w") as f:
            # Create's the header of the XML file
            f.write("<annotation>\n")
            f.write("\t<folder>XML</folder>\n")
            f.write("\t<filename>{}</filename>\n".format(self.filename))
            f.write("\t<path></path>\n")
            f.write("\t<source>\n\t\t<database>Unknown</database>\n\t</source>\n")
            f.write("\t<size>\n\t\t<width>640</width>\n\t\t<height>640</height>\n\t\t<depth>3</depth>\n\t</size>\n\n")
            
            # The for loop is used to unpake each set of x and y from the nested list
            for i in range(len(self.yy)):
                # Gets the curve that's being written into XML
                c = curves[i]

                # Defines the lists of the true pixel value
                x_pxl = self.xx[i]
                y_pxl = self.yy[i]

                for n in range(len(x_pxl)):
                    # Creates an object
                    f.write("\t<object>\n")
                    f.write("\t\t<name>{}</name>\n".format(self.markerDictionary[c.marker]))
                    f.write("\t\t<bndbox>\n")
                    f.write("\t\t\t<xmin>{:d}</xmin>\n".format(round(x_pxl[n] - 7)))
                    f.write("\t\t\t<ymin>{:d}</ymin>\n".format(round(y_pxl[n] - 7)))
                    f.write("\t\t\t<xmax>{:d}</xmax>\n".format(round(x_pxl[n] + 7)))
                    f.write("\t\t\t<ymax>{:d}</ymax>\n".format(round(y_pxl[n] + 7)))
                    f.write("\t\t\t<pose>Unspecified</pose>\n")
                    f.write("\t\t<truncated>1</truncated>\n")
                    f.write("\t\t<difficult>0</difficult>\n")
                    f.write("\t\t</bndbox>\n")
                    f.write("\t</object>\n\n")

            # Tag to close the XML file
            f.write("</annotation>")

class Graph():

    def __init__(self, filename):
        print("Initiating Graph...")

        # Creates a list to hold curve objects
        self.curves = []

        # Create the filename of each file
        self.filename = filename
        xmlName = filename[:-3] + "xml"

        # Setup the XML class
        self.xml = XML(xmlName)

        # Setup the width and height
        self.width = 640
        self.height = 480

    def addCurve(self, curveType = 0):
        # This if statement is used to automaticly generate a shape
        if curveType == 0:
            curveType = rand.randint(1,2)

        # Creates the curve class and generates a x and y
        c = Curve()
        self.curves.append(c.generate(curveType))

    def plot(self):
        # Setup ax varible
        fig, ax = plt.subplots()
        print(fig)
        print("Plotting...")

        # Plots the curve
        for c in self.curves:
            plt.scatter(c.x, c.y, c = c.color, marker = c.marker)
            # line, = ax.plot(c.x, c.y, c = c.color)
        
        # Gets mins and maxes of the graph
        xmin, xmax, ymin, ymax = plt.axis()

        # Gets then left, bottom, width, height position
        l, b, w, h = ax.get_position().bounds

        # For loop calculates the true pixel points
        for c in self.curves:

            # Intilazes the of the NumPy arrays
            sz = len(c.x)

            # Setup the pxl areas
            x_pxl = np.zeros(sz)
            y_pxl = np.zeros(sz)

            # Calculates the pixel values
            for i in range(len(c.x)):
                # Calculates the pixel
                x_pxl[i] = self.width * (l + (c.x[i]-xmin)/(xmax-xmin)*w)
                y_pxl[i] = self.height * (1 - b - (c.y[i]-ymin)/(ymax-ymin)*h)

            # Appends the completed List
            self.xml.xx.append(x_pxl)
            self.xml.yy.append(y_pxl)

        # Saves the graph
        plt.savefig(self.filename)

        # Displays the graph
        # plt.show()
 
    def write(self):
        self.xml.write(self.curves)

# This input statement askes the user how many sets they want to generate
iterations = int(input("Enter how many sets you want: "))

# This list holds what type of curve it'll generate  
curveTypes = []

# This for loop creates however many plots the user wants
for x in range(iterations):
    # This generates the filenames of each set
    filename = "Noline" + str(x + 1) + ".png"

    # This for loop generates which type of curve will be in the set
    for _ in range(2):
        curveTypes.append(rand.randint(1,2))

    # This runs the graph class
    graph = Graph(filename)
    graph.addCurve(curveTypes[0])
    graph.addCurve(curveTypes[1])
    graph.plot()
    graph.write()