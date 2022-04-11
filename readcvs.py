import csv
f1 = open ("my.cvs","r+")
ff = csv.reader(f1)
for n in ff:
	print n
	

f1.close()
