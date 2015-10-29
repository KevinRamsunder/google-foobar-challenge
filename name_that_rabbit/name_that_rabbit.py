def answer(names):
    names.sort(reverse=True)
    output = [length(names[i]) for i in range(len(names))]
    
    pairs = [(output[i], names[i]) for i in range(len(names))]
    pairs.sort(reverse=True) 

    return [pairs[i][1] for i in range(len(pairs))]

def length(name):
    i = 0
    for letter in name:
        i += ord(letter) - 96
    
    return i