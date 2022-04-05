#!/bin/python
var1="\033c\033[47;30m \n"
print var1
list2=[]
for n in range(0,10):list2=list2+[n*5]
print list2
list1=[]
f1 = open("data.txt","w+")
for n in range(0,len(list2)):
	f1.write(str(list2[n]))
	f1.write("\n")
f1.close()

