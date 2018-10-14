import sqlite3
import csv

if __name__ == "__main__":
    ipl =sqlite3.connect("ipl.db")
    cur = ipl.cursor()
    cur.execute('''SELECT sum(runs_scored)from 'ball_by_ball' Join 'match' on 'match'.match_id='ball_by_ball'.match_id group by 'match'.venue_name ''')
    # dosri_ginti=ipl.cursor()
    # dosri_ginti.execute('''SELECT sum(extra_runs)from 'ball_by_ball' Join 'match' on 'match'.match_id='ball_by_ball'.match_id group by 'match'.venue_name ''')
    ginti = ipl.cursor()
    ginti.execute('''select  count(match_id), venue_name  from 'match' where venue_name!="NULL" group by venue_name ''')
    for a,b in zip(cur,ginti):
    	d= (a[0])/b[0]
    	#print(a[0],b[0],a[0]/b[0])
    	print(str(b[1])+","+str(d))
     	