import numpy as np
import pandas as pd

matris = np.random.randn(4,3)

dataFrame = pd.DataFrame(matris)
print(dataFrame)
print(type(dataFrame)) #dataframe olduğu görüldü
print(dataFrame[0]) #sütunu getirdi

############################################

yeniDataFrame = pd.DataFrame(matris ,index = ["gokhan","osman","mercan","gokce"], columns=["maas", "saat", "yas"])
print(yeniDataFrame)
#tek sütunu görme
print(yeniDataFrame["yas"])
#birden fazla sütunu görme
print(yeniDataFrame[["yas","maas"]])

#sadece tek indexe ait özellikleri görüntüleme (LOC fonksiyonu)
print(yeniDataFrame.loc["gokhan"])

#index bazlı loc fonksiyonu. iloc
print(yeniDataFrame.iloc[1])

#data frame'e kolon ekleme

yeniDataFrame["emeklilik yasi"] = yeniDataFrame["yas"] *2
print(yeniDataFrame)

#data frame'den sütun silme
yeniDataFrame.drop("emeklilik yasi", axis=1) #axis = 1 olursa sütun, 0 olursa satır siler
print(yeniDataFrame)

#üstteki değişiklikler geçidir. dataframe'de kalıcı değişiklik yapmaz.

yeniDataFrame.drop("maas",axis=1, inplace=True) #inplace true olduğunda gerçekten siler

print(yeniDataFrame)

#dataframe üzerinde şartlı arama yapabiliriz. True / False döndürür
print(yeniDataFrame<0)

#yaşı sıfırdan büyük olanların tüm bilgileri
print(yeniDataFrame[yeniDataFrame["yas"]>0])

#INDEX İŞLEMLERİ
#####################################################################
yeniIndeksListesi = ["g","o","m","gok"]

yeniDataFrame["yeni index"] = yeniIndeksListesi
yeniDataFrame.set_index("yeni index", inplace=True) #inplace True seçilmezse, değişiklik geçici olur
print(yeniDataFrame)

print(yeniDataFrame.loc["g"])