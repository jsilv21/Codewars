# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.


#first attempt

def disemvowel(string):
    vowels = ['a','e','i','o','u', 'A', "E", "I", "O", "U"]
    newstr =''
    for x in string:
        if x not in vowels:
            newstr+=x
    return newstr
    
    # print(str([''.join(x) for x in string if x not in vowels]))

disemvowel("This website is for losers LOL!")


#smaller code solution
def disemvowel_v2(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

    #had this part right, my .join needed a parenthesis - that's why i was having issues. 
    #also wanted .lower on the If statement, not in the first string call.