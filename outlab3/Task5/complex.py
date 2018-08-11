class Complex:
	def __init__(self,x,y):
		self.real=float(x)
		self.imag=float(y)
	def __str__(self):
		if(self.imag>0):
			number=str(self.real)+"+"+str(self.imag)+"i"
		else:
			number=str(self.real)+str(self.imag)+"i"
		return(number)
	def __add__(self,number2):
		ret=Complex(0,0)
		ret.real=self.real+number2.real
		ret.imag=self.imag+number2.imag
		print(ret)
		return(ret)
	def __sub__(self,number2):
		ret=Complex(0,0)
		ret.real=self.real-number2.real
		ret.imag=self.imag-number2.imag
		print(ret)		
		return(ret)
	def __mul__(self,number2):
		ret=Complex(0,0)
		ret.real=self.real*number2.real - self.imag*number2.imag
		ret.imag=self.real*number2.imag + self.imag*number2.real
		print(ret)
		return ret
	def __truediv__(self,number2):
		ret=Complex(0,0)
		ret.real=(self.real*number2.real + self.imag*number2.imag)/(number2.imag**2+number2.real**2)
		ret.imag=(-self.real*number2.imag + self.imag*number2.real)/(number2.imag**2+number2.real**2)
		print(ret)
		return ret
if __name__=="__main__":
	f=open('numbers.txt')
	content=f.readlines()
	num1=Complex(content[0].split()[0],content[0].split()[1])
	num2=Complex(content[1].split()[0],content[1].split()[1])
	print(num1)
	print(num2)
	_=num1+num2
	_=num1-num2
	_=num1*num2
	_=num1/num2

		
		

