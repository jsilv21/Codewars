# https://www.codewars.com/kata/5375f921003bf62192000746/train/python

# The word i18n is a common abbreviation of internationalization in the developer community, 
# used instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

# Write a function that takes a string and turns any and all "words" (see below) within that string of length 4 or greater into an abbreviation, following these rules:

# A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") 
# will split up a series of letters into two words (eg. "elephant" and "ride").
# The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "elephant ride" => "e6t r2e").

import re

def abbreviate(s):
    #need to handle for non-alphanumeric delimiters
    s = re.split("([\W\d\_])", s)
    newword=[]
    for word in s:
        #handle for the exclamation
        if len(word)>3 and '!' not in word:
        #need to take first and last letters, then add the number of skipped
            newword.extend([word[0], len(word)-2, word[-1]])
        else:
            newword.extend(word)
    final = "".join(map(str, newword))
    return final



abbreviate("internationalization")# "i18n"
abbreviate("accessibility")# "a11y"
abbreviate("elephant-rides are really fun!") #"e6t-r3s are r4y fun!"
abbreviate("Accessibility")# "A11y"
abbreviate("elephant-ride")# "e6t-r2e"

abbreviate("double-barreled cat'on'is: the'a5doggy'cat-") # "d4e-b6d cat'on'is: the'a5d3y'cat-"
abbreviate("balloon; balloon double-barreled5monolithic_") # "b5n; b5n d4e-b6d5m8c_"


# SIMPLER SOLUTION

import re

regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate_v2(s):
    return regex.sub(replace, s)