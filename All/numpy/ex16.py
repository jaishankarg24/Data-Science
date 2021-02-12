#creating the copy of Numpy array
   #using reference variable
   #using copy()
   
import numpy as n 

arr1=n.array([10,20,30])
print(arr1)      #[10 20 30]
print(id(arr1))  #1000
# -------------------------------------
arr2=arr1
print(arr2)     #[10 20 30]
print(id(arr2)) #1000
# --------------------------------------
print(n.copy(arr1)) #[10 20 30]
# --------------------------------------
arr2=arr1.copy()
print(arr2)   #[10 20 30]
# ---------------------------------------