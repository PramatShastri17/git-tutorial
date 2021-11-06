print('Hello World!!')

import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = math.sin(x)

plt.plot(x, y, 'b-')
plt.show()
