"""
    write an algorithm that returns the values of an array that are not odd
"""

def returnNotOdds(array):
    notOddArray = []
    if len(array) == 0:
        return notOddArray
    for element in array:
        if not element%2 == 0:
            continue
        else:
            notOddArray.append(element)

    return notOddArray

print(returnNotOdds([]))