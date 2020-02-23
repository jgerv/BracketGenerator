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
#finds the closest power of two > num and subtracts num from it to get the numByes
def findNumByes(num):
    countUp = 0
    countDown = 0
    if(isPowerOfTwo(num)):
        return 0
    else:
        while(~isPowerOfTwo(num + countUp)):
            countUp = countUp + 1
            countDown = countDown + 1
            if(isPowerOfTwo(num + countUp)):
                return countUp

#function to find the number of rounds in a tournament
def findNumRounds(num):
    if(isPowerOfTwo(num)):
        return int(math.log(num) / math.log(2))
    else:
        return int(math.log(num) / (math.log(2)) + 1)

#gets the number of sets in a current round
def getNumSets(currentRoundEntrants):
    return currentRoundEntrants / 2



#class Entrant(object):
class Entrant:
    def __init__(self, name, seed):
        self.name = name
        self.seed = seed


#class Round(Entrant):
class Round:    
    roundEntrants = []
    winners = []
    losers = []
    #def __init__(self, name, seed, roundEntrants, winners, losers):
    #super(Round, self).__init__(name, seed)
    #    self.roundEntrants = roundEntrants
     #   self.winners = winners
    #    self.losers = losers
  
    #sets the entrants in the round
    def setRoundEntrants(self, start, end, entrantList):
        for i in range(start, end):
            self.roundEntrants.append(entrantList[i])
        return self.roundEntrants

    #displays the names of the entrants in the current round
    def displayRoundEntrants(self):
        for entrant in self.roundEntrants:
            print(entrant.name)

    #adds a winner to winners
    def addWinner(self, entrant):
        self.winners.append(entrant)
        return self.winners

    #removes an entrant from roundEntrants
    def removeEntrant(self, entrant):
        self.roundEntrants.remove(entrant)

    #prints out the winners of the current round
    def displayWinners(self):
        for entrant in self.winners:
            print(entrant.name)

    #prints out the losers of the current round
    def displayLosers(self):
        for entrant in self.losers:
            print(entrant.name)

    def getWinners():
        return winners

    def getRoundEntrants():
        return roundEntrants
        
        


            

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
    print(numByes)
    numSets = (numEntrants - numByes) / 2
    numRounds = findNumRounds(numEntrants)

    #inputs all the entrants in the bracket and puts it into a list
    for i in range(numEntrants):
        placeholder = input("Seed " + str(i + 1) + ": ")
        nameEntrants.append((Entrant(placeholder, i + 1)))

   # rounds.insert(0, Round())
   # rounds[0].setRoundEntrants(0, numEntrants, nameEntrants)
    #rounds[0].displayRoundEntrants()
    #print(rounds[0].roundEntrants[0].name)
    

    #gets the entrants into a list of the current round the tournament is in 
    #for i in range(numByes, len(nameEntrants)):
     #   rounds.insert(0, Round(

    #rounds[0].displayRoundEntrants()
    #for i in range(numByes):
     #   rounds.insert(1, Round(nameEntrants[i], getNumSets(len(nameEntrants) - numByes)))

    #print(rounds[0].roundNumSets)
   

    #for i in range(len(rounds[0].roundEntrants)):
     #   print(rounds[0].roundEntrants[i])
    #byes only happen in the first round
    rounds.insert(i, Round())
    rounds[0].setRoundEntrants(0, numEntrants, nameEntrants)

    #print(numByes)
    for i in range(numByes):
        rounds[0].addWinner(rounds[0].roundEntrants[i])
        
    rounds[0].displayRoundEntrants()
    for i in range(len(rounds[0].winners)):
        if(rounds[0].winners[i] in rounds[0].roundEntrants):
            rounds[0].removeEntrant(rounds[0].winners[i])
    rounds[0].displayRoundEntrants()
            
    #for i in range(numByes):
        #rounds[0].removeEntrant(rounds[0].roundEntrants[0])
    #rounds[0].displayRoundEntrants()
    #need to figure out a way to iterate throughout the currentRoundEntrants no matter the size
    #iterates throughout the whole tournament, i is the currentround on
    for i in range(1,numRounds):
        rounds.insert(i, Round())
        rounds[i].setRoundEntrants(numByes,numEntrants, nameEntrants)
       # print("Round ", i + 1, ":")
       # for j in range(len(rounds[i].roundEntrants)):
            #print(rounds[i].roundEntrants, "plays ", currentRoundEntrants[-1])
        #    currentRoundEntrants.pop(0)
        #    currentRoundEntrants.pop(-1)
          
        
        
        
        



main()
        
            
