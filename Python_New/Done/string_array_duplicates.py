# #https://www.codewars.com/kata/59f08f89a5e129c543000069
# In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

# For example:

# dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

# dup(["kelless","keenness"]) = ["keles","kenes"].

# Strings will be alphabet characters only. Don't worry about lower and upper case. See test cases for more examples.

# Good luck!


def dup(array):
    final_list = []
    for word in array:
        prev_val = None
        new_word = ''
        for letter in word:
            if letter != prev_val:
                new_word+=letter
                prev_val=letter
        final_list.append(new_word)
    return final_list

dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"])#['codewars','picaniny','hubububo'])
#dup(["abracadabra","allottee","assessee"])#['abracadabra','alote','asese'])
#dup(["kelless","keenness"])#['keles','kenes'])

#advanced solution
from itertools import groupby

def duplicate(array):
    return ["".join(c for c, grouper in groupby(i)) for i in array]
