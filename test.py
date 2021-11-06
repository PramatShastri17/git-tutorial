print('Hello World!!')

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.sin(x)

plt.plot(x, y, 'b-')
plt.grid(linestyle='--')
plt.show()
