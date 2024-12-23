import numpy as np
import matplotlib.pyplot as plt

yasListesi = [1,2,3,4,5,6,7,8,9]
kiloListesi = [10,20,30,40,50,60,70,85,96]

yl = np.array(yasListesi)
kl = np.array(kiloListesi)
plt.title("Yaş - Kilo Değişimi")
sonuc = plt.plot(yl,kl,"g")
plt.show()