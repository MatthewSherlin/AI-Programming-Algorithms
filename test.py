import os
import sys
import math
from math import dist
import random
import numpy as np

numList = 0
list1 = []
list2 = [1,2,3]
def main():

	numList = int(input("enter num of lists: "))
	print(numList)
	for i in range(numList):
		list1.append(list2)
	print(list1)

if __name__ == '__main__':
	main()

