list1=[]
#list1.append(2)
def getprime(n):
    for i in range(2,n):
        count=0
        for j in list1:
            if i%j!=0:
                count+=1
        if count==len(list1):
            list1.append(i)    

n = int(input("Enter the no upto which prime no has to be printed:"))
getprime(n)
print("The prime nos. are " + str(list1))
