#Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second 
# character of the final pair with an underscore ('_').


def solution(s):
    new_lst = []
    #if not divisible by 2, add on "_" to s string
    if len(s) % 2 != 0:
        s += "_"
    #iterate over range to get splits of 2
    for i in range(0, len(s), 2):
        new_lst.append(s[i : i + 2])
    return new_lst


print(solution("abcd"))  # == ['ab', 'cd']
print(solution("abc"))  # == ['ab', 'c_']
