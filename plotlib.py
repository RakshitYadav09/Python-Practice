import numpy as np
import matplotlib.pyplot as plt 
print(np.pi)
print(np.tan(np.pi/2))
##using matplotlib with numpy

x=np.arange(1,11)
y=np.arange(10,110,10)

plt.figure(figsize=(6,6))
plt.plot(x,y,'r--')
plt.show()
