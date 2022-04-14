group=[-2,-1,0,1,2]
negative=[]
positive=[]
print "group:"
print group
for n in group:
	if n < 0:
		negative=negative+[n]
	else:
		positive=positive+[n]
		
print "group of negative numbers:"
print negative
print "group of positive numbers:"
print positive

