# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

#WORKING CODE

#pulling in a dictionary of a-z to start the scoring system

import string
d = dict.fromkeys(string.ascii_lowercase,1)

# iterating over dict to update values. Have to create a list of the keys, then find index, then add 1. 
# this gives the 1-26 score values.

for key in d:
    d[key] = list(d.keys()).index(key)+1

# main function
def high(x):
    highscore=0
    #split the x string, iterate over words
    for word in x.split():
        wordscore=0
        #iterate over letters in the word
        for letter in word:
            #update 'newscore' to aggregate word score
            wordscore +=d[letter]
            #comparing for best score
            if wordscore > highscore:
                highscore = wordscore
                highword = word #store the corresponding word
    return highword

high('man i need a taxi up to ubud') #taxi
high('what time are we climbing up the volcano') #volcano