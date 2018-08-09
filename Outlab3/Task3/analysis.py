import pandas as pd  
import numpy as np 

if __name__=="__main__":
	data=pd.read_csv("info_day.csv")
	x=data.iloc[:,1:].values
	std=np.std(x,axis=0)
	mean=np.mean(x,axis=0)
	fields=["Temperature", "Humidity","Light","CO2" ]
	print("Field\t\tMean\t\tStd. Dev. ")
	for i in range(len(fields)):
		printer=fields[i]+"\t"+str(mean[i])+"\t"+str(std[i])
		print(printer)
		

