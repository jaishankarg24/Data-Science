#advantages of pandas over numpy:
    #using pandas we can store all category of data
    
import pandas as p
ds=p.Series([1,'sandesh',70.8,True,20+4j])
print(ds)

# o/p:
# ----
# 0          1
# 1    sandesh
# 2       70.8
# 3       True
# 4    (20+4j)
# dtype: object
