import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a[1, :]) #вывести строку
print(a[:, 1]) #вывести столбец 
b= a[:, ::-1]
print (b)
#[start:stop:step]
# по умолчанию 
#start=0
#stop=len (строки или столбцы)
#step=1