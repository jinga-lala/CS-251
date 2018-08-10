import json
import random
def makeTeams(teams,players):
	if(teams==0):
		raise ValueError("Error: Enter a non-zero number of teams")
	elif(players%teams!=0):
		error="Error: Remove "+str(players%teams)+" players"
		raise ValueError(error)
	else:
		pool_teams="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		roster={}
		jerseys=[]
		for i in range(teams):
			team=[]
			for j in range(int(players/teams)):
				player={}
				jersey=random.randint(1,1000)
				while jersey in jerseys:
					jersey=random.randint(1,1000)
				loyalty=random.random()*10
				player["Jeresey"]=jersey
				player["Loyalty"]=loyalty
				team.append(player)
			roster[pool_teams[i]]=team
		return roster
def get_min_loyalty(team,teams):
	roster=teams[team]
	m={}
	min_loyalty=10
	for p in roster:
		if(p["Loyalty"]<min_loyalty):
			m=p
			min_loyalty=p["Loyalty"]
	buff=m 
	team.delete[m]
	return buff


if __name__=="__main__":
	tr=open("transfers.txt","r")
	db=open("database.json","w")
	teams=makeTeams(10,100)
	json.dump(teams,db)
	transfers=tr.readlines()[1:]
	count=0
	for t in transfers:
		team=t.split()[0]
		jersey=int(t.split()[1])
		if(jersey not in (1,1001)):
			print("jersey does not exist")
			continue
		if (team not in list(teams.keys())):
			print("Team does not exist")
			continue
		f=0
		for p in teams:
			for k in teams[p]:
				# print(k)
				if(k["Jeresey"]==jersey):
					f=1
					if(k["Loyalty"]>7):
						print("Loyalty exceeded, try another player")
					else:
						buff=k
						teams[p].delete(k)
						teams[p].append(get_min_loyalty(team,teams))
						teams[team].append(buff)
						count+=1
						print("Player transferred")
		if(f==0):
			print("Jersey does not exist")
	print(count)


