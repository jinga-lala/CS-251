import sqlite3
import sys

if __name__=="__main__":
	arg=sys.argv[1]
	ipl=sqlite3.connect("ipl.db")
	cur=ipl.cursor()
	args=arg.splitlines()
	values=[]
	for a in args[1:]:
		try:
			values.append(int(a))
		except:
			values.append(a)
	
	table_dict={'1':'team','2':'player','3':'match','4':'player_match','5':'ball_by_ball'}
	# print(values)
	s=',?'*len(values)
	s='('+s[1:]+')'
	# print(s)
	command='insert into '+table_dict[args[0]]+' values'+s
	cur.execute(command,values)
	ipl.commit()
	ipl.close()	
