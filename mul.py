#!/usr/bin/python
def formatedPrint(values,n):
	v=values*n
	var1=""
	var1=var1+str(values) 
	var1=var1+"\t X\t"
	var1=var1+str(n)
	var1=var1+"\t =\t"
	var1=var1+str(v)
	print var1
var1="\033c\033[47;30m \n"
print var1
var2="hello world..."
values=8
for n in range(0,10):formatedPrint(values,n)
