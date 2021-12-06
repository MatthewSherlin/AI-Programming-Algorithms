#program takes an input of vector, output, perceptrons, bias, learning rate, and threshold and outputs an output vector of size sizeOut

import os
import sys
import random
import numpy as np


def main():
    #getting inputs needed
    #bias=float(input("Give the perceptron bias: "))
    #learningRate=float(input("Please provide the learning rate between 0 and 1: "))
    #threshold=float(input("Please provide the threshold value: "))
    sizeIn=int(input("Please provide size of input vectors: "))
    sizePercep=int(input("Please provide number of perceptrons: "))
    sizeOut=int(input("Please provide size of output vectors: "))
    

    
    #settings rows and columns
    rows, cols = (sizeIn, sizePercep)
    rows2, cols2 = (sizeOut, sizePercep)
    #creating matricies
    inputHiddenMatrix = [[0.0]* cols] * rows
    hiddenOutputMatrix = [[0.0]* cols2] * rows2
    
    for row in range(sizeIn):
        for col in range(sizePercep):
            inputHiddenMatrix[col][row]=random.randrange(-1, 1)

    for row in range(sizePercep):
        for col in range(sizeOut):
            inputHiddenMatrix[row][col]=random.randrange(-1, 1)
    
    print(inputHiddenMatrix)



    
    
    return



if __name__ == '__main__':
    main()