with open('students.txt') as f:
	lines=f.readlines()
	number=int(lines[0].split()[0])
	stu=[]
	for i in range(1,len(lines)):
		[x,y]=lines[i].split()
		dict={}
		dict[int(x)]=int(y)
		stu.append(dict)

def find_loc(x1,y1,x2,y2):
	if(x1<=x2 and y1<=y2):
		print(x2-x1+y2-y1)
	else:
		print(-1)
def find_total(x1,y1,x2,y2):
	if(x1!=x2):
		slope=float((y2-y1)/(x2-x1))
		c=y1-slope*x1
		for x in range(x1+1,x2):
			y=(slope*x+c)
			if(int(y)==y):
				dict={x:int(y)}
				try:
					i=stu.index(dict)
					print(x,y)
				except ValueError:
					continue
	else:
		for y in range(y1+1,y2):
			dict={x1:y}
			try:
				i=stu.index(dict)
				print(x1,y)
			except ValueError:
				continue
# buff=input("Enter x1 y1 x2 y2 space seperated: \n")
# [x1,y1,x2,y2]=[int(x) for x in buff.split()]
# # print(stu)
# find_total(x1,y1,x2,y2)
