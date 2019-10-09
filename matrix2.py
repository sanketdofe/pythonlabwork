n = int(input('Enter the dimension for the matrix:'))
matrix = [[(x+y)%2 for x in range(n)] for y in range(n)]
for b in range(n):
	print(matrix[b])
print('\n\n\n')
matrix = [[(x*y)%2 for x in range(n)] for y in range(n)]
for b in range(n):
	print(matrix[b])
