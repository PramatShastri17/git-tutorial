print('Hello World!!')

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, 'b-',label='Sine')
plt.plot(x, y2, 'r-',label='Cosine')
plt.grid(linestyle='--')
plt.legend()
plt.show()
