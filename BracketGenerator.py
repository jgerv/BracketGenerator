import math

#checks if x is logbase 2
def Log2(x):
    if x == 0:
        return false;
    return (math.log10(x)/math.log10(2));

#checks if n is a power of two
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)));

#function to find the number of byes in a tournament
def findNumByes(num):
    countUp = 0
    countDown = 0
    if(isPowerOfTwo(num)):
        return 0
    else:
        while(~isPowerOfTwo(num + countUp) & ~isPowerOfTwo(num - countDown)):
            countUp = countUp + 1
            countDown = countDown + 1
            if(isPowerOfTwo(num + countUp)):
                return countUp
            elif(isPowerOfTwo(num - countDown)):
                return countDown

#function to find the number of rounds in a tournament
def findNumRounds(num):
    if(isPowerOfTwo(num)):
        return int(math.log(num) / math.log(2))
    else:
        return int(math.log(num) / (math.log(2)) + 1)
            

def main():
    numEntrants = 0 #number of entrants in the tournament
    nameEntrants = [] #list of the names of the entrants
    placeholder = "" #placeholder to put names into list
    numSets = 0 #number of sets to be played in current round
    currRound = 1 #current round the bracket is in(starts at 1 not 0)
    numByes = 0 
    numRounds = 0
    
    numEntrants = input("How many entrants will there be? ")

    numByes = findNumByes(numEntrants)
    numSets = (numEntrants - numByes) / 2
    numRounds = findNumRounds(numEntrants)
    print(numRounds)
    print(numByes)
    print(str(numSets) + " sets in the " + str(currRound) + " round to be played")

    for i in range(numEntrants):
        placeholder = input("Seed " + str(i + 1) + ": ")
        nameEntrants.append(placeholder)

    for i in range(len(nameEntrants)):
        print(nameEntrants[i])

        
        



main()
        
            
