snakes=[]
class snake:
	def __init__(self,gName,gLength,gVenom):
		self.name=gName
		self.length=int(gLength)
		self.venom=int(gVenom)
		snakes.append(self)
def findByVenom(venom):
	for snake in snakes:
		if(snake.venom==venom):
			print(snake.name)

def findByLength(length):
	for snake in snakes:
		if(snake.length==length):
			print(snake.name)

if __name__=="__main__":
	f=open('snakes.txt')
	content=f.readlines()
	# print(content)	
	number_of_snakes=int(content[0])
	for i in range(1,number_of_snakes+1):
		[name,length,venom]=content[i].split()
		snake(name,length,venom)
	number_of_queries=int(content[number_of_snakes+1])
	# print([x.venom for x in snakes])
	for i in range(number_of_queries+4,len(content)):
		command=content[i].split()[0]
		if(command=='V'):
			findByVenom(int(content[i].split()[1]))
		else:

			findByLength(int(content[i].split()[1]))

