def answer(x):
    count = 0
    dictionary = {}
    list_one = list(set(x)) # remove duplicates
    list_two = [list_one[i][::-1] for i in range(len(list_one))]

    for item in list_one:
        dictionary[item] = 0

    for item in list_two:
        if item in dictionary and item != item[::-1]:
            dictionary[item] += 1
            count += 1
    
    return(len(list_one) - count / 2)