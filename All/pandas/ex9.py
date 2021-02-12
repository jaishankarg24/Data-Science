#Concatination of DataFrame

import pandas as p 

lst1=[10,20,30,40,50]
lst2=[30,40,30,20,50]

df1=p.DataFrame(lst1)
df2=p.DataFrame(lst2)

print(df1)
print(df2)

df3=df1.append(df2)
print(df3)

df4=p.concat([df1,df2])
print(df4)

o/p:
----
    0
0  10
1  20
2  30
3  40
4  50


    0
0  30
1  40
2  30
3  20
4  50



    0
0  10
1  20
2  30
3  40
4  50
0  30
1  40
2  30
3  20
4  50


    0
0  10
1  20
2  30
3  40
4  50
0  30
1  40
2  30
3  20
4  50