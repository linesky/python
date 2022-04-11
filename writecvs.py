import random
import csv
f1 = open ("my.cvs","w+")
ff = csv.writer(f1)
list1=range(0,50)
random.SystemRandom(random.random())
for n in list1:
	ff.writerow([n]+[random.randrange(1,50)])

f1.close()
