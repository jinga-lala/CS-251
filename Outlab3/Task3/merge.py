import csv

if __name__=="__main__":
	fday=open("info_day.csv","r")
	fnight=open("info_night.csv","r")
	combined=open("info_combined.csv","w", newline='')
	rday=list(csv.reader(fday))
	rnight=list(csv.reader(fnight))
	writer=csv.writer(combined)
	writer.writerow(['Day',"Temperature(Day)","Temperature(Night)","Humidity(Night)","Humidity(Night)","Light(Day)","Light(Night)","CO2(Day)","CO2(Night)"])
	for row in range(1,len(rday)):
		day=rday[row][1:]
		night=rnight[row][1:]
		# print(day)
		# print(night)
		buff=['']*(2*len(day)+1)
		buff[1::2]=day
		buff[2::2]=night
		buff[0]=rday[row][0]
		print(buff)
		writer.writerow(buff)		


