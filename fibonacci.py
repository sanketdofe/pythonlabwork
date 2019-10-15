n=int(input("Enter the length of sequence:"))
list1 = []
a = 0
list1.append(a)
b=1
list1.append(b)
for i in range(2,n):
    j=list1[i-1]+list1[i-2]
    list1.append(j)

print(list1)
