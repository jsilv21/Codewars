# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python
# You need to write regex that will validate a 
# password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.




import re

text_to_search = "fjd3IR9"

""" 
quantifiers
* - 0 or more
+ - 1 or more
? - 0 or One
{3} - Exact number
{3,4} - Range of numbers (min, max)
"""


pattern = re.compile(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[a-zA-Z\d]{6,}$")

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# SAVED REGEX - https://regex101.com/r/FcmJX8/2

# print(bool(search(regex, 'fjd3IR9')))# True
# print(bool(search(regex, 'ghdfj32')))# False
# print(bool(search(regex, 'DSJKHD23'))) # False