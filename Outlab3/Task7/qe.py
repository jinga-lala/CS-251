import numpy as np
from math import *	
def quaternion_to_euler(quaternion):
	norms=np.sum(np.abs(quaternion)**2,axis=1)**(1./2)
	quaternion=quaternion/norms	
	euler=np.zeros((quaternion.shape[0],3))
	euler[:,0]=(atan2(2*(quaternion[:,0]*quaternion[:,1]+quaternion[:,2]*quaternion[:,3]),1-2(quaternion[:,1]**2+quaternion[:,2]**2)))*(180.0/np.pi)
	euler[:,1]=(asin(2*(quaternion[:,0]*quaternion[:,2] - quaternion[:,3]*quaternion[:,1])))*(180.0/np.pi)
	euler[:,2]=(atan2(2*(quaternion[:,0]*quaternion[:,3]+quaternion[:,2]*quaternion[:,1]),1-2(quaternion[:,2]**2+quaternion[:,3]**2)))*(180.0/np.pi)
	# for i in range(len(quaternion)):
		# q=quaternion[i]/norms[i]
		# euler[i][0]=degrees(atan2(2*(q[0]*q[1]+q[2]*q[3]),1-2(q[1]**2+q[2]**2)))
		# euler[i][1]=degrees(asin(2*(q[0]*q[2] - q[3]*q[1])))
		# euler[i][2]=degrees(atan2(2*(q[0]*q[3]+q[2]*q[1]),1-2(q[2]**2+q[3]**2)))
	return euler

def euler_to_quaternion(euler):
	quaternion=np.zeros((euler.shape[0],4))
	euler=euler*(np.pi/180)
	quaternion[:,0]=np.cos(euler[:,0]*0.5)*np.cos(euler[:,1]*0.5)*np.cos(euler[:,2]*0.5) + np.sin(euler[:,0]*0.5)*np.sin(euler[:,1]*0.5)*np.sin(euler[:,2]*0.5)
	quaternion[:,1]=np.cos(euler[:,0]*0.5)*np.sin(euler[:,1]*0.5)*np.cos(euler[:,2]*0.5) - np.sin(euler[:,0]*0.5)*np.cos(euler[:,1]*0.5)*np.sin(euler[:,2]*0.5)
	quaternion[:,2]=np.cos(euler[:,0]*0.5)*np.cos(euler[:,1]*0.5)*np.sin(euler[:,2]*0.5) + np.sin(euler[:,0]*0.5)*np.sin(euler[:,1]*0.5)*np.cos(euler[:,2]*0.5)
	quaternion[:,3]=np.sin(euler[:,0]*0.5)*np.cos(euler[:,1]*0.5)*np.cos(euler[:,2]*0.5) - np.cos(euler[:,0]*0.5)*np.sin(euler[:,1]*0.5)*np.sin(euler[:,2]*0.5)
	norms=np.sum(np.abs(quaternion)**2,axis=1)**(1./2)
	quaternion=quaternion/norms	
	return quaternion	