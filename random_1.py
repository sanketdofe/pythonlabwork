import random
l=[]
m=[]
for i in range(10):
	l.append(random.uniform( 1, 100))

print(l)

for j in range(len(l)-1):
	l[j] = str(l[j])
	for k in range(len(l[j])-1):
		if(l[j][k]=='.'):
			if(l[j][k+1]=='7' or l[j][k+1]=='8' or l[j][k+1]=='9'):
				m.append(l[j])
				break
		else:
			continue	
print("\n\nrequired list:")
print(m)

L = filter(lambda x : True if str(x)[str(x).index('.')+1] in '789' else False, l)

print(L)
