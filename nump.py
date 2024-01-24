import numpy as np
import sys
a=np.array([2,3,4,5,3,2,6])
d=np.array([[1,2,3],
           [2,3,4]])
print(d)
print(d.dtype)
print(d.size)
print(a[4]-d[1])
print(d[1,-1])
print(d.ndim)
b=np.empty((4,4), dtype=float)
c=np.ones((6,5), dtype=int)
e=np.ones((4,4), dtype=str)
print(b)
print(c)
print(e)