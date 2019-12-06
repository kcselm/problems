"""
Consider an array of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array
(true means present).
"""

def count_sheeps(arrayOfSheeps):
    # counter = 0
    # for sheep in arrayOfSheeps:
    #     if sheep:
    #         counter += 1
    # return counter
    return arrayOfSheeps.count(True)


print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))