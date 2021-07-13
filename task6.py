'''
Task6. Reverse each word of a string passed as a script argument.
'''

import sys
import unittest

def main(argv):
    stringlist = argv[0].split(' ')
    reversedstring = " "
    reversedlist = [word[::-1] for word in stringlist]
    
    reversedstring = reversedstring.join(reversedlist)
    return reversedstring

if __name__ == "__main__":
   main(sys.argv[1:])

class Testtask1(unittest.TestCase):
    def test(self):
        self.assertEqual(main(['asdfghjkl']),'lkjhgfdsa')