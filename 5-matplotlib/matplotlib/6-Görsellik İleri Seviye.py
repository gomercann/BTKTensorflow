import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0,10,20)
dizi2 = dizi1 **2

(fg,eksen) = plt.subplots()

#çizdirme yaparken "g", "b" gibi renkler yerine, color = HEXKODU ile renk seçmek mümkün
#alpha değeri saydamlık oranıdır. 0 ile 1 arasında değer alır. 1 en opak, 0 en saydamdır
#linewidth değeri ile çizgi kalınlığını özelleştirmek mümkün.
#linestyle ile çizgi biçimini ayarlamak mümkün. .,-,:, -., gibi seçenekler mevcut.
#marker ile işaretler eklemek mümkün.
#marker eklendiyse, marker özelleştirilebilir. markersize ile boyut, markerfacecolor ile renk seçimi mümkün.
eksen.plot(dizi1, dizi2, color= "#C85F12", alpha = 0.1)
eksen.plot(dizi2, dizi1, "b", linewidth = 4.0)
eksen.plot(dizi2, dizi2+30, "y", linewidth = 2.0, linestyle="--")
eksen.plot(dizi2, dizi2*4, "y", linewidth = 2.0, linestyle="-.",marker = "+")
plt.show()