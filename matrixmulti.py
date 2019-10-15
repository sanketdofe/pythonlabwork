def printm(m):
    for i in range(len(m)):
        print(m[i])
        
n = int(input('Enter the dimension for the matrix:'))
print("\nMatrix 1")
m1=[[int(input("Enter the element at ("+str(j+1)+","+str(i+1)+"):")) for i in range(n)]for j in range(n)]
print("\nMatrix 2")
m2=[[int(input("Enter the element at ("+str(j+1)+","+str(i+1)+"):")) for i in range(n)]for j in range(n)]
#m1=[[1,1,1],[1,1,1],[1,1,1]]
#m2=[[1,2,3],[4,5,6],[7,8,9]]
print("\nMatrix 1")
printm(m1)
print("\nMatrix 2")
printm(m2)
m3=[[0 for i in range(n)]for j in range(n)]
#Tm2=zip(m2[0],m2[1],m2[2]))
#matrix3=[[pre+i*k for i,k in m1[j],Tm2[j]]for j in range(3)] 
for i in range(len(m1)):
    for j in range(len(m2[i])):
        for k in range(len(m2)):
            m3[i][j]+=m1[i][k]*m2[k][j]
print("\nMatrix 3")
printm(m3)            

