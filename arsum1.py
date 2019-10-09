list1 =[]
sum2=0
def sum_arr(n):
	global sum2
	if(n<10):
		n+=1
		sum2=sum2 + list1[n-1]
		sum_arr(n)
	return sum2		
def add_el():
	for i in range(10):
		list1.append(int(input()))
add_el()
print("The sum is " + str(sum_arr(0)))

