'''
Task4. Check if a key exists in a dictionary or not
'''

import sys
import unittest

def main(argv):
    squaredict = {}

    for i in range(1,26):
        squaredict[i] = i*i
    try:
        key = int(argv)
    except:
        key = int(argv[0])
    print(key)
    
    if key in squaredict:
        return True
    else:
        return False
        
if __name__ == "__main__":     
    main(sys.argv[1:])

class Testtask1(unittest.TestCase):
    def test(self):
        self.assertEqual(main(4),True)