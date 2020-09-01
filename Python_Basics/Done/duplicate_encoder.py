# The goal of this exercise is to convert a string to a new string where each character in the new string is 
# "(" if that character appears only once in the original string, or ")" if that character appears more than 
# once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    convert = word.lower()
    finalstring=''
    for l in convert:
        if convert.count(l)>1:
            finalstring+=")"
        else:
            finalstring+="("
    return finalstring


duplicate_encode("din") # "((("
duplicate_encode("recede") # "()()()"

#cleaner solution
def duplicate_encode_v2(word):
    word = word.lower()
    return ''.join('(' if word.count(x) == 1 else ')' for x in word)