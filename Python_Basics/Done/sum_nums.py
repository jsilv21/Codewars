# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. 
# If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

#identify max number
#get all nums between ? not sure how to do this
#do we need abs value for negative?

# def get_sum(a,b):
#     nums = [a,b]
#     num_range = range(min(nums),max(nums))
#     if a==b:
#         return a
#     else:
#         return num_range

def get_sum(a,b):
    if a != b:
        numrange = [*range(min(a,b),(max(a,b)+1))]
        print('range is: ', numrange)
        print('sum is: ', sum(numrange))
    else: 
        print('nums are the same: ', a)

get_sum(1, 0)# == 1   // 1 + 0 = 1
get_sum(1, 2)# == 3   // 1 + 2 = 3
get_sum(0, 1)# == 1   // 0 + 1 = 1
get_sum(1, 1)# == 1   // 1 Since both are same
get_sum(-1, 0)# == -1 // -1 + 0 = -1
get_sum(-1, 2)# == 2  // -1 + 0 + 1 + 2 = 2


