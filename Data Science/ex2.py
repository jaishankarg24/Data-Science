#program to store dictionary object within numpy and pandas(DataSeries)

import numpy as n 
import pandas as p 

my_dict={1:'a',2:'b',3:'c'}

arr=n.array(my_dict)
print(arr)
print(type(arr))

ds=p.Series(my_dict)
print(ds)
print(type(ds))

# o/p:
# -----
# {1: 'a', 2: 'b', 3: 'c'}
# <class 'numpy.ndarray'>

# 1    a
# 2    b
# 3    c
# dtype: object
# <class 'pandas.core.series.Series'>