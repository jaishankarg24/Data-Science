# Builtin functions within numpy module
import numpy as n 
arr1=n.zeros(3)
print(arr1)

arr2=n.zeros((3,4))
print(arr2)

arr3=n.ones(3)
print(arr3)

arr4=n.ones((3,4))
print(arr4)

arr5=n.eye(3)
print(arr5)

arr6=n.eye(4)
print(arr6)

arr7=n.full((3,3),8)
print(arr7)

arr8=n.full((5,3),7)
print(arr8)

o/p:
----
[0. 0. 0.]

[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]

[1. 1. 1.]

[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]

[[8 8 8]
 [8 8 8]
 [8 8 8]]
 
[[7 7 7]
 [7 7 7]
 [7 7 7]
 [7 7 7]
 [7 7 7]]