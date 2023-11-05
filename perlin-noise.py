## préambule
""""
More advanced noise generation, folowing documentation
"""

## imports

import random as rd
import time as ti
import matplotlib.pyplot as plt
import math as ma

## brouilon

M=[[0 for x in range (50)] for y in range (50)]

## visual

def visual(M):
    plt.matshow(M)
    plt.show()

## code

"""
following the insturctions for perlin noise

the basic principel is to equip the plane with a grid and giving each point a vector. then dot products are used to calculate the value of each point on the plane. see on wikipedia for more info
"""

def randomUnitVector():
    phi=rd.random()*2*ma.pi
    return [ma.cos(phi),ma.sin(phi)]

def smoothstep(x):
    return -2*x**3+3*x**2

def dotproduct(x1,y1,x2,y2):
    return x1*x2+y1*y2

def perlin_noise(gridSize = 10 ,caseSize = 20):
    n=gridSize*caseSize
    plane=[[0 for x in range (n)] for y in range (n)]
    vectMatrix=[[randomUnitVector() for x in range (gridSize+1)] for y in range (gridSize+1)]
    for x in range(n):
        for y in range(n):
            xvect=int(x/caseSize)
            yvect=int(y/caseSize)
            a= dotproduct((x-xvect*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect][yvect][0], vectMatrix[xvect][yvect][1])
            b= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect+1][yvect][0], vectMatrix[xvect+1][yvect][1])
            c= dotproduct((x-xvect*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect][yvect+1][0], vectMatrix[xvect][yvect+1][1])
            d= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect+1][yvect+1][0], vectMatrix[xvect+1][yvect+1][1])
            avg1 = a+smoothstep((x-xvect*caseSize)/caseSize)*(b-a)
            avg2 = c+smoothstep((x-xvect*caseSize)/caseSize)*(d-c)
            avg = avg1+smoothstep((y-yvect*caseSize)/caseSize)*(avg2-avg1)
            plane[x][y]=avg
    return plane

"""
sucess !
"""
## Void implementation

def blankPlane(gridSize,caseSize):
    n=gridSize*caseSize
    plane=[[0 for x in range (n)] for y in range (n)]
    return plane

def perlinNoiseVoid(plane,gridSize):
    n=len(plane)
    caseSize=n//gridSize
    vectMatrix=[[randomUnitVector() for x in range (gridSize+2)] for y in range (gridSize+2)]
    for x in range(n):
        for y in range(n):
            xvect=int(x/caseSize)
            yvect=int(y/caseSize)
            a= dotproduct((x-xvect*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect][yvect][0], vectMatrix[xvect][yvect][1])
            b= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect+1][yvect][0], vectMatrix[xvect+1][yvect][1])
            c= dotproduct((x-xvect*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect][yvect+1][0], vectMatrix[xvect][yvect+1][1])
            d= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect+1][yvect+1][0], vectMatrix[xvect+1][yvect+1][1])
            avg1 = a+smoothstep((x-xvect*caseSize)/caseSize)*(b-a)
            avg2 = c+smoothstep((x-xvect*caseSize)/caseSize)*(d-c)
            avg = avg1+smoothstep((y-yvect*caseSize)/caseSize)*(avg2-avg1)
            plane[x][y]+=avg

def perlinNoiseComposition(plane,gridSizeList,factorList):
    t=ti.time()
    n=len(plane)
    factorIndex=0
    for gridSize in gridSizeList:
        caseSize=n//gridSize
        vectMatrix=[[randomUnitVector() for x in range (gridSize+3)] for y in range (gridSize+3)]
        for x in range(n):
            for y in range(n):
                xvect=int(x/caseSize)
                yvect=int(y/caseSize)
                a= dotproduct((x-xvect*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect][yvect][0], vectMatrix[xvect][yvect][1])
                b= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect+1][yvect][0], vectMatrix[xvect+1][yvect][1])
                c= dotproduct((x-xvect*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect][yvect+1][0], vectMatrix[xvect][yvect+1][1])
                d= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect+1][yvect+1][0], vectMatrix[xvect+1][yvect+1][1])
                avg1 = a+smoothstep((x-xvect*caseSize)/caseSize)*(b-a)
                avg2 = c+smoothstep((x-xvect*caseSize)/caseSize)*(d-c)
                avg = avg1+smoothstep((y-yvect*caseSize)/caseSize)*(avg2-avg1)
                plane[x][y]+=avg*factorList[factorIndex]
        factorIndex+=1
        print(ti.time()-t)

## postprocessing

def minmax(M):      #calculates extrem valueas of a plane
    minValue=1
    maxValue=-1
    for x in range(len(M)):
        for y in range(len(M)):
            if M[x][y]<minValue:
                minValue=M[x][y]
            if M[x][y]>maxValue:
                maxValue=M[x][y]
    return (minValue,maxValue)

def plateauTransform(plane,nbPlateau):      #nice little effect that makes little plateaus
    (minValue,maxValue)=minmax(plane)
    heightDifference=maxValue-minValue
    plateauHeight=heightDifference/nbPlateau
    for x in range(len(plane)):
        for y in range(len(plane)):
            plane[x][y]=int(plane[x][y]/plateauHeight)*plateauHeight

