import random
import pickle
def fill_choice():
	l=[]
	alpha="QWERTYUIOPASDFGHJKLZXCVBNM"
	while(len(l)<100):
		j=random.randint(1,5000)
		while j in [x[0] for x in l]:
			j=random.randint(1,5000)
		name=alpha[random.randint(0,25)]+alpha[random.randint(0,25)]+alpha[random.randint(0,25)]+"\n"
		l.append([j,name])
	pickle.dump(l,open("new_int.p","wb"))




