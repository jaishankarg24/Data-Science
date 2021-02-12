# Creation 3 d array

import numpy as n 
arr=n.array([[[10,20,30],[40,50,60],[70,80,90]],[[11,22,33],[44,55,66],[77,88,99]]])
print(arr)
print(type(arr))
print(arr.ndim)
print(arr.shape)
print(arr.dtype)

# o/p:
# ----
# [[[10 20 30]
#   [40 50 60]
#   [70 80 90]]

#  [[11 22 33]
#   [44 55 66]
#   [77 88 99]]]
# <class 'numpy.ndarray'>
# 3
# (2, 3, 3)
# int32