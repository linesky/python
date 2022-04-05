#!/bin/python
var1="\033c\033[47;30m \n"
print var1
list2=[]
for n in range(0,10):list2=list2+[n*5]
print list2
list1=[]
for n in range(0,len(list2)):
	if list2[n]==(list2[n]/10)*10:
			list1=list1+[list2[n]]
print list1
