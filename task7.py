squaredict = {}
for i in range (1,16):
    squaredict[i] = i*i

print("Square Dict. The dictionary where value is key squared")
print(squaredict)

#dict = {key:value for k, v in squaredict.items()}
inverseddict = {value:key for key,value in squaredict.items()}
print(inverseddict)