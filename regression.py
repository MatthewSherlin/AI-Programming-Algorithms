import matplotlib.pyplot as plt
import numpy as np

def func(numPoints, xVals, yVals):
        #sum of x points and mean
        sumX=0
        for x in xVals:
            sumX += x
        meanX = sumX/numPoints
        print("Mean of x-values:", meanX) 

        #sum of y points and mean
        sumY=0
        for y in yVals:
            sumY += y
        meanY = sumY/numPoints
        print("Mean of y-values:", meanX) 
        
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

        print("Variance: ", variance(xVals, numPoints))
        print("Covariance: ", covariance(xVals, meanX, meanY, yVals, numPoints))
            
        #slope    
        slope = covariance(xVals, meanX, meanY, yVals, numPoints)/variance(xVals, numPoints)
        
        #intercept
        intercept = (meanY - slope * meanX)
        
        print("The slope of the points is", slope, "and the y-intercept of the points is", intercept)
        print("y=", slope,"x +", intercept)

        #printing points first
        plt.plot(xVals, yVals, 'r*', label='points')
        plt.axis([0, 20, 0, 20])
        for i, j in zip(xVals, yVals):
            plt.text(i, j+0.5, '({}, {})'.format(i, j))
        plt.title('Graph of Points')
        plt.show()

        #printing slope intercept form
        x = np.linspace(0,25,100)
        y = slope*x+intercept
        plt.plot(x, y, '-r', label='slope intercept form')
        plt.plot(xVals, yVals, 'r*')
        plt.axis([0, 10, 0, 10])
        for i, j in zip(xVals, yVals):
            plt.text(i, j+0.5, '({}, {})'.format(i, j))
        plt.title('Graph w/ Given Points')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.show()


def main():
    xVals=[]
    yVals=[]
    print("List of values input from text file.")
    with open('textFiles\RegressionPts.txt') as f:
        for line in f:
            row = line.split()
            xVals.append(int(row[0]))
            yVals.append(int(row[1]))
   
    for i in range(len(xVals)):
        print("Points:(",xVals[i],",",yVals[i],")")
    

    numPoints = len(xVals)
    if(len(xVals) != len(yVals)): 
        print("\nPlease enter the same amount of x and y points")
        quit()

    func(numPoints, xVals, yVals)

if __name__ == '__main__':
    main()