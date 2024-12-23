import numpy as np
import matplotlib.pyplot as plt


dizi1 = np.linspace(0,10,20)
dizi2 = dizi1 **2

#scatter grafik
plt.scatter(dizi1,dizi2)
plt.show()

#histogram
dizi3 = np.random.randint(0,100,50)
plt.hist(dizi3)
plt.show()

#boxplot
plt.boxplot(dizi3)
plt.show()