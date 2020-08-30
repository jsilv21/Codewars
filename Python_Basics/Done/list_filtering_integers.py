# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

#first pass - longer form

# def filter_list(l):
#     final_list=[]
#     for x in l:
#         if isinstance(x, int):
#             final_list.append(x)
#     return final_list

# filter_list([1,2,'a','b'])
# filter_list([1,'a','b',0,15])


#one liner

def filter_list(l):
    return [i for i in l if not isinstance(i, str)]
