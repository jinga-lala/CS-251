import pandas as pd 
import numpy as np 
import csv

def convert_to_fahrenheit(celsius):
	return (1.8*celsius + 32)

if __name__=="__main__":
	data=pd.read_csv("info_day.csv")
	x=data.iloc[:,:].values
	for i in range(len(x)):
		x[i][1]=convert_to_fahrenheit(x[i][1])
	file=open('transformed.csv','w',newline='')
	writer = csv.writer(file)
	writer.writerow(['Day',"Temperature","Humidity","Light","CO2"])
	for i in range(x.shape[0]):
		writer.writerow(x[i])
	file.close()

