class Test:
	def  __init__(self,sno,name):
		self.sno=sno
		self.name=name 

	def showTest(self):
		print  self.sno ,"  ",self.name

temp=Test(12,'Rajan')
temp.showTest()
