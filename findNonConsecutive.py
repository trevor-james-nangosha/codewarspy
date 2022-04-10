"""
    your task is to find the first element of an array 
    that is not consecutive
    for example the [1,2,3,5,6,7] should return 5

    how do we achieve chaining the commands in Python????????
    for now i will just give the expect function two parameters
"""
from Test import Test
test = Test()

"""
    this thing has a fault.come back later.
"""

def returnNonConsecutiveNumber(array):
    if array == []:
        return None
    if len(array) == 1 or len(array) == 2:
        return None

    if (array[1] - array[0]) == (array[2] - array[1]):
        diff = (array[1] - array[0])
    elif not ((array[1] - array[0]) == (array[2] - array[1])):
        return array[2]
    
    for i in range(2,len(array)):
        if(array[i] - array[i-1]) == diff:
            return None
        elif not ((array[i] - array[i-1]) == diff):
            return array[i]

test.expect(returnNonConsecutiveNumber([1,2,4]), 4)
test.expect(returnNonConsecutiveNumber([]), None)
test.expect(returnNonConsecutiveNumber([1,2,3,4,5,6]), None)
test.expect(returnNonConsecutiveNumber([1,2,4,5,6]), 4)
test.expect(returnNonConsecutiveNumber([2,3,4,5,6,7,8,10]), 10) #returns None
test.expect(returnNonConsecutiveNumber([1]), None)
test.expect(returnNonConsecutiveNumber([1,2]), None)

