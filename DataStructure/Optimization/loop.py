"""
Optimizing Loops
Case1. for loop
Case2. map loop
Case3. comprehension
Case4. itertools
ref: https://aglowiditsolutions.com/blog/python-optimization/
"""
import timeit
import itertools

Zipcodes = ['121212', '232323', '343434']
newZipcodes = ['  131313  ', ' 242424   ', ' 212121 ', '     353535', '434343   ', ' 565656 ', ' 838497 ', '  281048    ', '092093      ']


def updateZips(newZipcodes, Zipcodes):
    for zipcode in newZipcodes:
        Zipcodes.append(zipcode.strip())


def updateZipsWithMap(newZipcodes, Zipcodes):
    Zipcodes += map(str.strip, newZipcodes)


def updateZipsWithListCom(newZipcodes, Zipcodes):
    Zipcodes += [iter.strip() for iter in newZipcodes]


def updateZipsWithGenExp(newZipcodes, Zipcodes):
    return itertools.chain(Zipcodes, (iter.strip() for iter in newZipcodes))


print('updateZips() Time            : ' + str(timeit.timeit('updateZips(newZipcodes, Zipcodes)', setup='from __main__ import updateZips, newZipcodes, Zipcodes')))

Zipcodes = ['121212', '232323', '343434']
print('updateZipsWithMap() Time     : ' + str(timeit.timeit('updateZipsWithMap(newZipcodes, Zipcodes)', setup='from __main__ import updateZipsWithMap, newZipcodes, Zipcodes')))

Zipcodes = ['121212', '232323', '343434']
print('updateZipsWithListCom() Time : ' + str(timeit.timeit('updateZipsWithListCom(newZipcodes, Zipcodes)', setup='from __main__ import updateZipsWithListCom, newZipcodes, Zipcodes')))

Zipcodes = ['121212', '232323', '343434']
print('updateZipsWithGenExp() Time  : ' + str(timeit.timeit('updateZipsWithGenExp(newZipcodes, Zipcodes)', setup='from __main__ import updateZipsWithGenExp, newZipcodes, Zipcodes')))
print(list(updateZipsWithGenExp(newZipcodes, Zipcodes)))
