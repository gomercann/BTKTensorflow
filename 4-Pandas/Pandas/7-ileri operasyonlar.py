import numpy as np
import pandas as pd

maasSozluk = {"isim": ["gokhan","osman","mercan", "gökçe"],
              "departman": ["yazılım","satış","pazarlama", "yazılım"],
              "maaş": [200,300,400,500]}

df = pd.DataFrame(maasSozluk)

#tekrar etmeden değerleri listele
print(df["departman"].unique())

#değer çeşidi sayısı
print(df["departman"].nunique())

#sütundaki tekrar eden veri sayısı
print(df["departman"].value_counts())

#dataframe'e fonksiyon uygulama
def bruttenNete(maas):
    return maas * 0.66

print(df["maaş"].apply(bruttenNete))

### boş olup olmama sorgulama (true false döndürür)
print(df.isnull())


##########  PİVOT TABLE #############

sozluk = {"sınıf": ["south park", "south park", "simpson", "simpson","simpson"],
          "isim": ["cartman","kenny", "homer", "bart","bart"],
          "yas": [9,10,50,20,10]}

df2 = pd.DataFrame(sozluk)

print(df2.pivot_table(values = "yas", index = ["sınıf","isim"]))