import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0,10,20)
dizi2 = dizi1 ** 3

fg = plt.figure()
eksen1 = fg.add_axes([0.1,0.1,0.7,0.7])
eksen2 = fg.add_axes([0.2,0.4,0.2,0.2])

eksen1.plot(dizi1,dizi2,"g")
eksen1.set_xlabel("x ekseni")
eksen1.set_ylabel("y ekseni")
eksen1.set_title("Ana Grafik Başlık")

eksen2.plot(dizi2,dizi1,"b")
eksen2.set_xlabel("X Ekseni")
eksen2.set_ylabel("Y Ekseni")
eksen2.set_title("Küçük Grafik Başlık")

plt.show()

plt.subplot()