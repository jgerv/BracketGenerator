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

#gets the number of sets in a current round
def getNumSets(currentRoundEntrants):
    return currentRoundEntrants / 2


class Round:
    roundEntrants = []
    roundNumSets = 0
    winners = []
    losers = []

    def setRoundEntrants(length, entrantList):
        for i in range(length):
            roundEntrants.append(entrantList[i])
        return roundEntrants
        
        

class Entrant:
    def __init__(self, name, seed):
        self.name = name
        self.seed = seed

            

def main():
    rounds = []     #list of Round 
    numEntrants = 0 #number of entrants in the tournament
    nameEntrants = [] #list of the names of the entrants
    currentRoundEntrants = [] #the names of the entrants in the current round
    placeholder = "" #placeholder to put names into list
    numSets = 0 #number of sets to be played in current round
    currRound = 1 #current round the bracket is in(starts at 1 not 0)
    numByes = 0 
    numRounds = 0
    
    numEntrants = input("How many entrants will there be? ")

    numByes = findNumByes(numEntrants)
    numSets = (numEntrants - numByes) / 2
    numRounds = findNumRounds(numEntrants)

    #rounds.append(Round('nice', 3,))
    #print(rounds[0].roundNumSets)

    for i in range(numEntrants):
        placeholder = input("Seed " + str(i + 1) + ": ")
        nameEntrants.append((Entrant(placeholder, i + 1)))

    rounds.insert(0, Round())
    print(rounds[0].roundEntrants)
    rounds[0].setRoundEntrants(numEntrants, nameEntrants) 

    #gets the entrants into a list of the current round the tournament is in 
    #for i in range(numByes, len(nameEntrants)):
     #   rounds.insert(0, Round(nameEntrants[i], getNumSets(len(nameEntrants)- numByes)))

    #for i in range(numByes):
     #   rounds.insert(1, Round(nameEntrants[i], getNumSets(len(nameEntrants) - numByes)))

    #print(rounds[0].roundNumSets)
   

    #for i in range(len(rounds[0].roundEntrants)):
     #   print(rounds[0].roundEntrants[i])

    #need to figure out a way to iterate throughout the currentRoundEntrants no matter the size
    #iterates throughout the whole tournament, i is the currentround on
#    for i in range(numRounds):
 #       print("Round ", i + 1, ":")
  #      for j in range(numSets):
   #         print(currentRoundEntrants[0], "plays ", currentRoundEntrants[-1])
    #        currentRoundEntrants.pop(0)
     #       currentRoundEntrants.pop(-1)
          
        
        
        
        



main()
        
            
