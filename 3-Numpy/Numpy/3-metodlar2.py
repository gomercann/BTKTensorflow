import random

import numpy as np

#random
#rastgele değer üretmeye yarar.

uretilen = np.random.randn(8)  #n tane sayı üret
print(uretilen)

uretilen=np.random.randn(4,4)  #n x n'lik rastgele sayı matrisi oluştur
print(uretilen)

uretilen = np.random.randint(1,10)  #belirtilen rakamlar arasında rastgele sayı üret
print(uretilen)

uretilen = np.random.randint(1,10,5)  #belirtilen rakamlar arasında rastgele array üret
print(uretilen)
print(type(uretilen)) #tipinin numpy array olduğunu gör

