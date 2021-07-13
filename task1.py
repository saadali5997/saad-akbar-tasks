'''
Task1. Create a dictionary where value is key squared in the range(1,15) inclusive
'''

import unittest

def main():
    squaredict = {}
    for i in range (1,16):
        squaredict[i] = i*i

    print(f"Square Dict. The dictionary where value is key squared.{squaredict}")
    return squaredict
if __name__ == '__main__':
    main()


class Testtask1(unittest.TestCase):
    def test(self):
        dict = {1: 1 ,2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
        self.assertEqual(main(),dict)