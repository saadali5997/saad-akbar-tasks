'''
Task7. Implement a script where a dictionary is given as an argument and the script inverses the key value pairs.
'''

import unittest

def main(dict1):  
    inverseddict = {value:key for key,value in dict1.items()}
    print(inverseddict)
    return inverseddict

if __name__ == "__main__":
    dict = {1: 1 ,2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
    main(dict)
    resultdict = {1: 1, 4: 2, 9: 3, 16: 4, 25: 5, 36: 6, 49: 7, 64: 8, 81: 9, 100: 10, 121: 11, 144: 12, 169: 13, 196: 14, 225: 15}

class Testtask1(unittest.TestCase):    
    def test(self):
        testdict = {1: 1 ,2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
        resultdict = {1: 1, 4: 2, 9: 3, 16: 4, 25: 5, 36: 6, 49: 7, 64: 8, 81: 9, 100: 10, 121: 11, 144: 12, 169: 13, 196: 14, 225: 15}
        self.assertEqual(main(testdict),resultdict)