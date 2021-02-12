#scattered graph
import matplotlib.pyplot as mp 
x1=[1,2,3,4,5,6,7,8]
y1=[75,83,73,73,73,67,45,78]

x2=[1,2,3,4,5,6,7,8]
y2=[56,67,78,89,45,56,34,54]

mp.scatter(x1,y1,color='red',label='sachin')
mp.scatter(x2,y2,color='black',label='dravid')

mp.title('scattered graph')
mp.xlabel('x axis')
mp.ylabel('y axis')
mp.legend()
mp.show()
# NOTE:
# -----
# -->Inorder to obtain scattered graph we have to make use of scatter() available within pyplot 
# submodule , matplotlib module