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
e=np.arange(1,100,2)
print(e)
e=e.reshape((10,5))
print(e)
f=np.arange(0,18).reshape((6,3))
g=np.arange(12,30).reshape((3,6))
print(f)
print(g)
h=f@g
print(h)
print(h.max())


print(np.random.randint(1,12,(3,3,5)))

s1="hello guys"
s2="whats up"

print(np.char.add(s1,s2))
print(np.char.upper(s1))
print(np.char.split(s1))
print(np.char.splitlines(s1))
print('\n')
print(np.char.center('BYEBYE',40,'-'))