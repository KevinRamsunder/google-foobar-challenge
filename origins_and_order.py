import itertools

def answer(x, y, z):
    good_dates = []
    list_of_dates = list(set(itertools.permutations([x,y,z])))
    months = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    for date in list_of_dates:
        if not (date[0] < 1 or date[0] > 12 or \
            date[1] < 1 or date[1] > months[date[0]] or \
            date[2] < 1 or date[2] > 99):
            good_dates.append(date)

    if len(good_dates) == 1:
        return str('%02d' % good_dates[0][0]) + '/' + \
               str('%02d' % good_dates[0][1]) + '/' + \
               str('%02d' % good_dates[0][2])
    else:
        return 'Ambiguous'