import os
import sys
import math
from math import dist   
import random

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
            xVals.append(row[0])
            yVals.append(row[1])
            points.append((row[0], row[1]))
    
    #input number of clusters
    numClusters=float(input("Enter in number of clusters: "))
    print("Number of Clusters:", numClusters)

    #input shifting threshold value
    threshold=float(input("Enter in maximum centroid shift threshold: "))
    print("Threshold:", threshold)

    #call generate_seed_points(centroid, threshold)
    seedPoints, radius = generate_seed_points(xVals, yVals, numClusters)

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
    while count < maxLoop and stabilized == False:
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
    #determining the population to use?
    maxX, maxY, minX, minY, sizeX, sizeY, xLow, xMid, xHigh, yLow, yMid, yHigh, numMacro = 0 #some of these variables may be arrays
    #density = []?
    for x in xVals:
        xVals[x] = x * math.pi
    for y in yVals:
        yVals[y] = y * math.pi
    maxX = max(xVals)
    maxY = max(yVals)
    minX = min(xVals)
    minY = min(yVals)
    sizeX = (maxX-minX)/numClusters
    sizeY = (maxY-minY)/numClusters #in the pseudocode sizeY = (maxX-minX)/numClusters. is this a typo?
    numMacro = numClusters * numClusters
    #density  #density calculation goes here. how do i calculate this?
    #initialize set of macroblocks with higher than average density Sh ={}
    for i in range(numClusters):
        xLow  = minX + i * sizeX
        xHigh = xLow + sizeX
        xMid  = (xLow + xHigh)/2
        for j in range(numClusters):
            yLow  = minY + i * sizeY
            yHigh = yLow + sizeY
            yMid  = (yLow + yHigh)/2
            #δmacro = points_in_macroblocks(SP, xlow, ylow, xhigh, yhigh); wtf does this mean
            #if ( δmacro > δavg) Sh = (xmid, ymid); no clue what this does either
    
    #initializing seed points
    points2=points
    for i in range(numClusters):
        randSeedXY = random.choice(points)
        seedPoints.append(randSeedXY)
        points2.remove(randSeedXY)
    
    #calculating radius
    radius = infinityPositive
    for i in range(numClusters):
        for j in points2:
            tempDist = dist(seedPoints[i], points2[j])
            if (tempDist < 2 * radius):
                radius = tempDist/2

    return seedPoints, radius
if __name__ == '__main__':
    main()