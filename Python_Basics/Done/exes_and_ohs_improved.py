#improved logic for exes_and_ohs test.
# #1 - Instead of doing both cases, convert to lower w s.lower()
# #2 - you can evaluate the bool in one expression, don't even need the for loop. Just count the (s) in string.

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('xo')) #true
print(xo('xo0')) #true
print(xo("zpzpzpp")) #true
print(xo("zzoo")) #false