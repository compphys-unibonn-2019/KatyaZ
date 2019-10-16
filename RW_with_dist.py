#!/usr/bin/env python
# coding: utf-8

# In[66]:


import numpy as np
import matplotlib.pyplot as plt

distance = []
n = []

for N in range (100,5000,50):

    x = [0]
    y = [0]

    for i in range (N): 
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

    #plt.plot(x,y)
    #plt.scatter(x, y)
    #plt.show()

    distance.append(((abs(x[0] - x[N-1]))**2 + (abs(y[0] - y[N-1]))**2)**0.5)
    n.append(N)

#print(distance)
f = list(map(lambda x: (2 * x) ** 0.5, n))
plt.scatter(n, distance)
plt.plot(n,f, 'purple')
plt.show()

