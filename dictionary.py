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
print("1.Add contact\n2.Delete contact\n3."
