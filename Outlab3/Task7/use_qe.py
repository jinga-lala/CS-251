from qe import quaternion_to_euler as qte 
from qe import euler_to_quaternion as etq 
import sys
import numpy as np 

if __name__=="__main__":
	if(len(sys.argv)<3):
		print("Enter infile,outfile and choice")
		exit(1)
	infile_n=sys.argv[1]
	outfile_n=sys.argv[2]
	choice=sys.argv[3]
	infile=open(infile_n,"r")
	outfile=open(outfile_n,"w")
	i=np.loadtext(infile,delimiter=",")
	if(choice=='0'):
		if(i.shape[1]==4):
			euler=qte(i)
			np.writetext(outfile,delimiter=",")
		else:
			print("Wrong dimensions")
			exit(1)
	else:
		if(i.shape[1]==3):
			quaternion=etq(i)
			np.writetext(outfile,delimiter=",")
		else:
			print("Wrong dimensions")
			exit(1)
