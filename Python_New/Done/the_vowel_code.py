# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5

# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.
# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
# For example, decode("h3 th2r2") would return "hi there".
# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

def encode(st):
    newmsg=''
    vowel = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5
    }
    for l in st:
        if l in vowel:
            newmsg+=str(vowel[l])
        else:
            newmsg+=l
    st=newmsg
    return st


def decode(st):
    newmsg=''
    reverse = {
        '1': 'a',
        '2': 'e',
        '3': 'i',
        '4': 'o',
        '5': 'u'
    }
    for l in st:
        if l in reverse:
            newmsg+=str(reverse[l])
        else:
            newmsg+=l
    st=newmsg
    return st

encode('hello')# 'h2ll4')
encode('How are you today?')# 'H4w 1r2 y45 t4d1y?')
encode('This is an encoding test.')# 'Th3s 3s 1n 2nc4d3ng t2st.')
decode('h2ll4')# 'hello')


#MUCH EASIER METHOD
#Using "maketrans"

def encode_v2(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode_v2(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)

encode_v2('hello')# 'h2ll4')
encode_v2('How are you today?')# 'H4w 1r2 y45 t4d1y?')
encode_v2('This is an encoding test.')# 'Th3s 3s 1n 2nc4d3ng t2st.')
decode_v2('h2ll4')# 'hello')
