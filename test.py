import os
import sys
import math
from math import dist
import random
import numpy as np

xVals = []
yVals = []
points = []

def main():

	with open('textFiles\kMeansTextFile.txt') as f:
		for line in f:
			row = line.split()
			xVals.append(int(row[0]))
			yVals.append(int(row[1]))
			points.append((row[0], row[1]))
		print("all points: ", points)
		print("X values: ", xVals)
		print("Y valyes: ", yVals)

if __name__ == '__main__':
	main()

