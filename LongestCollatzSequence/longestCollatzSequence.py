import time

def lengthOfCollatzSequence(startingNumber):
    length = 1
    while startingNumber > 1:
        if startingNumber % 2 == 0:
            startingNumber = startingNumber/2
            length += 1
        else:
            startingNumber = (3*startingNumber)+1
            length += 1
    return length
        
def lengthChecker(startingNumber):
    longestLength = lengthOfCollatzSequence(startingNumber)
    num = startingNumber
    while(startingNumber > 1):
        startingNumber -= 1
        length = lengthOfCollatzSequence(startingNumber)
        if(length > longestLength):
            longestLength = length
            num = startingNumber
    print("Starting Number = ",num)
    print("Length of the sequence = ",longestLength)
            
startTime = time.time()
startingNumber = 1000000
lengthChecker(startingNumber)
print("--- %s seconds ---" % (time.time() - startTime))