class adds:
	def __init__(self,v1):
		self.a=v1
		
	def addd(self,v1):
		self.a=self.a+[v1]
	
	def reports(self):
		print self.a
		
list1=["8086","80186","80286","80386","80486","arm6","arm7"]
aa=[]
a=adds(aa)
for n in list1:
	a.addd(n)

a.reports()
