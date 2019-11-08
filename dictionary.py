from datetim import datetime as dt
contacts={}
def addcont():
	name = str(input("Enter the name:"))
	no = str(input("Enter the no:"))
	contacts[no] = name

def update():
	no = str(input("Enter the no to be updated:"))
	up_name = str(input("Enter the updated name:"))
	contacts[no] = up_name

def delete():
	no = str(input("Enter the no to be deleted:")
	del contacts[no]

def printall():
	if len(contacts)=0:
		print("The contact list is empty!!")
	else:
		print("Name\tMobile")
		for i in contacts:
			print({}+"/t"+{} ,contacts[i],i)

def search():
	req_no=input("Enter the no to be searched:")	
	for i in contacts:
		if i==req_no:
			print("The no is present.")
			print("Name associated with {}:" + contacts[i],i)			
			break
		
n=0
print("1.Add a contact\n2.Delete a contact\n3.Update a contact\n4.Search a particular contact\n5.Exit")
while n!=5 :
	n = int(input("Enter a choice:"))
	if n==1:
		addcont()
	elif n==2:
		delete()
	elif n==3:
		update()
	elif n==4:
		search()
	elif n==5:
		break

