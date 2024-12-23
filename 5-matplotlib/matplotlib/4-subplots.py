import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0,10,20)
dizi2 = dizi1 ** 3

(bf,be) = plt.subplots(nrows=1,ncols=2)

for eksen in be:
    eksen.plot(dizi1,dizi2,"g")
    eksen.set_xlabel("X Ekseni")

plt.tight_layout()
plt.show()