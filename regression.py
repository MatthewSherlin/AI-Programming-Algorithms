import os
import sys

def main():
    
    def func(numPoints, xVals, yVals):
        #sum of x points and mean
        sumX=0
        for x in xVals:
            sumX += x
        meanX = sumX/numPoints 

        #sum of y points and mean
        sumY=0
        for y in yVals:
            sumY += y
        meanY = sumY/numPoints
        
        #variance
        def variance(xVals, numPoints):
            sub_x=0
            for x in xVals:
                sub_x += (x - meanX) ** 2
            xVar = sub_x / (numPoints - 1)
            return xVar
        
        #covariance
        def covariance(xVals, meanX, meanY, yVals, numPoints):
            sub_x=[i-meanX for i in xVals]
            sub_y=[i-meanY for i in yVals]
            num = sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
            denom = numPoints - 1
            covar = num/denom
            return covar
            
        #slope    
        slope = covariance(xVals, meanX, meanY, yVals, numPoints)/variance(xVals, numPoints)
        
        #intercept
        intercept = (meanY - slope * meanX)
        
        print("The slope of the points is", slope, "and the y-intercept of the points is", intercept)
        print("y=", slope,"x +", intercept)

    print("Enter list of x values separated by spaces")
    # store in x values
    str_arr = input().split(' ') #will take in a string of numbers separated by a space
    xVals = [int(num) for num in str_arr]

    print("Enter list of y values separated by spaces")
    # store in y values
    str_arr2 = input().split(' ') #will take in a string of numbers separated by a space
    yVals = [int(num2) for num2 in str_arr2] 

    numPoints = len(xVals)
    if(len(xVals) != len(yVals)): 
        print("\nPlease enter the same amount of x and y points")
        quit()

    func(numPoints, xVals, yVals)

if __name__ == '__main__':
    main()