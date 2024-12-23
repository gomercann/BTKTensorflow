import numpy as np
import pandas as pd

#SERİLER
benimSozlugum = {"Gokhan" : 50, "Zeynep":40, "Mehmet":30}

olusanSeri = pd.Series(benimSozlugum)
print(olusanSeri) #sözlüğü anlamlı bir biçime çevirdi
print(type(olusanSeri)) #pandas.core series olarak döndü

benimYaslarim = [30,40,50]
benimIsimlerim = ["gokhan", "osman", "mercan"]

sonuc = pd.Series(data = benimYaslarim, index = benimIsimlerim)
print(sonuc)


#numpy dizisi ile seri oluşturma

numpyDizisi = np.array([50,40,30])
sonuc = pd.Series(numpyDizisi)
print(sonuc)

#yeni örnek
yarismaSonucu1 = pd.Series([10,5,1],["gokhan","osman","mercan"])
yarismaSonucu2 = pd.Series([20,10,8],["gokhan","osman","mercan"])

#aynı indexe sahip değerleri toplamak mümkün:
sonuc = yarismaSonucu2 + yarismaSonucu1
print(sonuc)

####################################################

farkliSeries = pd.Series([20,30,40,50,60],["a","b","c","d","e"])
farkliSeri2 = pd.Series([30,40,50,60,70],["a","c","d","f","g"])

sonuc = farkliSeri2 + farkliSeries
print(sonuc)

