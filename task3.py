squaredict = {}
quaddict = {}
for i in range (1,16):
    squaredict[i] = i*i

for i in range (1,25):
    quaddict[i] = i*i*i*i

print("Square Dict. The dictionary where value is key squared")
print(squaredict)
print("Quad Dict. The dictionary where the value is key quadrupled (key^4)")
print(quaddict)

commondict = {}
for i in range(1, 25):
    try:
        if (squaredict[i] and quaddict[i]):
            commondict[i] = squaredict[i] + quaddict[i]
    except:
        continue
print("Commondict. The dictionary of two added values")
print(commondict)
removelist = []
for key in commondict: 
    if(commondict[key] % 2 == 0):
        value = commondict[key]
    removelist.append((key,value))
    
for tuple in removelist:
    commondict.pop(tuple[0],tuple[1])
commondict[16]= 3

print("Commondict after removing even values")
print(commondict)

