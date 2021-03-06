import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x ** 2) + 1
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='$\sinx+1$', color='red', linewidth=2)
plt.plot(x, z, label='$cos^2+1$')
plt.xlabel('Times(s)')
plt.ylabel('Volt')
plt.title('A Simple Example')
plt.ylim(0, 2.2)
plt.legend()
plt.show()
