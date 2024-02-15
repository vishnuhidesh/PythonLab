import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x, y, label=r'$x^2$')
plt.title('Plot of the function $x^2$')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
