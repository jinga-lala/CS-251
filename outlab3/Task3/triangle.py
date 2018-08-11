EPSILON=0.000001
def dist(x1,y1,x2,y2):
	return ((x2-x1)**2+(y2-y1)**2)**0.5
def area(x1,y1,x2,y2,x3,y3):
	a=dist(x1,y1,x2,y2)
	b=dist(x2,y2,x3,y3)
	c=dist(x3,y3,x1,y1)
	# print(a,b,c)
	s=(a+b+c)/2
	A=(s*(s-a)*(s-b)*(s-c))**0.5
	return A
def insideOut(x1,y1,x2,y2,x3,y3,x,y):
	if area(x1,y1,x2,y2,x,y)+area(x,y,x2,y2,x3,y3)+area(x1,y1,x,y,x3,y3)-area(x1,y2,x2,y2,x3,y3)<EPSILON:
		print("INSIDE")
	else:
		print("OUTSIDE")

if __name__=="__main__":
	buff=input("Enter first point")
	[x1,y1]=buff.split()
	buff=input("Enter second point")
	[x2,y2]=buff.split()
	buff=input("Enter third point")
	[x3,y3]=buff.split()
	buff=input("Enter key point")
	[x,y]=buff.split()
	insideOut(int(x1),int(y1),int(x2),int(y2),int(x3),int(y3),int(x),int(y))		
