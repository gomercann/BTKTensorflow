from cProfile import label

import numpy as np
import matplotlib.pyplot as plt

dizi1 = np.linspace(0,10,20)
dizi2 = dizi1 ** 3

fg = plt.figure()
#figure parantezi içine alınabilecek değerler de var.
#figsize etiketi ile kalınlık ayarları yapılır
#dpi değeri ile grafik çözünürlüğünü ayarlamak mümkün


eksen = fg.add_axes([0.1 ,0.1, 0.9, 0.9])
eksen.plot(dizi1,dizi1**2,label = "Dizi **3")
eksen.plot(dizi1,dizi1**3,label="dizi **5")
eksen.legend() #eksenlerin açıklamaları. içine "loc =" etiketi konarak grafik içinde konumlandırılabilir
plt.show()

#oluşan grafiği dpi seçerek kaydetme
fg.savefig("benimfigurum.png",dpi=200)
