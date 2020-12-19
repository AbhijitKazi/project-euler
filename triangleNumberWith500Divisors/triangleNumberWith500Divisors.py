import math

def numOfDiv(triangleNum):
    divNum = 0
    if triangleNum == 1:
        divNum = 1
    else:
        numSqrt =int(math.sqrt(triangleNum))
        for i in range(1,numSqrt+1):
            if triangleNum % i:
                divNum += 2
        if numSqrt * numSqrt == triangleNum:
            divNum += 1
    return divNum
                
            

triangleNum = 1
currentNum = 2
target = 500
numOfDivisors = 0

numOfDivisors = numOfDiv(triangleNum)

while numOfDivisors < target:
    triangleNum += currentNum;
    currentNum += 1
    numOfDivisors = numOfDiv(triangleNum)
    
print ("Triangle Number ",triangleNum)






