import os
import sys
import math
from math import dist
from math import sqrt
import random
import numpy as np

#initializing variables
numClusters=0   
threshold=0
maxLoop=0
xVals = []
yVals = []
points = []
radius = 0
seedPoints = []
counter = 0
stabilized = True
firstCentroids=[]
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

    #input shifting threshold value
    threshold=float(input("Enter in maximum centroid shift threshold: "))
    print("Threshold:", threshold)

    #call generate_seed_points(points, num clusters)
    randSeedy = 0
    randSeedy = 0
    radius = generate_seed_points(xVals, yVals, numClusters)

    #input max loops
    maxLoop=float(input("Enter in maximum amount of loops: "))
    print("Maximum loops:", maxLoop)

    #setting count to 1 and stabilized to false
    counter + 1
    stabilized=False

    #copying centroid into another xy point
    firstCentroids = seedPoints #seedPoints[(1,1), (2,3), ...]

    #create a vector with size number of clusters of set of points
    clusters = []

    #big while loop that clusters
    while counter < maxLoop and stabilized == False:
        outliers=[]
        outliers=points
        clusterSequence=[]
        
        #go through the new cycle of computing clusters and centroids
        for i in range(numClusters):
            XcYc = firstCentroids[i]
            clusters[i]=[]
            for j in range(points):
                distance = dist(XcYc, points[j]) #for ex dist((1,2), (4,5))
                if distance <= radius:
                    clusters[i] = points[j] + clusters[i]
                    outliers = (outliers - points[j])
           
            XnewC=0
            YnewC=0
            SnewC=[]

             #x-mean of the points in the new cluster
            for x in range(clusters):
                XnewC += clusters[x(0)]
            XnewC = XnewC/len(clusters)
            
            #y-mean of the points in the new cluster
            for y in range(clusters):
                YnewC += clusters[y(0)]
            YnewC = YnewC/len(clusters)

            #collect centroids of the new clusters
            clusterSequence = (XnewC, YnewC) + clusterSequence
            print("Cluster #", i, "New Centroid:", XnewC, YnewC)
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
        count = count + 1
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
        xVals.remove(randSeedx)
        yVals.remove(randSeedy)

    #calculating radius
    radius = 100
    tempDist = 0
    print("seedpointx:", seedPointx, "seedpointy:", seedPointy)
    for i in range(numClusters):
        for j in range(len(xVals)):
            print("current seedPoint(x,y): ", seedPointx[i], seedPointy[i], "current point(x,): ", xVals[j], yVals[j])
            tempDist = distCalc(seedPointx[i],seedPointy[i],xVals[j],yVals[j])
            if (tempDist < 2 * radius):
                radius = tempDist/2

    return seedPointx, seedPointy, radius

#Euclidian distance calculation
def distCalc(x,x1,y,y1):
    temp = sqrt((x-x1)**2 + (y-y1)**2)
    return temp

if __name__ == '__main__':
    main()
