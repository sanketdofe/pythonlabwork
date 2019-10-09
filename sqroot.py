
from __future__ import print_function
import sys
def check(n):
	i=0
	while i<100:
		if n==i*i:
			print(i, end=" ")
			break
		i+=1
	print("is the square root")

check(int(sys.argv[1]))
