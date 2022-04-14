group=[-2,-1,0,1,2]
pare=[]
notPare=[]
print "group:"
print group
for n in group:
	if (n/2)*2==n:
		pare=pare+[n]
	else:
		notPare=notPare+[n]
		
print "group of Pare numbers:"
print pare
print "group of notPare numbers:"
print notPare

