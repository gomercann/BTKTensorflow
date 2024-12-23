import numpy as np
import pandas as pd

sozluk1 = {"isim": ["ahmet", "mehmet", "gökhan", "osman"],
           "spor": ["futbol", "basketbol", "voleybol", "basketbol"]}

dataframe1 = pd.DataFrame(sozluk1)

sozluk2 = {"isim": ["ahmet", "mehmet", "gökhan", "osman"],
           "kalori": [100,200,300,400]}

dataframe2= pd.DataFrame(sozluk2)

#ortak kolon seçerek dataframe birleştirme yaptık
sonuc = pd.merge(dataframe1,dataframe2, on = "isim")
print(sonuc)