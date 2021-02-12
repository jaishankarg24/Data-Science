#using line graph plot the data of 2 students a/c to thier sem percentage
import matplotlib.pyplot as mp 
x1=[1,2,3,4,5,6,7,8]
y1=[75,83,73,73,73,67,45,78]

x2=[1,2,3,4,5,6,7,8]
y2=[56,67,78,89,45,56,34,54]

mp.plot(x1,y1,color='red')
mp.plot(x2,y2,color='yellow')

mp.title('line graph')
mp.xlabel('x axis')
mp.ylabel('y axis')
mp.show()
