#Manipulation of Numpy array:

import numpy as n 

arr=n.arange(10)
print(arr)  #[0 1 2 3 4 5 6 7 8 9]

print(arr.shape)  #(10,)
print(arr.ndim)   #1

# syntax:
# -------
# resize(a, new_shape)

res=n.resize(arr,(3,2))
print(res)

res=n.resize(arr,(3,3))
print(res)
# ----------------------------------------
# syntax:
# -------
# reshape(a, new_shape)

# res=n.reshape(arr,(3,2))  -->ValueError: cannot reshape array of size 10 into shape (3,2)

res=n.reshape(arr,(2,5))
print(res) 

res=n.reshape(arr,(5,2))
print(res) 
# -----------------------------------------
res=n.reshape(arr,(2,5),'F')    #priority is given for column
print(res) 

res=n.reshape(arr,(5,2),'C')  #priority is given for row
print(res) 

o/p:
-----
[0 1 2 3 4 5 6 7 8 9]


(10,)


1


[[0 1]
 [2 3]
 [4 5]]


[[0 1 2]
 [3 4 5]
 [6 7 8]]


[[0 1 2 3 4]
 [5 6 7 8 9]]


[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]


[[0 2 4 6 8]
 [1 3 5 7 9]]


[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
 # ---------------------------------------------------------
 
# NOTE:
# -----
# ---->Bydefault the priority will be given for row while filling the data
# ---->Using resize() we can not provide the priority
# ---->Using reshape() we can provide the priority