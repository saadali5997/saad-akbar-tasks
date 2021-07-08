import sys

def main(argv):
    stringlist = argv[0].split(' ')
    reversedstring = " "
    reversedlist = [word[::-1] for word in stringlist]
    
    reversedstring = reversedstring.join(reversedlist)
    print(reversedstring)

if __name__ == "__main__":
   main(sys.argv[1:])