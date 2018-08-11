import random
import json
def makeTeams(teams, players):
	try:
		x=players/teams
		if teams>players:
			raise ValueError("Enter the numbers again")
		if (players%teams )!=0:
			raise ValueError("Enter the value again with teams="+str(teams)\
				+ "and players="+str(players-1))

	except TypeError:
		raise TypeError("Format is incorrect")
	except ZeroDivisionError:
		raise ZeroDivisionError("Number of teams cannot be zero")
	# except ValueError:
	# 	print("Remove "+ str(players%teams) + " players first.")


#makeTeams(100,10)
def createDatabase():
	teams={}
	jersey=range(1,1001)
	random.shuffle(jersey)

	k=0
	for i in ['A','B','C','D','E','F','G','H','J']:
		dic={}
		y=range(1,11)
		random.shuffle(y)
		for j in range(10):
			dic[jersey[10*k+j]]=y[j]
		teams[i]=dic
		k=k+1
	t=json.dumps(teams)
	return t

# dic=[{"a":"b"},{"c":"d"}]
# print(dic[0])
TeamNames={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9}
#print(TeamNames["A"])
p=createDatabase()
p=json.loads(p)
#print(q["A"])
with open("transfer.txt")as f:
	lines=f.readlines()
	for line in lines:
		#print(line)
		l=line.split()
		#print(p["A"])
		b=0
		if l[0] not in ['A','B','C','D','E','F','G','H','J']:
			print("Try another transfer(Wrong team name)")
			continue
		for a in ['A','B','C','D','E','F','G','H','J']:
			if l[1] in  p[a].keys():
				b=a
		if b==0:
			print("Try another transfer(Wrong player name)")
			continue
		if p[b][l[1]] >=7 :
			print("Try another transfer(Very high loyalty)")
			continue
		else:
			print("Transfer Complete")
		


