#converting the given 2d array into 1d array:
#---------------------------------------------
	#flatten()
	#ravel()  
	
import numpy as n 

arr=n.array([[10,20],[30,40]])
print(arr)

print(arr.ndim)   #2
print(arr.shape)  #(2, 2)

# -----------------------------------------
res=arr.flatten()
print(res)       #[10 20 30 40]
print(res.ndim)  #1
# -------------------------------------------
res=arr.ravel()
print(res)       #[10 20 30 40]
print(res.ndim)  #1