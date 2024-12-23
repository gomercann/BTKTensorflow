import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0,10,20)

dizi2 = dizi1 ** 3

## g değerinin yerine g-- yazarsan kesik çizgi, g*- yazarsan yıldızlı çizgi
plt.plot(dizi1,dizi2,"g*-")
plt.show()

plt.subplot(1,2,1)
plt.plot(dizi1,dizi2,"r*-")
plt.subplot(1,2,2)
plt.plot(dizi2,dizi1,"b*-")
plt.show()


########FİGÜRLER
fg = plt.figure()
axe = fg.add_axes([0.2,0.2,0.9,0.9])
axe.plot(dizi1,dizi2,"g*-")
axe.set_xlabel("x ekseni")
axe.set_ylabel("y ekseni")
axe.set_title("başlık")

plt.show()