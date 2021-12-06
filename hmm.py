from itertools import product
import numpy as np

#set states and emission vectors. Remain with A- and X-
states=['A','B','C']
emissions=['X','Y','Z']

#setting transition matrix and emission matrix
transitionMatrix=[[0.9, 0.0, 0.5], #A
                  [0.0, 0.5, 0.2], #B
                  [0.1, 0.5, 0.3]] #C
                 #  A    B    C 

                # X    Y    Z
emissionMatrix=[[0.6, 0.3, 0.1], #A
                [0.1, 0.7, 0.2], #B
                [0.2, 0.3, 0.5]] #C

#setting probability vector
probVector=[0.0, 0.2, 0.4]
sequenceEmissions = []

#main driver
def main():
    get_path = True
    while(get_path):
        #get emission sequence from user
        sequenceEmissions= list(map(str, input("Enter the emission sequence: ").strip().split()))
        #if it is valid, run the rest of code
        if(valid_emission(sequenceEmissions, emissions) == True):
            print("All possible paths: ")
            #cartesian product to get all possible paths
            s3 = list(product(states, states, states))
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
                if(probability==0):
                    deletedPaths.append(set)
                else:
                    print("Next probable sequence is:", set, "with a probability of:", probability)
                if(maxProb[1] < probability):
                    maxProb = (set, probability)
            #finally, print the highest probability
            print("\nSequences",deletedPaths," were removed. Probability was 0.0")
            print("\nMost probable sequence is:", maxProb[0], "with a probability of:", maxProb[1], "\n")
        else:
            print("Emission sequence is invalid. Exiting...")
            exit()
        exit()

#check if emissions are valid. Making sure that user is inputting characters that exist in the vector
def valid_emission(setEmissions, emissions):
    #if too many emissions are added, false
    if(len(probVector) != len(states)):
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
    if(states[0] == 'A' | states[0] == 's1'):
        j=probVector[0]
    if(states[0] == 'B' | states[0] == 's2'):
        j=probVector[1]
    if(states[0] == 'C' | states[0] == 's3'):
        j=probVector[2]
    if(states[0] == 'D' | states[0] == 's4'):
        j=probVector[3]
    if(states[0] == 'E' | states[0] == 's5'):
        j=probVector[4]

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
    if(set[0] == 'A' | states[0] == 's1'):
        init=probVector[0]
    if(set[0] == 'B' | states[0] == 's2'):
        init=probVector[1]
    if(set[0] == 'C' | states[0] == 's3'):
        init=probVector[2]
    if(set[0] == 'D' | states[0] == 's4'):
        init=probVector[3]
    if(set[0] == 'E' | states[0] == 's5'):
        init=probVector[4]

    #getting the multiplication values from transition matrix and emission matrix
    # [A,B,A] A->B -> transitionMatrix[0][1]
    var1 = transitionMatrix[states.index(set[0])][states.index(set[1])]
    var2 = transitionMatrix[states.index(set[1])][states.index(set[2])]
    em1 = emissionMatrix[states.index(set[0])][emissions.index(sequenceEmissions[0])]
    em2 = emissionMatrix[states.index(set[1])][emissions.index(sequenceEmissions[1])]
    em3 = emissionMatrix[states.index(set[2])][emissions.index(sequenceEmissions[2])]
    #case if length of intial states is A-D
    if(len(states)==4):
        var3=transitionMatrix[states.index(set[2])][states.index(set[3])]
        em4=emissionMatrix[states.index(set[3])][emissions.index(sequenceEmissions[3])]
        finalSum = init*var1*var2*var3*em1*em2*em3*em4
        return finalSum
    #case if length of intial states is A-E
    if(len(states)==5):
        var3=transitionMatrix[states.index(set[2])][states.index(set[3])]
        em4=emissionMatrix[states.index(set[3])][emissions.index(sequenceEmissions[3])]
        var4=transitionMatrix[states.index(set[3])][states.index(set[4])]
        em5=emissionMatrix[states.index(set[4])][emissions.index(sequenceEmissions[4])]
        finalSum = init*var1*var2*var3*var4*em1*em2*em3*em4*em5
        return finalSum

    #getting the final probability sum and returning it
    finalSum = init * var1 * var2 * em1 * em2 * em3
    return finalSum


if __name__ == '__main__':
    main()