#u={1,2,3,4,5,6,7,8,9}
m=int(input("Enter the no of vertices:"))
u=set([int(input("Enter the vertice "+ str(i+1) +":") for i in range(m))])
n=int(input("Enter the no of edges:"))
arr = [set([]) for i in range(30)]
#edges=set([(1,3),(2,4),(6,7),(2,5),(1,4),(2,3),(5,7),(2,6)])
k=0
cycle=0
edges=set([tuple((int(input("Enter vertices of edge "+ str(i+1) + ":")))for j in range(2)) for i in range(n)])
print(edges)
for i in list(edges):
	flag = 0
	count=0	
	for j in i:		
		if j in u:#check if it is in universal
			temp=u.remove(j)
			arr[k].add(temp)
		else:
			for l in arr:#check if it is in newly made sets
				
				if j in l:
					flag+=1
					#arr[k].add=l.remove(j)
					#arr[k].add(j+1)
					arr[k].union(l)
					for z in range(count,20):
						arr[z]=arr[z+1]
					l=0
				else:
					arr[k].add(j)
				count+=1	
	k+=1
	if flag==2:
		cycle+=1

print("Cycle:" + str(cycle))
