import numpy as np
m=4
n=3
a= np.ndarray(shape=(m, n))
for i in range(m):
    for j in range(n):
        if m>0 and n>0:
            a[i, j] = np.sin(n*i+m*j)
            if a[i, j] < 0:
                a[i, j] = 0
        elif m==0 and n==0:
            a[i, j] = np.sin(n*(i+1)+m*(j + 1))
print(a)