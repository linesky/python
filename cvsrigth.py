import csv
def rigths(values,s):
	a=s
	while True:
		a=" "+a
		if len(a)>=values:break
	return a
	
f1 = open ("my.cvs","r+")
ff = csv.reader(f1)
a="------------------------"
for n in ff:
	print a
	a=""
	b=""
	for m in n:
		a=a+"|"+rigths(5,m)

f1.close()
