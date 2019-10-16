#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

x = [0]
y = [0]

for i in range (100): 
    rand1 = np.random.uniform(0., 2., 2)
    #print(rand1)
    if rand1[0] >= 1:
        x.append(x[i] + 1)
    else:
        x.append(x[i] - 1)
    
    if rand1[1] >= 1:
        y.append(y[i] + 1)
    else:
        y.append(y[i] - 1)     

plt.plot(x,y)
plt.scatter(x, y)
plt.show()
    
        

