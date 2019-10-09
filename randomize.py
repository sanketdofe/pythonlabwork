import random
list1 = []
def add_el():
	for i in range(10):
		list1.append(int(input()))
def swap(a,b):
	temp=a
	a=b
	b=temp

def random():
	for i in range(10):
		swap(list1[i], random.random)	 
