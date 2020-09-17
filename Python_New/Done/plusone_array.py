# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python
# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

# the array can't be empty
# only non-negative, single digit integers are allowed
# Return nil (or your language's equivalent) for invalid inputs.

# Examples
# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

# [4, 3, 2, 5] would return [4, 3, 2, 6]

def up_array(arr):
    if len(arr) != 0: #handle empty lists
        for item in arr:
            if len(str(item))>1: #check for double digits (not allowed)
                return None
        try:
            #map each element back into string, then convert to int
            newstr2 = int(''.join(map(str, arr)))+1
            final_list = []
            #convert back to string for iteration
            for i in str(newstr2):
                final_list.append(int(i)) #need back in int
            return final_list
        #handling for cases that don't work
        except ValueError:
            None
    else:
        None


up_array([2,3,9])# [2,4,0]
up_array([4,3,2,5])# [4,3,2,6]
up_array([1,-9])# None
up_array([10, 10, 3, 8, 10, 3]) #None


#MUCH CLEANER SOLUTION
def up_array_v2(arr):
    if not arr or min(arr) < 0 or max(arr) > 9:
        return None
    else:
        return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]