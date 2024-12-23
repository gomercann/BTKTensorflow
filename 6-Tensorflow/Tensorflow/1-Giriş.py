import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

df = pd.read_excel('bisiklet_fiyatlari.xlsx')
print(df.head()) #veriyi ön incelemeye sokma

#veriyi birçok yönden görselleştirmeye yarayan pairplot komutu
sbn.pairplot(df)
plt.show()