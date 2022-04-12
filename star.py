import random
def printxy(x,y,s):
	print "\033["+str(y)+";"+str(x)+"f"+s

random.SystemRandom(random.random())	
list1=range(380)
for n in list1:
	printxy(random.randrange(1,75),random.randrange(1,18),"*")
	
