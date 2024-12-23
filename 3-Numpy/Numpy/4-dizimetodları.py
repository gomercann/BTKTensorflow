import numpy as np

benimRandomDizim = np.random.randint(0,100,30)

#diziyi n satır ve m sütüna böl ve matris oluştur
sonuc = benimRandomDizim.reshape(6,5)
print(sonuc)

#dizideki en büyük değer
sonuc = benimRandomDizim.max()
print(sonuc)

#dizideki en küçük değer
sonuc = benimRandomDizim.min()
print(sonuc)

#en büyük değerin indexi
sonuc = benimRandomDizim.argmax()
print(sonuc)

#En küçük değerin indexi
sonuc = benimRandomDizim.argmin()
print(sonuc)

