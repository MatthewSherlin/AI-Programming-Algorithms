import os
import sys
import math
from math import dist
from math import sqrt
import random
import numpy as np

#initializing variables
numClusters=0   
radius=0
maxShift=0
maxLoop=0
xVals = []
yVals = []
points = []
radius = 0
seedPoints = []
counter = 0
stabilized = True
firstCentroidx=[]
firstCentroidy=[]
infinityPositive = math.inf

def main():
    #open & read in file
    with open('textFiles\kMeansTextFile.txt') as f:
        for line in f:
            row = line.split()
            xVals.append(int(row[0]))
            yVals.append(int(row[1]))
            points.append((row[0], row[1]))
    print("all points: ",points)
    print("xValues: ",xVals)
    print("yValues: ",yVals)

    #input number of clusters
    numClusters=int(input("Enter in number of clusters: "))
    print("Number of Clusters:", numClusters)

    #input maximum shift threshold value
    maxShift=float(input("Enter in maximum centroid shift threshold: "))
    print("Maximum shift:", maxShift)

    #input threshold value
    radius=int(input("Enter in centroid radius: "))
    print("Radius: ", radius)

    #input max loops
    maxLoop=float(input("Enter in maximum amount of loops: "))
    print("Maximum loops:", maxLoop)

    #call generate_seed_points(points, num clusters)

    firstCentroidx, firstCentroidy = generate_seed_points(xVals, yVals, numClusters)
    for i in range(len(firstCentroidx)):
        print("First Centroids(x,y): ", "(", firstCentroidx[i], ",", firstCentroidy[i], ")") 

    #setting count to 1 and stabilized to false
    counter = 0
    stabilized=False
            
    #copying centroid into another xy point
    firstCentroids = seedPoints #seedPoints[(1,1), (2,3), ...]

    #create a vector with size number of clusters of set of points
    clusters = []

    #big while loop that clusters
    while counter < maxLoop and stabilized == False:
        outliersX=[]
        outliersY=[]
        clusterSequence=[]
        clusterX=[]
        clusterY=[]
        tempListx = []
        tempListy = []
        tempOutx = []
        tempOuty = []
        tempDist = 0
        meanX = 0
        meanY = 0

        #go through the new cycle of computing clusters and centroids
        for i in range(numClusters):
            temp = 0
            for j in range(len(xVals)):
                tempDist = distCalc(firstCentroidx[i], firstCentroidy[i], xVals[j], yVals[j])
                print("current centroid(x,y): ", firstCentroidx[i], firstCentroidy[i], "current point(x,y): ", xVals[j], yVals[j], "tempDist: ", tempDist)
                if tempDist < radius:
                    tempListx.append(xVals[j])
                    tempListy.append(yVals[j])
                    clusterX.append(tempListx)
                    clusterY.append(tempListy)
                    temp = temp + 1
                else:
                    tempOutx.append(xVals[j])
                    tempOuty.append(yVals[j])   
                    outliersX.append(tempOutx)
                    outliersY.append(tempOuty)
            
            print("cluster: ", i+1, "X outliers: ", outliersX[i])
            print("cluster: ", i+1, "Y outliers: ", outliersY[i])
            print("cluster: ", i+1, "X points in cluster: ", clusterX[i])
            print("cluster: ", i+1, "Y points in cluster: ", clusterY[i])
            #x-mean of the points in the new cluster
            meanX = (sum(clusterX[i]))/temp
            print("Mean X: ", meanX)
            #y-mean of the points in the new cluster
            meanY = (sum(clusterY[i]))/temp
            print("Mean Y:", meanY)
        exit()
            #collect centroids of the new clusters
#            clusterSequence = (meanX, meanY) + clusterSequence
#            print("Cluster #", i, "New Centroid:", meanX, meanY)
            #end for loop

        print("Current Outliers:", outliers)
        stabilized = True
        for i in range(numClusters):
            XnewC = math.pi(clusterSequence[i(0)])
            YnewC = math.pi(clusterSequence[i(1)])
            Xc = math.pi(firstCentroids[i(0)])
            Yc = math.pi(firstCentroids[i(1)])
            centroid_shift=math.sqrt((pow((XnewC-Xc),2))+(pow((YnewC-Yc),2)))
            if centroid_shift > threshold:
                stabilized = False
        firstCentroids = clusterSequence
        counter = counter + 1
    #output centroids, sequence of points in clusters, and outliers for each loop
    print("Final Clusters and Outliers:")
    for i in range(numClusters):
        print(clusters[i])
    print(outliers)
        

# inputs set of points and number of clusters
# outputs set of seed points, radius of clusters
def generate_seed_points(xVals, yVals, numClusters):
    
    #initializing seed points
    seedPointx = []
    seedPointy = []
    for i in range(numClusters):
        index = random.choice(range(len(xVals)))
        randSeedx = xVals[index]
        randSeedy = yVals[index]
        seedPointx.append(randSeedx)
        seedPointy.append(randSeedy)
        del xVals[index]
        del yVals[index]

    return seedPointx, seedPointy

#Euclidian distance calculation
def distCalc(x,y,x1,y1):
    temp = math.sqrt(((x-x1)**2) + ((y-y1)**2))
    return temp

if __name__ == '__main__':
    main()
