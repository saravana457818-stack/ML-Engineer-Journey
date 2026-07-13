import numpy as np
arr=[1,2,3,4,5,6,7,8,9,10,11,12]
print(arr)
matrix = np.array(arr).reshape(3, 4)
print(matrix)   
print(matrix[1])  
print(matrix[:,2])
print(matrix*5)
print(matrix+10)
print(matrix.shape)
print(matrix.ndim)
