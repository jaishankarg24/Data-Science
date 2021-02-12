#functions associated with DataFrame

import pandas as p 
d={'name':('sachin','dravid'),'age':[48,40],'gender':('male','male')}
cid=(10,19)
df=p.DataFrame(d,index=cid)
print(df)

print(df.info()) #used to fetch data w.r.t Dataframe
print(df.head()) #used to display the data from the top
print(df.tail()) #used to display the data
print(df.tail(1))


# o/p:
# ----
#       name  age gender
# 10  sachin   48   male
# 19  dravid   40   male


# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 2 entries, 10 to 19
# Data columns (total 3 columns):
# name      2 non-null object
# age       2 non-null int64
# gender    2 non-null object
# dtypes: int64(1), object(2)
# memory usage: 48.0+ bytes
# None


#       name  age gender
# 10  sachin   48   male
# 19  dravid   40   male


#       name  age gender
# 10  sachin   48   male
# 19  dravid   40   male


#       name  age gender
# 19  dravid   40   male

