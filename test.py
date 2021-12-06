import os
import sys
import random
import numpy as np

xVals = []
yVals = []
points = []

def main():

	nIn=int(input("Please provide size of input vectors: "))
	nPercep=int(input("Please provide number of perceptrons: "))
	nOut=int(input("Please provide size of output vectors: "))
	bias=float(input("Please provide bias: "))
	threshold=float(input("Please provide threshold: "))
	print("\n")
	
	inHiddenM = genInputHiddenMatrix(nIn, nPercep)
	hiddenOutM = genHiddenOutputMatrix(nOut, nPercep)

    
#initializing input to hidden layer matrix with random weights between -1 and 1
def genInputHiddenMatrix(n, m):
	inputM = np.zeros((n, m), dtype = float)
	for row in range(n):
		for col in range(m):
			inputM[row][col] = (random.randrange(-10,10)/10)
	print("input to hidden layer")
	print(inputM)
	return inputM

#initializing hidden to output layer matrix with random weights between -1 and 1
def genHiddenOutputMatrix(n, m):
	outputM = np.zeros((n, m), dtype = float)
	for row in range(n):
		for col in range(m):
			outputM[row][col] = (random.randrange(-10,10)/10)
	print("\n")
	print("input to hidden layer")
	print(outputM)
	return outputM


if __name__ == '__main__':
	main()

