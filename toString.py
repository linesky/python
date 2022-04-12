def toString(lists):
	a=""
	b=0
	for lis in lists:
		if b!=0:a=a+","
		a=a+lis
		b=b+1
	return a
		
list1=["hello","world","hi","there"]
print toString(list1)
