'''
Task4. Check if a key exists in a dictionary or not
'''

import sys

def main(argv):
    squaredict = {}
    for i in range(1,26):
        squaredict[i] = i*i
    key = 9
    
    
    if squaredict.has_key(key):
        print("Key exists")
    else:
        print("Key does not exist")

if __name__ == "__main__": 
    
    main(sys.argv[1:])