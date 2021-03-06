#include <iostream>
#include <bits/stdc++.h>
#include <vector>
using namespace std;

//boolean to see if a number is a power of two, ex 8 is and 7 is not
bool isPowerOfTwo(int number)
{
    return (ceil(log2(number)) == floor(log2(number)));
}

//finds the number of byes
int findNumberByes(int number)
{
    int countUp, countDown = 0;
    if(isPowerOfTwo(number)){
        return 0; 
    }
    else{
	while(!isPowerOfTwo(number + countUp) && !isPowerOfTwo(number - countDown)){
	    countUp++;
	    countDown++;
	    if(isPowerOfTwo(number + countUp)){
	        return countUp;
	    }
	    else if(isPowerOfTwo(number - countDown)){
	        return countDown;
	    }
	}
    }
    return 0;
}

int findNumRounds(int number)
{
    if(isPowerOfTwo(number))
	return log(number) / log(2);
    else
        return log(number) / (log(2)) + 1;
}

int main(){
    int numEntrants; //number of entrants entered into the tournament 
    vector<string> nameEntrants; //list of the names of the entrants
    string placeholder; //placeholder to put names into vector
    int numSets = 0; //number of sets to be played in current round
    int currRound = 1; //current round the bracket is in
    int numByes = 0;
    int numRounds = 0;
    vector<vector<string>> rounds;

    cout << "How many entrants will there be? ";
    cin >> numEntrants;

    numByes = findNumberByes(numEntrants);
    numSets = (numEntrants - numByes) / 2;
    numRounds = findNumRounds(numEntrants);
    cout << numRounds << endl;
    cout << numByes << endl;
    cout << numSets << " sets in the " << currRound << " round to be played" << endl;

    for(int i = 0; i < numEntrants; i++)
    {
        cout << "Seed " << i + 1 << ": ";
	cin >> placeholder;
	nameEntrants.push_back(placeholder);
    }

    for(int i = 0; i < numEntrants; i++)
    {
	vector<string> myVec;
	myVec.push_back(nameEntrants[i]);
	rounds.push_back(myVec);
    }

    return 0;
}
