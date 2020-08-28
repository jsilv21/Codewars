#Check to see if a string has the same amount of 'x's and 'o's. 
#The method must return a boolean and be case insensitive. 
#The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

    #create counter for X & os
    #iterate over string, 
    # increment each counter for X & O
    #check if they're equal
    #final else - false (if no X & Os)

def xo(s):
    x_count = 0
    o_count = 0 
    for letter in s:
        if letter == 'x' or letter == 'X':
            x_count+=1
        elif letter == 'o' or letter == 'O':
            o_count+=1
    if x_count == o_count:
        return True
    else: 
        return False

print(xo('xo')) #true
print(xo('xo0')) #true
print(xo("zpzpzpp")) #true
print(xo("zzoo")) #false