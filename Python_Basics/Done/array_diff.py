# difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.

#original
def array_diff(a, b):
    final=[]
    for l in a:
        if len(a)==0:
            final=b
        elif l not in b:
            final.append(l)
    return final


# array_diff([1,2], [1]) # [2]
# array_diff([1,2,2], [1])# [2,2]
# array_diff([1,2,2], [2])# [1]
# array_diff([1,2,2], [])# [1,2,2]
# array_diff([], [1,2])# []