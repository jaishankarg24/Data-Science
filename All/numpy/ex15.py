#deletion of Numpy array

import numpy as n 

a=n.array([1,2,3,4,5])
print(a)  #[1 2 3 4 5]

# res=n.pop()   # AttributeError: module 'numpy' has no attribute 'pop'
# res=n.remove(3)  #AttributeError: module 'numpy' has no attribute 'remove'

# syntax:
# -------
# delete(arr, obj)

res=n.delete(a,4)
print(res)  #[1 2 3 4]

