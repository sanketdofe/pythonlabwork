list1=[]
n = int(input("Enter the no:"))
for i in range(1,n):
    if n%i==0:
        list1.append(i)
    
print("The Factors are "+str(list1))
