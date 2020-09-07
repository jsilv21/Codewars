def high(x):
    words=x.split(' ')
    list = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
    return words[list.index(max(list))]

high('man i need a taxi up to ubud') #taxi
high('what time are we climbing up the volcano') #volcano