def plateauTransformv2(plane,nbPlateau):
    plateauHeight=2/nbPlateau
    for x in range(len(plane)):
        for y in range(len(plane)):
            plane[x][y]=int(plane[x][y]/plateauHeight)*plateauHeight

def plateauTransformv3(plane,nbPlateau,maxheight):
    n=len(plane)
    plateauHeight=2*maxheight/nbPlateau
    for x in range(len(plane)):
        for y in range(len(plane)):
            plane[x][y]=int(plane[x][y]/plateauHeight)*plateauHeight
    plane[0][0]=-0.35*maxheight
    plane[n-1][n-1]=0.35*maxheight

def scale(plane,alpha):     #scale a map by a certain factor
    for x in range(len(plane)):
        for y in range(len(plane)):
            plane[x][y]=alpha*plane[x][y]

def absolutTransform(plane):                # makes little valleys
    for x in range(len(plane)):
        for y in range(len(plane)):
            plane[x][y]=abs(plane[x][y])

def firstDerivativ(plane):      #derivates the terrain, looks funny I guess
    derivedPlane=[[0 for x in range (len(plane))] for y in range (len(plane))]
    for x in range(1,len(plane)-1):
        for y in range(1,len(plane)-1):
            derivedPlane[x][y]=plane[x+1][y]+plane[x][y+1]-plane[x-1][y]-plane[x][y-1]
    return derivedPlane

## flowmap

def particleTravel1Step(plane,x,y):
    n=len(plane)
    neighbours=[plane[(x+1)%n][y%n],plane[x%n][(y+1)%n],plane[(x-1)%n][y%n],plane[x%n][(y-1)%n],plane[x%n][y%n]]
    minVal=neighbours[0]
    minIndex=0
    for i in range(5):
        if neighbours[i]<minVal:
            minVal=neighbours[i]
            minIndex=i
    if minIndex == 0:
        return (x+1,y,minIndex)
    if minIndex == 1:
        return (x,y+1,minIndex)
    if minIndex == 2:
        return (x-1,y,minIndex)
    if minIndex == 3:
        return (x,y-1,minIndex)
    if minIndex == 4:
        return (x,y,minIndex)

def particleTravel1Stepv2(plane,x,y):
    n=len(plane)
    neighbours=[plane[(x+1)%n][y%n],plane[x%n][(y+1)%n],plane[(x-1)%n][y%n],plane[x%n][(y-1)%n],(plane[(x+1)%n][(y+1)%n])*0.7071067811865475,(plane[(x-1)%n][(y+1)%n])*0.7071067811865475,(plane[(x-1)%n][(y-1)%n])*0.7071067811865475,(plane[(x+1)%n][(y-1)%n])*0.7071067811865475,plane[x%n][y%n]]
    minVal=neighbours[0]
    minIndex=0
    for i in range(9):
        if neighbours[i]<minVal:
            minVal=neighbours[i]
            minIndex=i
    if minIndex == 0:
        return (x+1,y,minIndex)
    if minIndex == 1:
        return (x,y+1,minIndex)
    if minIndex == 2:
        return (x-1,y,minIndex)
    if minIndex == 3:
        return (x,y-1,minIndex)
    if minIndex == 4:
        return (x+1,y+1,minIndex)
    if minIndex == 5:
        return (x-1,y+1,minIndex)
    if minIndex == 6:
        return (x-1,y-1,minIndex)
    if minIndex == 7:
        return (x+1,y-1,minIndex)
    if minIndex == 8:
        return (x,y,minIndex)

def particleTravel(plane,flowplane,x0,y0):
    n=len(plane)
    x=x0
    y=y0
    stop = False
    while stop == False:
        (x,y,i)=particleTravel1Stepv2(plane,x,y)
        if i == 8 or rd.random()<0.01 :
            stop = True
        flowplane[x%n][y%n]+=1

def flowPlane(plane,density):
    flowplane=[[20 for x in range (len(plane))] for y in range (len(plane))]
    for x in range(2,len(plane)-1):
        for y in range(len(plane)):
            if rd.random()<density:
                particleTravel(plane,flowplane,x,y)
    for x in range(len(plane)):
        for y in range(len(plane)):
            flowplane[x][y]=min(ma.log((flowplane[x][y])),500)
    return flowplane



## animate it

def randomUnitVectorv2():
    phi=rd.random()*2*ma.pi
    return [ma.cos(phi),ma.sin(phi),phi]

def turnUnitVector(phi,addedAngle):
    addedAngle*=ma.pi/180
    return [ma.cos(phi+addedAngle),ma.sin(phi+addedAngle),phi+addedAngle]




