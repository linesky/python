group=[-2.2,-1,0,1.1,2]
integers=[]
notIntegers=[]
print "group:"
print group
for n in group:
	if int(n)==n:
		integers=integers+[n]
	else:
		notIntegers=notIntegers+[n]
		
print "group of integers numbers:"
print integers
print "group of notIntegers numbers:"
print notIntegers

