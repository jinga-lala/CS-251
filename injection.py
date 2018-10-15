import sqlite3
import sys

if __name__=="__main__":
	arg=sys.argv[1]
	ipl=sqlite3.connect("ipl.db")
	cur=ipl.cursor()
	args=arg.splitlines()
	if(args[1]=='0'):
	# for a in args[1:]:
	# 	try:
	# 		values.append(int(a))
	# 	except:
			# values.append(a)
		table_dict={'1':'team','2':'player','3':'match'}
		column_dict={'1':'team_name = "','2':'player_name = "','3':'match_id = '}
		end_dict={'1':'"','2':'"','3':''}
		s=args[2]
		command='delete from '+table_dict[args[0]]+' where '+column_dict[args[0]]+s+end_dict[args[0]]
		print(command)
		cur.execute(command)
		ipl.commit()
		ipl.close()		
	# print(values)
	# s=',?'*len(values)
	# s='('+s[1:]+')'
	# # print(s)
	# command='insert into '+table_dict[args[0]]+' values'+s
