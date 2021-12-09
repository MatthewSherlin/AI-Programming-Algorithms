import os
import sys
import random
import numpy as np

sizeIN = 0
sizeOUT = 0
inputVector=[]
outputVector=[]
thresholdFire=0
thresholdError=0
maxCount=0

def main():
    
    #reading in size of input vector
    file = open("textFiles\inputVector.txt", "r")
    data = file.read()
    inputVector=data.split(" ")
    sizeIN=len(inputVector)
    print("Input Vector:", inputVector)
    
    #reading in size of output vector
    file = open("textFiles\outputVector.txt", "r")
    data2 = file.read()
    outputVector = data2.split(" ")
    sizeOUT=len(outputVector)
    print("Input Vector:", outputVector)

    numPerc=float(input("Give number of perceptrons in hidden layer: "))
    bias=float(input("Give the perceptron bias: "))
    cycle=float(input("Give cycles to be repeated: "))
    learnRate=float(input("Please provide the learning rate between 0 and 1: "))
    matrix1 = []
    matrix2=[]
    matrix1 = create_random_matrix(matrix1, sizeIN, numPerc)
    matrix2 = create_random_matrix(matrix2, numPerc, sizeOUT)
    print(matrix1)
    print(matrix2)
    i=2

    #no while loop because of single hidden layer
    matrixi=[]
    matrixi = create_random_matrix(matrixi, numPerc, numPerc)
    bias_vector_input=create_vector_bias(bias, sizeIN)
    bias_vector_hidden_layer=create_vector_bias(bias, numPerc)
    bias_vector_output_layer=create_vector_bias(bias, sizeOUT)
    while(cycle > 0):
        
    
        return 0


#create random matrix
def create_random_matrix(matrix, numRow, numCol):
    matrix = np.zeros(numRow,numCol)
    for i in range(numRow):
        for j in range(numCol):
            matrix[i][j] = random.randrange(-1,1)
    return matrix


def threshold_fire(cumVector, thresholdFire):
    cumOutVector=[]
    for i in range(cumVector):
        if cumVector[i] > thresholdFire:
            cumOutVector[i]=1
        else:
            cumOutVector[i]=0


def create_vector_bias(biasValue, vectorSize):
    i=0
    biasVector = []
    while i <= vectorSize:
        biasVector[i]=biasValue


def adjust_weight(numLayers, seqMatrixes, targetVector, actualVector, errorE, errorThreshold, learningRate):
    count = 1
    while errorE > errorThreshold and count <= maxCount:
        eIndex=[]
        for i in range(outputVector):
            if(outputVector[i] != vActual[i]):
                eIndex.append(outputVector[i])
        for index in eIndex:
            #sE = derive_weighted_edges
            for weightedEdge in sE:
                weight = weight + learningRate*(outputVector[weightedEdge]-vActual[weightedEdge])
        count=count+1
    return()


if __name__ == '__main__':
    main()