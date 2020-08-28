# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    return(int((''.join(str(int(i)**2) for i in str(num)))))

square_digits(9119)

#While above is good, it's probably a bit confusing to read

#easier to read

def square_digits_v2(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)

square_digits_v2(9119)