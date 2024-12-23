import numpy as np

benimDizim = np.arange(0,15)
print(benimDizim)

#dizinin n. elemanını listeleme
sonuc = benimDizim[5]
print(sonuc)

#dizinin belirli aralıktaki indexini listeler
sonuc = benimDizim[3:5]
print(sonuc)

#dizinin belirli bir kısmını değiştir
benimDizim[3:8] = -1
print(benimDizim)

#yeni dizi
baskaDizi = np.arange(0,24)

#baskadizi'nin bir bölümünü yeni bir diziye atadık
slincingDizisi = baskaDizi[4:9]

#dizinin bütün elemanlarını 700 yaptık.
slincingDizisi[:] = 700

#hem slicing, hem baskadizi'de de ilgili elemanların 700 olarak değiştiğini gör
print(slincingDizisi)
print(baskaDizi)

