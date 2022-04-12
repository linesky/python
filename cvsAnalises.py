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
list1=range(1,50)
for v in list1:
	f1.seek(0)
	for n in ff:
		if (int)(n[1])==v:
			print n

f1.close()
