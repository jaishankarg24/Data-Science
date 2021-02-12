import pandas as p 
lst=[10,20,30,40,50]
print(lst)        #[10, 20, 30, 40, 50]
print(type(lst))  #<class 'list'>

ds=p.Series(lst)
print(ds)
print(type(ds))

# o/p:
# ----
# [10, 20, 30, 40, 50]
# <class 'list'>

# 0    10
# 1    20
# 2    30
# 3    40
# 4    50

# dtype: int64
# <class 'pandas.core.series.Series'>