import csv
f1 = open ("my.cvs","r+")
ff = csv.reader(f1)
a="------------------------"
for n in ff:
	print a
	a=""
	b=""
	for m in n:
		a=a+b"|\t" + m+"\t"
		b="\t"
	

f1.close()
