from itertools import product

states=['A','B','C']
emissions=['X','Y','Z']

transitionMatrix=[[0.9, 0.0, 0.1], #A
                  [0.2, 0.6, 0.2], #B
                  [0.2, 0.5, 0.3]] #C
                 #  A    B    C 
                # X    Y    Z
emissionMatrix=[[0.6, 0.3, 0.1], #A
                [0.1, 0.7, 0.2], #B
                [0.2, 0.3, 0.5]] #C

probVector=[0.0, 0.2, 0.4]
sequenceEmissions = []

#finished
def main():
    get_path = True
    while(get_path):
        sequenceEmissions= list(map(str, input("Enter the emission sequence: ").strip().split()))
        if(valid_emission(sequenceEmissions, emissions) == True):
            #transition_set=[]
            print("All possible paths: ")
            s3 = list(product(states, states, states))
            print(s3)
            probablePaths = []
            for each in s3:
                if(valid_transitions(each, transitionMatrix, probVector)==True):
                    probablePaths.append(each)
            print("All probable paths: ")
            print(probablePaths)
            maxProb = ['', 0.0]
            for set in probablePaths:
                probability = path_probability(set, transitionMatrix, emissionMatrix, probVector, sequenceEmissions)
                print("Next probable sequence is:", set, "with a probability of:", probability)
                if(maxProb[1] < probability):
                    maxProb = (set, probability)
            print("\nMost probable sequence is:", maxProb[0], "with a probability of:", maxProb[1], "\n")
        exit()

#finished
def valid_emission(setEmissions, emissions):
    for ch in setEmissions:
        if ch not in emissions:
                return False
    return True

def valid_transitions(states, matrix, probVector):
    n = len(states)
    m=1
    j=0
    path_possible=True
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

    if (j <= 0.0 ):
        path_possible=False

    while(m < n and path_possible==True):
        i = m
        j = m
        if(abs(matrix[i][j] < 0.0)):
            path_possible = False
            i = i+1
            j = j+1
        m= m+1

    if(path_possible):
        return True
    else: 
        return False


def path_probability(set, transitionMatrix, emissionMatrix, probVector, sequenceEmissions):
    
    #getting the initial probability number
    init = 0
    if(set[0] == 'A'):
        init=probVector[0]
    if(set[0] == 'B'):
        init=probVector[1]
    if(set[0] == 'C'):
        init=probVector[2]
    if(set[0] == 'D'):
        init=probVector[3]
    if(set[0] == 'E'):
        init=probVector[4]

    #getting the multiplication values from transition matrix and emission matrix
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

    finalSum = init * var1 * var2 * em1 * em2 * em3
    return finalSum



if __name__ == '__main__':
    main()