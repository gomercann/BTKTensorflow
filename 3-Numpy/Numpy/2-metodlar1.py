import numpy as np

list(range(0,10))

numlist = np.arange(0,10)
print(numlist)

ikiserliListe = np.arange(0,10,2)
print(ikiserliListe)

sifirListesi = np.zeros(5)
print(sifirListesi)

sifirMatrisi = np.zeros((8,8))
print(sifirMatrisi)

birMatrisi = np.ones((8,8))
print(birMatrisi)


##LINSPACE
#x'ten n'e kadar, y tane sayı oluşturmaya yarayan komuttur.
aralikli = np.linspace(0,20,5)
print(aralikli)

aralikli2 = np.linspace(0,10,20)
print(aralikli2)


##EYE
#n boyutunda birim matris oluşturmanıza yarar
birimMatris = np.eye(10)
print(birimMatris)