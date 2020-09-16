# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out
# how many cakes he could bake considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) 
# and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units 
# for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

#testing code
#import math

# def cakes(recipe, available):
#     amounts = []
#     for key, value in available.items():
#         if key in recipe:
#             print(f'{value} of the {key} gives us', available[key]/recipe[key], 'times the recipe.')
#             #storing tuples of key and associated amounts
#             amounts.append((available[key]/recipe[key]))
#     #take the minimum amount, since fewest ingredient limits the number of batches
#     print(math.floor((min(amounts))))

import math

def cakes(recipe, available):
    amounts = []
    #first check to see we have all ingredients we need
    for key in recipe:
        if key not in available:
            return 0
        else:
            for key, value in available.items():
                if key in recipe:
                    #storing associated amounts
                    amounts.append((available[key]/recipe[key]))
            #take the minimum amount, since fewest ingredient limits the number of batches
    return (math.floor(min(amounts)))




recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
cakes(recipe, available) #2

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available)


#MUCH SIMPLER VERSION

def cakes_v2(recipe, available):
    return int(min(available.get(k, 0)/recipe[k] for k in recipe))
    #this uses a default argument for available.get ( k , OR 0 if not in available)


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
cakes_v2(recipe, available)#2

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes_v2(recipe, available) #0
