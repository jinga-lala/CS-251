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


if __name__=="__main__":
	tr=open("transfers.txt","r")
	db=open("database.json","w")
	teams=makeTeams(10,100)
	json.dump(teams,db)
	transfers=tr.readlines()
	for t in transfers:
		team=t.split('\t')[0]
		jersey=int(t.split('\t')[1])
		if(jersey not in (1,1001)):
			raise ValueError("jersey does not exist")
		if (team not in list(teams.keys())):
			raise ValueError("Team does not exist")
		f=0
		for p in teams:
			try:
				if(p["Jeresey"]==jersey):
					f=1
					print("Transfer completed")
					'''
					TODO
					Return minimum loyalty player from somewhere else
					HAndle other exceptions
					'''

