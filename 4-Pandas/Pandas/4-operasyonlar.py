import numpy as np
import pandas as pd

sozlukVerisi = {"istanbul": [30,29,np.nan],"ankara": [15,np.nan,19], "mersin" : [30,40,45]}
havaDurumuDataFrame = pd.DataFrame(sozlukVerisi)
print(havaDurumuDataFrame)


########EKSİK DEĞERLERLE ÇALIŞMA
#axis 0 olursa, nan değer olmayan tüm satırları listeler. 1 olursa, nan olmayan tüm sütunları listeler
print(havaDurumuDataFrame.dropna(axis=0))
print(havaDurumuDataFrame.dropna(axis=1, thresh=2)) #thresh eşik değerdir. 2'den fazla nan olanları siler.

########### GROUP BY KOMUTU
maasSozlugu = {"Departman": ["Yazılım","Yazılım","Pazarlama","Pazarlama","Hukuk","Hukuk"],
               "Çalisan Ismi": ["Ahmet","Mehmet","Gokhan","Osman","Mercan","Tuna"],
               "Maas": [100,150,200,220,90,300]}

maasDataFrame = pd.DataFrame(maasSozlugu)
print(maasDataFrame)

#departmana göre grupla
grupObjesi = maasDataFrame.groupby("Departman")

##departmanlarda kaçar kayıt olduğunu listele
print(grupObjesi.count())

print(grupObjesi.max())

print(grupObjesi.min())

print(grupObjesi.describe())
