#addition of Numpy array

import numpy as n 

arr=n.array([1,2,3,4,5])
print(arr)  #[1 2 3 4 5]

#syntax
#-------
#append(arr, values)

res=n.append(arr,7)
print(res)  #[1 2 3 4 5 7]

# res=n.extend(arr,[7,8,9])
# print(res) AttributeError: module 'numpy' has no attribute 'extend'

res=n.append(arr,[7,8,9])
print(res) #[1 2 3 4 5 7 8 9]



#syntax
#-------
# insert(arr, obj, values)

res=n.insert(arr, 2, 99)
print(res)  #[ 1  2 99  3  4  5]




