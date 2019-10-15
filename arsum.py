import sys
list1 =[]
a=-1
def sum_arr():
	sum1=0
	for a in list1:
	    sum1+=a
	return sum1
def add_el(no):
    print("Enter the elements:")
    for i in range(no):
		list1.append(int(input()))

def result(sum1):
	print("The sum is " + str(sum1))

def display():
	print(list1)

n=0	
print("1.Push elements in list\n2.Add the elements of the list\n3.Display the list\n4.Display the sum\n5.Exit\n")
#check(int(sys.argv[1]))
while n!=5:
    n = int(input("Enter your choice:"))
    if n == 1:
        no=int(input(("Enter the no of elements:")))
        add_el(no)
    elif n==2:
        sum1 = sum_arr()
    elif n==3:
        display()
    elif n==4:
        result(sum_arr()) 
    elif n==5:
        break
