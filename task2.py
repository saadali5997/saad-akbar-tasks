'''
Task2. Add the common key values of 2 dictionaries.
'''

import unittest

def main(range1low,range1high,range2low,range2high):
    squaredict = {}
    quaddict = {}
    for i in range (range1low,range1high+1):
        squaredict[i] = i*i

    for i in range (range2low,range2high+1):
        quaddict[i] = i*i*i*i

    print("Square Dict. The dictionary where value is key squared.{}".format(squaredict))
    print("Quad Dict. The dictionary where the value is key quadrupled (key^4).{}".format(quaddict))


    commondict = {}
    for i in range(range2low, range2high):
        try:
            if (squaredict[i] and quaddict[i]):
                commondict[i] = squaredict[i] + quaddict[i]
        except:
            continue
    print("Commondict. The dictionary of two added values.{}".format(commondict))
    return commondict
if  __name__ == "__main__":
    main(1,15,1,25)

class Testtask1(unittest.TestCase):
    def test(self):
        dict = {1: 2, 2: 20, 3: 90, 4: 272, 5: 650, 6: 1332, 7: 2450, 8: 4160, 9: 6642, 10: 10100, 11: 14762, 12: 20880, 13: 28730, 14: 38612, 15: 50850}
        self.assertEqual(main(1,15,1,25),dict)