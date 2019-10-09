import sys
def check(n):
	i=0
	t=0
	while i<100:
		t=i*i
		if n==t:
			print("True")
			break
		i+=1
	else :
		print("False")

check(int(sys.argv[1]))

