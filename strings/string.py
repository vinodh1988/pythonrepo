print """Hello World!!!! 'this is wonderful"""
print "Hello World!!! ' this is also working"
print 'Hello World this is also Working'

#not much difference between ' and "


print  """ this is the first time I am working with python
	I feel I may fell in love with this language
	but who knows ............!!!!"""

""" there is not actually multi line comment in python
but if you want to have it 
you can have it this way """

temp=raw_input("enter your name\n")

print 'the value you entered is', temp

#print string by using for loop

for x in temp :
	print x


#print string by using for loop

p=0

while p < len(temp) :
	print temp[p]
	p+=1
