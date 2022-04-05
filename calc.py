#!/usr/bin/python
import py_compile
var1=""
for n in range(0,10000):
	var1 = raw_input('enter equation? ')
	print eval(var1)
