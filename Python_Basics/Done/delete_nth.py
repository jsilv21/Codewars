#Task
#Given a list lst and a number N, create a new list that contains each number of lst 
# at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] 
# since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].


# notes before attempting...
# take list
#iterate over item
#if count is past max_e, strip remainder
#create new list to append to... maybe establish an ignore value so it doesn't keep appending values?


def delete_nth(order, max_e):
    final_list = []
    for element in order:
        if final_list.count(element)<max_e:
            final_list.append(element)
    return final_list

delete_nth([20,37,20,21], 1)# [20,37,21]
delete_nth([1,1,3,3,7,2,2,2,2], 3)# [1, 1, 3, 3, 7, 2, 2, 2]


