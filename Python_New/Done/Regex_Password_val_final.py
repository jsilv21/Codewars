# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python
# You need to write regex that will validate a 
# password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
# Valid passwords will only be alphanumeric characters.

#https://regex101.com/r/FcmJX8/3

regex="^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[a-zA-Z\d]{6,}$"


#A BIT CLEARER

regex_v2 = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)