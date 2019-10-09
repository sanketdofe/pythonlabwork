import random
data1 = [[i+1] for i in range(10)]

for i in range(len(data1)):
		cost = random.randint(10000,100000)
		data1[i].append(cost)
		time = random.randint(1,10)
		data1[i].append(time)
		name = str(chr(random.randint(65,90)))
		for k in range(random.randint(2,5)):
			name=name+str(chr(random.randint(97,122)))
		data1[i].append(name)
		cpertime = cost/time;
		data1[i].append(cpertime)
		
print("\nID\tCost\tTime\tName\tCost/Time\n")		
for i in range(len(data1)):
	print(*data1[i], sep ="\t")

def gochi(given):
	

for i in range(len(data1)):
	for j in range(len(data1) - i-1):
		if(data1[j][4]>data1[j+1][4]):
			temp = ['id','cost','time','name','cpertime']
			for k in range(5):
				temp[k] = data1[j][k]
				data1[j][k] = data1[j+1][k]
				data1[j+1][k] = temp[k]


print("\n\n**SORTED LIST**\n")		
print("\nID\tCost\tTime\tName\tCost/time\n")		
for i in range(len(data1)):
	print(*data1[i], sep ="\t")
	

x = int(input("Enter the no of hours:"))
gochi(x)
