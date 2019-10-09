import sys
def check(n):
	i=0
	l=1
	temp=n
	while i<30:
		q=temp+l
		q=q/2.0
		if q*q>n:
			temp=q
		else :
			l=q
		i+=1
	print(q)

check(int(sys.argv[1]))
