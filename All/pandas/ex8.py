#Program to store the complex data within a DataFrame

import pandas as p
d={'name':('sachin','dravid'),'age':[48,40],'gender':('male','male')}
cid=(10,19)
df=p.DataFrame(d,index=cid)
print(df)

# o/p:
# ----
#       name  age gender
# 10  sachin   48   male
# 19  dravid   40   male