import random
list1=range(0,10)
random.SystemRandom(random.random())
list2=[]
for n in list1:
	list2=list2+[random.randrange(1,50)]

list1=list2
print list1

