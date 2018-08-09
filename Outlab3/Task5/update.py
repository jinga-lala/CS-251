import json
if __name__=="__main__":
	file=open("infinity_stones.json","r")
	main_dict=json.load(file)
	list_of_dicts=main_dict["Infinity Stones"]
	file=open("updated_stones.json","w")
	for dict in list_of_dicts:
		dict["Containment Unit"]="Infinity Gauntlet"
	json.dump(main_dict,file)	