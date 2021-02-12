#Bar Graph

import matplotlib.pyplot as mp 
x1=[1,2,3,4,5,6,7,8]
y1=[75,83,73,73,73,67,45,78]

x2=[1,2,3,4,5,6,7,8]
y2=[56,67,78,89,45,56,34,54]

mp.bar(x1,y1,color='red',label='sachin')
mp.bar(x2,y2,color='yellow',label='dravid')

mp.title('bar graph')
mp.xlabel('x axis')
mp.ylabel('y axis')
mp.legend()
mp.show()
# NOTE:
# -----
# -->Inorder to obtain bar graph we have to make use of bar() available within pyplot submodule , 
# matplotlib module
# -->inorder to display label we have to use legend()
# -->Inorder to display any graph we have to use show() 