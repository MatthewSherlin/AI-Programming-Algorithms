import os
import sys
import math
import random
import numpy as np



def main():

	p1 = pointdist(1,2,3)
	p2 = pointdist(4,5,6)
	print(p1.p, p1.dist)
	print(p2.p, p2.dist)

class pointdist:
    def __init__(self, x, y, dist):
            self.p = [x,y]
            self.dist = dist

if __name__ == '__main__':
	main()