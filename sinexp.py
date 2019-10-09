def fact(d):
	while (d!=1):
		d=d*fact(d-1)
		return d
	return d
def sin(x):
	return sum([(((-1)**n)*(x**(2*n + 1))/fact(2*n+1))for n in range(75)])

print(sin(3.14/6))

