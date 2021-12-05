import os
import sys
import math
from math import dist
from math import sqrt
import random
import numpy as np
import copy

#initializing variables
numClusters=0   
radius=0
maxShift=0
maxLoop=0
xVals = []
yVals = []
points = []
radius = 0
counter = 0
stabilized = True
centroidX=[]
centroidY=[]

def main():
    #open & read in file
    with open('textFiles\kMeansTextFile.txt') as f:
        for line in f:
            row = line.split()
            xVals.append(int(row[0]))
            yVals.append(int(row[1]))
    print("xValues: ",xVals)
    print("yValues: ",yVals)

    #input number of clusters
    numClusters=int(input("Enter in number of clusters: "))
    print("Number of Clusters:", numClusters, "\n")

    #input maximum shift threshold value
    maxShift=float(input("Enter in maximum centroid shift threshold: "))
    print("Maximum shift:", maxShift, "\n")

    #input threshold value
    radius=int(input("Enter in centroid radius: "))
    print("Radius: ", radius, "\n")

    #input max loops
    maxLoop=float(input("Enter in maximum amount of loops: "))
    print("Maximum loops:", maxLoop, "\n")

    #call generate_seed_points(points, num clusters)
    centroidX, centroidY = generate_seed_points(xVals, yVals, numClusters)

    #setting count to 1 and stabilized to false, init outliers
    counter = 0
    stabilized=False
    outliersX=[]
    outliersY=[]

    #big while loop that clusters
    while counter < maxLoop and stabilized == False:
        #these variables could do with being delcared before the while loop or before the function uses them to improve readability
        clusterX=[[] for _ in range(numClusters)]
        clusterY=[[] for _ in range(numClusters)]
        pointArr=[]
        distArr = []
        tempDist = 0
        meanX = 0
        meanY = 0

        #prints loop number
        print("\n")
        print("Loop number: ", counter + 1)

        #prints centroid value
        for i in range(len(centroidX)):
            print("Centroids(x,y) ",i+1, ": (", centroidX[i], ",", centroidY[i], ")") 
        
        #calculating distance between each point and centroids
        for i in range(len(xVals)):
            del distArr
            distArr = []
            for j in range(numClusters):
                #calculation distance
                tempDist = distCalc(xVals[i], yVals[i], centroidX[j], centroidY[j])
                distArr.append(tempDist)
                #print("current point(x,y): ", xVals[i], yVals[i], "current centroid(x,y): ", centroidX[j], centroidY[j], "tempDist: ", tempDist)
            tp = pointdist(xVals[i], yVals[i], distArr)
            pointArr.append(tp)

        outliersX.clear()
        outliersY.clear()
        #inserting into outliers and clusters
        for obj in pointArr:
            #obj.printData()
            dist, i = obj.getIndex()
            if dist < radius:
                clusterX[i].append(obj.getX())
                clusterY[i].append(obj.getY())
            else: 
                outliersX.append(obj.getX())
                outliersY.append(obj.getY())

        #printing cluster values
        for i in range(numClusters):
            print("Cluster: ", i+1, "x values: ", clusterX[i])
            print("Cluster: ", i+1, "y values: ", clusterY[i])
            if (len(clusterX[i])) == 0:
                print("Centroid ", i+1, "has no points within radius. Exiting")
                exit()

        for i in range(numClusters):
            #calculating x and y mean
            meanX = (sum(clusterX[i]))/(len(clusterX[i]))
            meanY = (sum(clusterY[i]))/(len(clusterY[i]))
            print("Cluster: ", i+1, "Mean x: ", meanX, "Mean y: ", meanY)

            #calculating centroid shift
            tempDist = distCalc(meanX, meanY, centroidX[i], centroidY[i])
            if tempDist < maxShift:
                stabilized = True
                print("Centroid ", i+1 ,"shift : ", tempDist,"is less than max shift, stabilized. Exiting")
                break
            else:
                print("Centroid ", i+1 ,"shift: ", tempDist)

            #setting new centroid values
            centroidX[i] = meanX
            centroidY[i] = meanY

        #incrementing counter
        counter = counter + 1
        if counter == maxLoop:
            print("Max Loop reached, exitng")

    #printing outlier values
    print("Outliers x values: ", outliersX)
    print("Outliers y values: ", outliersY)
        

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

class pointdist:
    def __init__(self, x, y, dist):
            self.x = x
            self.y = y
            self.distNum = dist

    def printData(self):
        print("(x,y): ", self.x, self.y,"distance: ", self.distNum)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getIndex(self):
        minDist = min(self.distNum)
        index = self.distNum.index(minDist)
        return minDist, index


if __name__ == '__main__':
    main()
