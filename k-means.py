import os
import sys

#generate_seed_points(sequence of points(xVals, yVals)?, num of clusters)
    #output set of seed points, radius of clusters

def main():
    xVals = []
    yVals = []
    full = []
    #open & read in file
    with open('textFiles\kMeansTextFile.txt') as f:
        for line in f:
            row = line.split()
            xVals.append(row[0])
            yVals.append(row[1])
    
    #input number of clusters

    #input shifting threshold value

    #call generate_seed_points(centroid, threshold)

    #input max loops

    #setting count to 1 and stabilized to false

    #copying centroid into another xy point

    #create a vector with size number of clusters of set of points

    #big ass while loop that clusters

    #output centroids, sequence of points in clusters, and outliers for each loop
    return


if __name__ == '__main__':
    main()