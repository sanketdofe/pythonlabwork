upper1= [[1, 1 ,1 ], [0 ,1 ,1 ], [0 ,0 ,1 ]]
lower1= [[1 ,0 ,0 ], [1 ,1 ,0 ], [1 ,1 ,1 ]]
tr1 = lower2 = upper2 = [[0 for i in range(3)] for j in range(3)]
    
for i in range(0, 3): 
      
	for j in range(0, 3): 
        
		if i>j: 
              
        	        upper2[i][j] = 0
            
		else: 

	                upper2[i][j] = 1

print("UPPER TRIANGULAR MATRIX:")
for i in range(3):
	print(upper2[i])
 


for i in range(0, 3): 
      
	for j in range(0, 3): 
        
		if i<j: 
              
        	        upper2[i][j] = 0
            
		else: 

	                upper2[i][j] = 1

print("\nLOWER TRIANGULAR MATRIX:")		 
for i in range(3):
	print(upper2[i])

print('\n')
#TRANSPOSE
tr = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
	print(tr[i])
for i in range(0, 3): 
      
	for j in range(0, 3):  
              
			tr1[i][j] = tr[j][i]
			
print("\nTRANSPOSE:")
for i in range(3):
	print(tr1[i])

