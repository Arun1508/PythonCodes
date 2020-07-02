#b = [[11, "arun"], [1,"Hetesh"],[1,"Sankar"]]
b = [["asa",2],["bsb",1], ["aaaa",1]]
b.append(["aaaaa",1])
for x in b:
    print (x)

b.sort(key= lambda x: x[1])
print ("sort")
print (b)
print ("Pop ")
b.pop()
print(b)