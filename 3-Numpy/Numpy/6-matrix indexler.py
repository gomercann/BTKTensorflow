import numpy as np

benimListem = [[10,20,30],[30,40,50],[60,70,80]]
benimMatrisDizim = np.array(benimListem)

#eleman çağırma
print(benimMatrisDizim[0])
print(benimMatrisDizim[0][2])
print(benimMatrisDizim[1,2])

#matriste slicing yapma

#n. satırdan itibaren, m. indexleri getir
sonuc = benimMatrisDizim[1:,2]
print(sonuc)

#n. satırdan itibaren, m. indexten itibaren değerleri getir
sonuc = benimMatrisDizim[0:,1:]
print(sonuc)
print(type(sonuc)) #numpy array olarak döndüğünü gör


##############################################################

yeniListe = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
yeniMatris = np.array(yeniListe)

print(yeniMatris)

print(yeniMatris[[4,2,0]])