import numpy as np
import pandas as pd

sozluk1 = {"isim": ["ahmet", "mehmet", "zeynep", "atil"],
           "spor": ["koşu", "yüzme", "koşu", "basketbol"],
           "kalori": [100,200,300,400]}

dataframe1 = pd.DataFrame(sozluk1, index=[0,1,2,3])

sozluk2 = {"isim": ["osman", "levent", "Atlas", "Fatma"],
           "spor": ["koşu", "yüzme", "koşu", "basketbol"],
           "kalori": [200,100,50,300]}
dataframe2 = pd.DataFrame(sozluk2, index=[4,5,6,7])

sozluk3 = {"isim": ["ayse", "mahmut", "duygu", "nur"],
           "spor": ["koşu", "yüzme", "badminton", "tenis"],
           "kalori": [300,400,500,250]}
dataframe3 = pd.DataFrame(sozluk3,index=[8,9,10,11])

#concat komutu ile 3 dataframe'i birleştirme yapıyoruz
sonuc = pd.concat([dataframe1,dataframe2,dataframe3])
print(sonuc)

