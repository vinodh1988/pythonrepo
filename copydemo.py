import copy

li1=[1,2,3]
li2=[1,2,3]

print id(li1)
print id(li2)


x=1
y=1

print id(x)
print id(y)

li3=copy.copy(li1);

print id(li1) == id(li3)
print id(li1[0]) == id(li3[0])

li4=copy.deepcopy(li1)

print id(li1) == id(li4)
print id(li1[0]) == id(li4[0])
