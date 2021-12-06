import os
import sys
import random
import numpy as np
import math

xVals = []
yVals = []
points = []

def main():

	nIn=int(input("Please provide size of input vectors: "))
	nPercep=int(input("Please provide number of perceptrons: "))
	nOut=int(input("Please provide size of output vectors: "))
	learningRate=float(input("Please learning rate: "))
	bias=float(input("Please provide bias: "))
	threshold=float(input("Please provide perceptron threshold: "))
	errorThreshold=float(input("Please provide error threshold: "))
	outVector= list(map(int, input("Enter the output vector: ").strip().split()))
	print(outVector)
	"""if(len(outVector) != len(nOut)):
		print("Output vector is too long.")
		exit()"""

	print("\n")

	#generating initial vector
	inVect = generateInputVector(nIn)
	print("initial vect: ", inVect)
	
	#generating matrixes
	inHiddenM = genInputHiddenMatrix(nIn, nPercep)
	hiddenOutM = genHiddenOutputMatrix(nOut, nPercep)
	print("\n")

	#generating value of hidden layer perceptrons
	fireList=fireCalc(inVect, inHiddenM, bias, threshold)
	print("1 is fire, 0 is no fire.\nFire list is:", fireList)

	#generating output value
	outList = fireOut(fireList, hiddenOutM)
	print("Output list is:", outList)

	error=calcError(outList,outVector)
	print("Error list:" ,error)





    
#initializing input to hidden layer matrix with random weights between -1 and 1
def genInputHiddenMatrix(n, m):
	inputM = np.zeros((n, m), dtype = float)
	for row in range(n):
		for col in range(m):
			inputM[row][col] = (random.randrange(-10,10)/10)
	print("input to hidden matrix")
	print(inputM)
	return inputM

#initializing hidden to output layer matrix with random weights between -1 and 1
def genHiddenOutputMatrix(n, m):
	outputM = np.zeros((n, m), dtype = float)
	for row in range(n):
		for col in range(m):
			outputM[row][col] = (random.randrange(-10,10)/10)
	print("\n")
	print("hidden to output matrix")
	print(outputM)
	return outputM

def generateInputVector(n):
	inVect = np.empty([n], dtype = float)
	for i in range(n):
		inVect[i] = random.randrange(0,2)
	return inVect

def fireCalc(inVect, inMatrix, bias, threshold):
	matrix=np.matmul(inVect, inMatrix)
	fireList=[]
	i=0
	while i < len(matrix):
		if((matrix[i]+bias)>=threshold):
			fireList.append(1)
			i=i+1
		else:
			fireList.append(0)
			i=i+1
	return fireList

def fireOut(hiddenOutM, fireList):
	matrixOutFire=np.matmul(hiddenOutM, fireList)
	return matrixOutFire

def calcError(outList, outVector):
	error = np.empty([len(outList)], dtype = float)
	i=0
	while i < len(outList):
		if(outList[i] != outVector[i]):
			error[i]=pow(((math.pi*outVector[i])-(math.pi*outList[i])),2)
			i=i+1
		else:
			error[i]=0
			i=i+1
	return error




if __name__ == '__main__':
	main()