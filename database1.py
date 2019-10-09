import random
data1 = [[i+101] for i in range(100)]
def avgsal():
	avg=0
	for i in range(len(data1)):
		avg+=data1[i][4]
	avg=avg/len(data1)
	return avg

for i in range(len(data1)):
	name=str(chr(random.randint(65,90)))
	name=name+str(random.choice(['a','e','i','o','u']))
	for k in range(random.randint(2,5)):
		name=name+str(chr(random.randint(97,122)))
	data1[i].append(name)
	age=random.randint(18,60)
	data1[i].append(age)
	email=str(chr(random.randint(97,122)))
	for k in range(random.randint(2,5)):
		email+=str(chr(random.randint(97,122)))
	email+=random.choice(['@gmail.com','@yahoo.com','@facbok.com'])
	data1[i].append(email)
	salary=random.randint(30,150)
	salary=salary*10000
	data1[i].append(salary)
print("\nID\t\tName\t\tAge\t\tEmail\t\t\tSalary\n")
for i in range(len(data1)):
	print(*data1[i],sep='\t\t')	
##print(*data1,sep='\n')

print("Avg Salary:",avgsal())
