# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

def find_it(seq):
    num=0
    for x in seq:
        if ((seq.count(x))%2!=0) and x != num:
            num = x
    return num

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5

#pretty clever solution

def find_it_v2(seq):
    return [x for x in seq if seq.count(x) % 2][0] #this selects the first element in the list that you get - takes care of duplicates.