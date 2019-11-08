from functools import reduce
f = open("avocado.csv", "r")
list1 = []
for line in f.readlines():
	list1.append(line.split(","))
	
mean = 0
count = 0

print(list1[1])
print(list1[2])
for i in list1[1:]:
	if (i[-1]=="Albany\n"):
		mean=mean+float(i[2])
		count+=1
mean=mean/count
print("The mean is " + str(mean))


mean1=reduce(lambda x,y: float(list1[list1.index(x)][2])+float(list1[list1.index(y)][2]),list1[1:])
mean1/=count
print(mean1)
