#pie chart

import matplotlib.pyplot as mp 

labels=['python','Java','C','C++']
size=[270,200,150,50]
colors=['blue','red','green','pink']
explode=[0.3,0.2,0,0]
mp.pie(size,labels=labels,colors=colors,explode=explode)
mp.title('pie chart')
mp.legend()
mp.show()