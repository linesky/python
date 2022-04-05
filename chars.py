#!/usr/bin/python
def printLeters(s,n):
	print s[n:n+1]
var1="\033c\033[47;30m \n"
print var1
var2="hello world..."
for n in range(0,8): printLeters(var2,n)
