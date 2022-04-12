import csv
f1 = open ("my.cvs","r+")
ff = csv.reader(f1)
a=""
nn=0
list1=range(1,51)
nn=0
for v in list1:
	f1.seek(0)
	if v>1:print str(v-1)+"\t"+str(nn)
	nn=0
	for n in ff:
		if (int)(n[1])==v:nn=nn+1
			

f1.close()
