import numpy as np
import matplotlib.pyplot as plt


x=np.arange(-5,5,0.1)

y=np.power(x,2)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=x^2")
plt.show()
print(x)
