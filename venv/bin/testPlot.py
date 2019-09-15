import matplotlib.pyplot as plt
import numpy as np
import math

plt.figure(1)


a = 67147.97326736226
b = -67106.96010367322
c = -1.3043121533668034e-05
size = 250
t = np.array([i*0.04 for i in range(size)])
y = np.zeros(len(t))
for i in range(size):
    y[i] = a+b* math.pow(math.e,-c*t[i])
plt.plot(t,y)
plt.show()
