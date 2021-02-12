#mathematical operations and Relational operations upon Dataseries 

import pandas as p 

lst1=[10,20,30,40,50]
lst2=[30,40,30,20,50]

ds1=p.Series(lst1)
ds2=p.Series(lst2)
print(ds1)
print(ds2)

print(ds1+ds2)
print(ds1-ds2)
print(ds1*ds2)
print(ds1/ds2)

print(ds1<ds2)
print(ds1>ds2)
print(ds1>=ds2)
print(ds1<=ds2)
print(ds1==ds2)
print(ds1!=ds2)

# o/p:
# ----
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# 0    30
# 1    40
# 2    30
# 3    20
# 4    50
# dtype: int64

# 0     40
# 1     60
# 2     60
# 3     60
# 4    100
# dtype: int64

# 0   -20
# 1   -20
# 2     0
# 3    20
# 4     0
# dtype: int64

# 0     300
# 1     800
# 2     900
# 3     800
# 4    2500
# dtype: int64

# 0    0.333333
# 1    0.500000
# 2    1.000000
# 3    2.000000
# 4    1.000000
# dtype: float64

# 0     True
# 1     True
# 2    False
# 3    False
# 4    False
# dtype: bool

# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# dtype: bool

# 0    False
# 1    False
# 2     True
# 3     True
# 4     True
# dtype: bool

# 0     True
# 1     True
# 2     True
# 3    False
# 4     True
# dtype: bool

# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# dtype: bool

# 0     True
# 1     True
# 2    False
# 3     True
# 4    False
# dtype: bool
