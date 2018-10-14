import sqlite3
import csv

if __name__ == "__main__":
    ipl =sqlite3.connect("ipl.db")
    cur = ipl.cursor()
    cur.execute('''SELECT Count(ball_id),striker, 'player'.player_name FROM 'BALL_BY_BALL' Join 'player' on 'player'.player_id='ball_by_ball'.striker group by striker   ORDER BY count(ball_id) DESC''')
    ginti = ipl.cursor()
    ginti.execute('''select count(match_id),'player_match'.player_id from player_match  group by 'player_match'.player_id''')
#   ginti.execute('''select count(match_id),'player_match'.player_id from player_match join 'player' on 'player'.player_id='player_match'.player_id group by 'player_match'.player_id
#''')
    d1=cur.fetchall()
    d2=ginti.fetchall()
    rank=0
    first=1
    prev=0
    matches=1
    list_avg=[]
    for a in d1:
    	for b in d2:
    		if b[1]==a[1]:
    			c=[a[0]/b[0],b[1],a[2]]
    			list_avg.append(c)
    			break
    list_avg.sort(key= lambda x: x[0])
    rank=0
    prev=list_avg[-1][0]
    for a in list_avg[::-1]:
    	if rank > 10:
    		break
    	if prev!=a[0]:
    		rank+=1
    		prev=a[0]
    	print(str(a[1])+","+str(a[2])+","+str(a[0]))

    	

    # for a in cur:
    # 	if first==1:
    # 		first=0
    # 		for c in ginti:
    # 			if c[1]==a[1]:
    # 				matches=c[0]
    # 				print("yash")
    # 				break
    # 		avg=a[0]/matches
    # 		prev=avg
    # 		rank+=1
    # 		print(str(a[1])+","+a[2]+","+str(matches))
    # 	else:
    # 		for c in ginti:
    # 			if c[1]==a[1]:
    # 				matches=c[0]
    # 				break
    # 		avg=a[0]/matches
    # 		rank+=1
    # 		if prev==avg:
    # 			rank-=1
    # 		else:
    # 			prev=avg
    # 		if rank <= 10:
    # 			print("rank ",rank)
    # 			print(str(a[1])+","+a[2]+","+str(matches))
    # 		else:
    # 			break
