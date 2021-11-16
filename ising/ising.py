import numpy as np
import matplotlib.pyplot as plt


N = 50

magnet = np.random.random([N,N])
magnet[magnet > 0.5] = 1
magnet[magnet<= 0.5] = -1




plt.imshow(magnet, cmap='binary')
plt.show()