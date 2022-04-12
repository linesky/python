def printxy(x,y,s):
	print "\033["+str(y)+";"+str(x)+"f"+s
	
list1=range(18)
for n in list1:
	printxy(n,n,"hello world...")
	
