import numpy as np

arr = np.array([1, 2, 'hello', True])

print(arr)
print(type(arr)) #<class 'numpy.ndarray'>



# tuple as a array
tupleArr = np.array((1,2,4,5))
print(tupleArr)

# 3-d array
arrMat = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arrMat.ndim)# tells the dimension of array






