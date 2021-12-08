from itertools import product
import numpy as np
import random

#initializing states and emission vectors. Remains with A- and X-
states=[]
emissions=[]

#initializing transition matrix and emission matrix
transitionMatrix=[]
emissionMatrix=[]

#initializing probability vector
probVector=[]
sequenceEmissions = []

#main driver
def main():
    statesNum=int(input("Enter in number of inital states: "))
    emissionsNum=int(input("Enter in number of emissions: "))
    
    for x in range(statesNum):
        states.append(possibleStates[x])
    for x in range(emissionsNum):
        emissions.append(possibleEmissions[x])
    for x in range(statesNum):
        print("Enter in inital probabilities (", x+1, '/', statesNum, "):")
        value=float(input())
        probVector.append(value)
    
    print("States:", states, "Emissions:", emissions, "Probability Vector:", probVector)

    transitionMatrix = np.random.rand(statesNum,statesNum)
    transitionMatrix=transitionMatrix/transitionMatrix.sum(axis=1)[:,None]
    print("Random Transition Matrix:\n",transitionMatrix)
    emissionMatrix = np.random.rand(emissionsNum, statesNum)
    emissionMatrix=emissionMatrix/emissionMatrix.sum(axis=1)[:,None]
    print("Random Emission Matrix:\n",emissionMatrix)


    get_path = True
    while(get_path):
        #get emission sequence from user
        sequenceEmissions= list(map(str, input("Enter the emission sequence: ").strip().split()))
        #if it is valid, run the rest of code
        if(valid_emission(sequenceEmissions, emissions) == True):
            print("All possible paths: ")
            #cartesian product to get all possible paths
            s3 = []
            if(len(states) == 2):
                s3 = list(product(states, states))
            if(len(states) == 3):
                s3 = list(product(states, states, states))
            if(len(states) == 4):
                s3 = list(product(states, states, states, states))
            if(len(states) == 5):
                s3 = list(product(states, states, states, states, states))
            print(s3)
            probablePaths = []
            deletedPaths = []
            #for each possible path from cartesian product: [a,a,a]
            for each in s3:
                #if they are valid, they are added to probable paths, the others are discarded
                if(valid_transitions(each, transitionMatrix, probVector)==True):
                    probablePaths.append(each)
            print("All probable paths: ")
            print(probablePaths)
            #setting maximum probability list
            maxProb = ['', 0.0]
            #for each path in the probable paths, calculate probability and if it is higher than max, replace it
            for set in probablePaths:
                probability = path_probability(set, transitionMatrix, emissionMatrix, probVector, sequenceEmissions)
                if(probability==0.0):
                    deletedPaths.append(set)
                else:
                    print("Next probable sequence is:", set, "with a probability of:", probability)
                if(maxProb[1] < probability):
                    maxProb = (set, probability)
            #finally, print the highest probability
            print("\nSequences with probability of 0.0 were removed.")
            print("\nMost probable sequence is:", maxProb[0], "with a probability of:", maxProb[1], "\n")
        else:
            print("Emission sequence is invalid. Exiting...")
            exit()
        exit()

#check if emissions are valid. Making sure that user is inputting characters that exist in the vector
def valid_emission(setEmissions, emissions):
    #if too many emissions are added, false
    if(range(len(probVector))) != range((len(states))):
        return False 
    #if the characters are incorrect, false
    for ch in setEmissions:
        if ch not in emissions:
                return False
    return True

def valid_transitions(states, matrix, probVector):
    #initializing some counters
    n = len(states)
    m=1
    j=0
    path_possible=True
    #set inital probability vector to first state
    if(states[0] == 'A'):
        j=probVector[0]
    if(states[0] == 'B'):
        j=probVector[1]
    if(states[0] == 'C'):
        j=probVector[2]
    if(states[0] == 'D'):
        j=probVector[3]
    if(states[0] == 'E'):
        j=probVector[4]
    if(states[0] == 'F'):
        j=probVector[5]
    if(states[0] == 'G'):
        j=probVector[6]
    # ...

    #if inital prob vector value is 0.0, false
    if (j <= 0.0 ):
        path_possible=False

    #if paths in matrix are 0.0, they are untraversable
    while(m < n and path_possible==True):
        i = m
        j = m
        if(abs(matrix[i][j] <= 0.0)):
            path_possible = False
            i = i+1
            j = j+1
        m= m+1

    #if path is possible, then add to possible paths list
    if(path_possible):
        return True
    else: 
        return False


def path_probability(set, transitionMatrix, emissionMatrix, probVector, sequenceEmissions):
    #getting the initial probability number
    init = 0
    if(set[0] == 'A'):
        init=probVector[0]
    if(set[0] == 'B' ):
        init=probVector[1]
    if(set[0] == 'C'):
        init=probVector[2]
    if(set[0] == 'D'):
        init=probVector[3]
    if(set[0] == 'E'):
        init=probVector[4]
    if(set[0] == 'F'):
        init=probVector[5]
    if(set[0] == 'G'):
        init=probVector[6]
    # ...

    #getting the multiplication values from transition matrix and emission matrix
    # [A,B,A] A->B -> transitionMatrix[0][1]
    varArray=[]
    emArray=[]
    finalSum=init

    #get all of the state amounts
    for x in range(len(states)):
        varArray.append(transitionMatrix[states.index(set[x-1])][states.index(set[x])])
    #get all of the emissions amounts
    for x in range(len(emissions)):
        emArray.append(emissionMatrix[states.index(set[x-1])][emissions.index(sequenceEmissions[x-1])])
    #multiply all together
    for x in range(len(varArray)):
        finalSum = finalSum * varArray[x-1]
    for x in range(len(emArray)):
        finalSum = finalSum * emArray[x-1]
    
    return finalSum


## End functionality
#################################












possibleStates=['A', 'B', 'C', 'D', 'E', 'F', 'G']
possibleEmissions=['X', 'Y', 'Z', 'W', 'V', 'R', 'S']

if __name__ == '__main__':
    main()
