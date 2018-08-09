import json
import csv
if __name__=="__main__":
	file=open("infinity_stones.json","r")
	main_dict=json.load(file)
	list_of_dicts=main_dict["Infinity Stones"]
	titles=list(list_of_dicts[0].keys())
	f=open("infinity_stones.csv","w", newline='')
	writer=csv.writer(f)
	writer.writerow(titles)
	for dict in list_of_dicts:
		row=[]
		for j in titles:
			row.append(dict[j])
		writer.writerow(row)
