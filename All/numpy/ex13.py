# Comparision of numpy arrays

import numpy as n 
arr1=n.array([10,20,30,40,50])
arr2=n.array([60,70,30,40,70])

print(arr1==arr2)  # [False False  True  True False]
print(arr1>arr2)  # [False False False False False]
print(arr1<arr2)  # [ True  True False False  True]
print(arr1>=arr2) # [False False  True  True False]
print(arr1<=arr2) # [ True  True  True  True  True]
print(arr1!=arr2) # [ True  True False False  True]
print(arr1 and arr2)  #ValueError

# NOTE:
# -----
# -->Comparision does not work for logical operators

