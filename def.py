import random
def number():
	list1=range(0,10)
	a=""
	for n in list1:
		a=a+chr(random.randrange(0,9)+48)
	print a

random.SystemRandom(random.random())
list1=range(0,50)
for nn in list1:
		number()