def animatedNoise(plane,gridSize):
    t=ti.time()
    n=len(plane)
    caseSize=n//gridSize
    vectMatrix=[[randomUnitVectorv2() for x in range (gridSize+2)] for y in range (gridSize+2)]
    turnSpeedMatrix=[[rd.choice([-2,-1,1,2]) for x in range (gridSize+2)] for y in range (gridSize+2)]
    for i in range(72):
        for x in range(n):
            for y in range(n):
                xvect=int(x/caseSize)
                yvect=int(y/caseSize)
                a= dotproduct((x-xvect*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect][yvect][0], vectMatrix[xvect][yvect][1])
                b= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect+1][yvect][0], vectMatrix[xvect+1][yvect][1])
                c= dotproduct((x-xvect*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect][yvect+1][0], vectMatrix[xvect][yvect+1][1])
                d= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect+1][yvect+1][0], vectMatrix[xvect+1][yvect+1][1])
                avg1 = a+smoothstep((x-xvect*caseSize)/caseSize)*(b-a)
                avg2 = c+smoothstep((x-xvect*caseSize)/caseSize)*(d-c)
                avg = avg1+smoothstep((y-yvect*caseSize)/caseSize)*(avg2-avg1)
                plane[x][y] = avg
        plateauTransformv2(plane,25)
        plt.matshow(P)
        plt.savefig('C:/Users/hugob/Desktop/studies/Polytechnique/Python&saucisson/visuals/noise frames/fig'+str(i)+'.png')
        for j in range(len(vectMatrix)):
            for k in range (len(vectMatrix)):
                vectMatrix[j][k]=turnUnitVector(vectMatrix[j][k][2],turnSpeedMatrix[j][k]*5)
        print(ti.time()-t)
    plt.clf()




def animatedComposedNoise(plane,gridSizeList,factorList):
    maxheight=sum(factorList)   #calculate the potential max height of the plane
    t=ti.time()
    n=len(plane)
    vectMatrixList=[]           #List of Matrixes for random vectors
    turnSpeedMatrixList=[]      #List of Matrixes for random vectors turn speeds
    for gridSize in gridSizeList:   #here the mentioned listes are filled with random values
        vectMatrixList.append([[randomUnitVectorv2() for x in range (gridSize+3)] for y in range (gridSize+3)])
        turnSpeedMatrixList.append([[rd.choice([-2,-1,1,2]) for x in range (gridSize+3)] for y in range (gridSize+3)])
    for i in range(72):         # We use 72 frames to make a loop
        Index=0           # this index is used to now on which gridSize we work on
        plane=[[0 for x in range(n)] for y in range(n)]     #restes the Plane for each frame
        for gridSize in gridSizeList:   #loops through the gridsizes
            caseSize=n//gridSize        #calculates the size of a case in th grid
            vectMatrix=vectMatrixList[Index]    #Seizes the grid we need to work on
            for x in range(n):
                for y in range(n):      #loops through all points of the plane
                    xvect=int(x/caseSize)
                    yvect=int(y/caseSize)   #associates gridcoordinates of the vectors for a given point x,y
                    a= dotproduct((x-xvect*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect][yvect][0], vectMatrix[xvect][yvect][1])
                    b= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-yvect*caseSize)/caseSize, vectMatrix[xvect+1][yvect][0], vectMatrix[xvect+1][yvect][1])
                    c= dotproduct((x-xvect*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect][yvect+1][0], vectMatrix[xvect][yvect+1][1])
                    d= dotproduct((x-(xvect+1)*caseSize)/caseSize, (y-(yvect+1)*caseSize)/caseSize, vectMatrix[xvect+1][yvect+1][0], vectMatrix[xvect+1][yvect+1][1])
                    avg1 = a+smoothstep((x-xvect*caseSize)/caseSize)*(b-a)
                    avg2 = c+smoothstep((x-xvect*caseSize)/caseSize)*(d-c)
                    avg = avg1+smoothstep((y-yvect*caseSize)/caseSize)*(avg2-avg1)
                    plane[x][y] += avg*factorList[Index]    #Here we apply th Perlin-noise algorithm
            Index+=1    #increments the Index to work on the next gridSize
        plateauTransformv3(plane,25,maxheight)  #adds some nice little plateau-effects
        plt.matshow(plane)
        plt.savefig('C:/Users/hugob/Desktop/studies/Polytechnique/Python&saucisson/visuals/noise frames/fig'+str(i)+'.png') #saving the image in a folder
        for m in range(len(gridSizeList)): #Here we make each vecor of the grid turn a bit to get ready for the next frame
            for j in range(len(vectMatrixList[m])):
                for k in range (len(vectMatrixList[m])):
                    vectMatrixList[m][j][k]=turnUnitVector(vectMatrixList[m][j][k][2],turnSpeedMatrixList[m][j][k]*5)
        print(ti.time()-t)
    plt.clf()



"""
Sucess!
Here is an example to execute: animatedComposedNoise(P,[3,7,15],[10,4,1.5])
(you just need the folder adress to be existant)

use this website to make a gif out of the images: https://ezgif.com/maker
"""





## to c++ vector

def MatrixToCppVector(M):
    n= len(M)
    vstring = ""
    for i in range(n):
        l = str(M[i])
        vstring +="{"
        vstring += l[1:-1]
        vstring +="},"
    return vstring































