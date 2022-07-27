import random
import numpy as np

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
	outVector= list(map(int, input("Enter the output vector: ").strip().split()))
	print(outVector)

	print("\n")

	#generating matrixes
	inHiddenM = genInputHiddenMatrix(nIn, nPercep)
	hiddenOutM = genHiddenOutputMatrix(nOut, nPercep)
	print("\n")
	
	loop = 0
	while loop < 500:
		#prints loop num
		print("Loop: ", loop+1)

		#generating initial vector
		inVect = generateInputVector(nIn)
		print("initial vect: ", inVect)

		#generating value of hidden layer perceptrons
		percepList=fireCalc(inVect, inHiddenM, bias, threshold)
		print("Perceptron list is:", percepList)

		#generating output value
		outList = outCalc(percepList, hiddenOutM, bias)
		print("Output list is:", outList)

		#error calculation
		error=calcError(outList,outVector, learningRate)
		print("Error list: ",error)
		totalError = np.sum(error)
		if totalError == 0:
			print("Actual output achieved on loop: ", loop+1)
			exit()

		#weight adjustment
		inHiddenM = matrixAdd(inHiddenM, error)
		hiddenOutM = matrixAdd(hiddenOutM, error)
		print("input to hidden matrix after weight change: \n", inHiddenM)
		print("hidden to output matrix after weight change: \n", hiddenOutM)
		print("\n")
		loop = loop + 1


    
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
	for i in range(len(matrix)):
		#for j in range(len(matrix[i])):
		if ((matrix[i]+bias)>=threshold):
			fireList.append(1)
		else: 
			fireList.append(0)
	return fireList

def outCalc(M1, M2, bias):
	matrix = np.matmul(M1,M2)
	for i in range(len(matrix)):
		matrix[i] = matrix[i] + bias
	return matrix

def matrixAdd(M1, M2):
	matrixOut=np.add(M1, M2)
	return matrixOut

def calcError(outList, outVector, learningRate):
	error = np.empty([len(outList)], dtype = float)
	i=0
	while i < len(outList):
		if(outList[i] != outVector[i]):
			error[i]=((outVector[i])-(outList[i])) * learningRate
			i=i+1
		else:
			error[i]=0
			i=i+1
	return error

if __name__ == '__main__':
	main()