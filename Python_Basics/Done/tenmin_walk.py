def is_valid_walk(walk):
    position=[0,0,0,0]
    print(len(walk))
    if len(walk) == 10:
        for val in walk:
            if val == 'n':
                position[0]+=1
            elif val == 's':
                position[1]+=1
            elif val == 'e':
                position[2]+=1
            elif val == 'w':
                position[3]+=1
        if position[0] == position [1] and position [2] == position[3]:
            return True
        else:
            return False
    else:
        return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))