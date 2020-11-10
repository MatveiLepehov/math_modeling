import numpy as np
A = 5
def mult_func(b):
    c = 0
    for x in b:
        c = c + x
    print(c/len(b))
a = np.array([1,2,3,4,5])
mult_func(a)
