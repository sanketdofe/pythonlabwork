list1=[]
def sum(list1 ,length):
	if length==0:
		return 0
	else:
		return list1[length -1] + sum(list1, length -1)

def add_el():
	for i in range(10):
		list1.append(int(input()))

add_el()
print("The sum is " + str(sum(list1, 10)))
