
def fact(r):
	if r ==0:
		return 1
	else:
		return (r * fact(r-1))

def sum(n,x):
	if n == 0:
		return x
	else:
		return ((((-1)**n)*(x**(2*n + 1))/fact(2*n+1)) + sum(n-1,x))
print(sum(10,1.0))
