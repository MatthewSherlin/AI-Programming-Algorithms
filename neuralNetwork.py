import os
import sys
import random
import numpy as np

sizeIN = 0
sizeOUT = 0
seqInputVectors=[]
seqOutputVectors=[]
thresholdFire=0
thresholdError=0
maxCount=0

def main():

    #reading in size of input vector
    file = open("textFiles\inputVector.txt", "r")
    data = file.read().replace(" ", "")
    sizeIN=len(data)
    
    #reading in size of output vector
    file = open("textFiles\outputVector.txt", "r")
    data = file.read().replace(" ", "")
    sizeOUT=len(data)


    numPerc=float(input("Give number of perceptrons in each hidden layer: "))
    numHidden=float(input("Give the number of hidden layers: "))
    bias=float(input("Give the perceptron bias: "))
    cycle=float(input("Give cycles to be repeated: "))
    learnRate=float(input("Please provide the learning rate between 0 and 1: "))
    matrix1 = create_random_matrix(sizeIN, numPerc)
    matrix2 = create_random_matrix(numPerc, sizeOUT)
    i=2
    
    return

#create random matrix
def create_random_matrix(matrix, numRow, numCol):
    matrix = np.zeros(shape=(numRow,numCol))
    for i in range(numRow):
        for j in range(numCol):
            matrix[i][j] = random.randrange(-1,1)
        return matrix

def threshold_fire(cumVector, thresholdFire):
    cumOutVector=[]
    for i in range(cumVector): ##fix this for loop |v|
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
        return 


if __name__ == '__main__':
    main()