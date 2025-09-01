#1. create 2-D array and extract odd elements
import numpy as np
arr= np.array([[1,2,3],[4,5,6]])
print(arr[arr%2==1])

#2.create 2D-array extract 1strow and 2nd column using slicing
arr= np.array([[1,2,3],[4,5,6]])
print(arr[0,0:3])
print(arr[0:2,1])
