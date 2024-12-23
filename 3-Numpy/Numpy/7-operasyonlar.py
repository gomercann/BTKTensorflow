import numpy as np

yeniDizi = np.random.randint(1,100,20)

print(yeniDizi)
#10'dan büyük rakamları bul
sonuc = yeniDizi >24
print(sonuc)

#sonuçları dizinin içinden seç
print(yeniDizi[sonuc])

sonDizi = np.arange(0,24)
print(sonDizi)

print(sonDizi-sonDizi)

print(np.sqrt(sonDizi))