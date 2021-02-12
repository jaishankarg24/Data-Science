#Disadvantages of Numpy:
#-----------------------
#It cannot store heterogeneous data , if we try to store then the type of the object will be 
#converted based upon the heirarchy
#---------
# int
# float
# complex
# boolean
# string

import numpy as n
arr=n.array([1,'sandesh',70.8,True,20+4j])
print(arr)  #['1' 'sandesh' '70.8' 'True' '(20+4j)']

