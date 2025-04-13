import array as a

#create an array 
b = a.array("i" , [1,2,3,4,5])
print(b)

# number of repetation 
c = a.array("i", [1,2,3,1,2,3,4,2])
print(c.count(3))

# reverse the array
d = a.array("i" , [1,2,3,4]) 
print(d[::-1])