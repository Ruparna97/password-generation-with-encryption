import string
import random

def generate(k,check):
	lowercase=list(string.ascii_lowercase)
	uppercase=list(string.ascii_uppercase)
	numbers=['0','1','2','3','4','5','6','7','8','9']
	specialcharacters=['!','@','#','$','%','&','*','^']
	all_values=lowercase+uppercase+numbers+specialcharacters
	password=""
	x=0

	if(check[0]==True):
		password=password+numbers[random.randint(0,len(numbers))-1]
		x+=1
	if(check[1]==True):
		password=password+specialcharacters[random.randint(0,len(specialcharacters))-1]
		x+=1
	if(check[2]==True):
		password=password+uppercase[random.randint(0,len(uppercase))-1]
		x+=1
	if(check[3]==True):
		password=password+lowercase[random.randint(0,len(lowercase))-1]
		x+=1

	for i in range(k-x):
		password+=all_values[random.randint(0,len(all_values)-1)]

	password=list(password)
	random.shuffle(password)

	password_string=""
	for i in password:
		password_string+=i

	print(password_string)
	return(password_string)

