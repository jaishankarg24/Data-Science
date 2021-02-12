# Mathematical operations upon Numpy array
import numpy as n 
arr1=n.array([1,2,3,4,5])
arr2=n.array([6,7,8,9,10])

print(arr1)
print(arr2)

print(arr1+arr2)
res=n.add(arr1, arr2)
print(res)

print(arr1-arr2)
res=n.subtract(arr1, arr2)
print(res)

print(arr1*arr2)
res=n.multiply(arr1, arr2)
print(res)

print(arr1/arr2)
res=n.divide(arr1, arr2)
print(res)

res=n.sqrt(arr1)
print(res)

res=n.log(arr1)
print(res)

res=n.sin(arr1)
print(res)

res=n.cos(arr1)
print(res)

o/p:
----
[1 2 3 4 5]

[ 6  7  8  9 10]

[ 7  9 11 13 15]

[ 7  9 11 13 15]

[-5 -5 -5 -5 -5]

[-5 -5 -5 -5 -5]

[ 6 14 24 36 50]

[ 6 14 24 36 50]

[0.16666667 0.28571429 0.375      0.44444444 0.5       ]

[0.16666667 0.28571429 0.375      0.44444444 0.5       ]

[1.         1.41421356 1.73205081 2.         2.23606798]

[0.         0.69314718 1.09861229 1.38629436 1.60943791]

[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]

[ 0.54030231 -0.41614684 -0.9899925  -0.65364362  0.28366219]
