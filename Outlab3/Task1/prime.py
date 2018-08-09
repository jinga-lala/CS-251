import argparse
import sys
def isPrime(n):
	for i in range(2,(int(n**0.5)+1)):
		if(n%i==0):
			return "No "
	return "Yes "

def die_with_usage():
	print(" Error : At least one of the following arguments are required: --check_prime, --range ")
	exit()
if __name__=="__main__":
	ap=argparse.ArgumentParser(description="Checks for prime, or prints all primes in a range")
	ap.add_argument("--check_prime",type=int)
	ap.add_argument("--range",nargs='+',type=int)
	if(len(sys.argv)<1):
		die_with_usage()
	args=ap.parse_args();
	prints=""
	if(args.check_prime):
		number=args.check_prime
		if(number in range(1,1001)):
			prints+=(isPrime(number))
		else:
			print(" Error : Please enter a value between 1 and 1000 only ")
			exit()	
	if(args.range):
		a=args.range[0]
		b=args.range[1]
		if(b in range(1,1001)):
			for i in range(a,b+1):
				if(isPrime(i)=="Yes "):
					s=str(i)+" "
					prints+=(s)
		else:
			print(" Error : Please enter a value between 1 and 1000 only ")
			exit()
	print(prints)			

