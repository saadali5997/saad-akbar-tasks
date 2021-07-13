'''
Task3. Filter the even values out of a Dictionary.
'''

import unittest

# Old implementation of the Task.
def oldmain():
    squaredict = {}
    quaddict = {}
    for i in range (1,16):
        squaredict[i] = i*i

    for i in range (1,25):
        quaddict[i] = i*i*i*i

    print(f"Square Dict. The dictionary where value is key squared.{squaredict}")
    print(f"Quad Dict. The dictionary where the value is key quadrupled (key^4).{quaddict}")


    commondict = {}
    for i in range(1, 25):
        try:
            if (squaredict[i] and quaddict[i]):
                commondict[i] = squaredict[i] + quaddict[i]
        except:
            continue
    print(f"Commondict. The dictionary of two added values.{commondict}")
    removelist = []
    for key in commondict: 
        if(commondict[key] % 2 == 0):
            value = commondict[key]
        removelist.append((key,value))
        
    for tuple in removelist:
        commondict.pop(tuple[0],tuple[1])
    # Adding an odd value to the dictionary because all other values are even. Checking to see if this value will remain
    # after even values are deleted
    commondict[16]= 3

    print(f"Commondict after removing even values {commondict}")

def main(dict1,dict2):
    dict3 = {}
    for key in dict2:
        if key in dict1:
            dict3[key] = dict1[key] +dict2[key]
    return dict3


if __name__ == "__main__":
    dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
    dict2 = {1: 1, 2: 16, 3: 81, 4: 256, 5: 625, 6: 1296, 7: 2401, 8: 4096, 9: 6561, 10: 10000, 11: 14641, 12: 20736, 13: 28561,
            14: 38416, 15: 50625, 16: 65536, 17: 83521, 18: 104976, 19: 130321, 20: 160000, 21: 194481, 22: 234256, 23: 279841,
            24: 331776}
    dict3 = {1: 2, 2: 20, 3: 90, 4: 272, 5: 650, 6: 1332, 7: 2450, 8: 4160, 9: 6642, 10: 10100, 11: 14762, 12: 20880, 13: 28730, 14: 38612, 15: 50850}
    main(dict1,dict2)


class Testtask1(unittest.TestCase):
    def test(self):
        dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
        dict2 = {1: 1, 2: 16, 3: 81, 4: 256, 5: 625, 6: 1296, 7: 2401, 8: 4096, 9: 6561, 10: 10000, 11: 14641, 12: 20736, 13: 28561,
                14: 38416, 15: 50625, 16: 65536, 17: 83521, 18: 104976, 19: 130321, 20: 160000, 21: 194481, 22: 234256, 23: 279841,
                24: 331776}
        dict3 = {1: 2, 2: 20, 3: 90, 4: 272, 5: 650, 6: 1332, 7: 2450, 8: 4160, 9: 6642, 10: 10100, 11: 14762, 12: 20880, 13: 28730, 14: 38612, 15: 50850}
        self.assertEqual(main(dict1,dict2),dict3)