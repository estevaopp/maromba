def calcGET(tmb, activity):
    if activity:
        return ((tmb * 1.7))
    else:
        return (tmb * 1.2)


def calcProtein(weight):
    return (weight*2.5)


def calcFat(weight):
    return weight


def calcTMB(height, weight, age, gender):
    if gender == 'M':
        return (66 + (13.8 * weight) + (5.0 * height) - (6.8 * age))
    elif gender == 'F':
        return (655 + (9.6 * weight) + (1.9 * height) - (4.7 * age))


