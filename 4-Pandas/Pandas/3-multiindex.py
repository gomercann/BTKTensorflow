import numpy as np
import pandas as pd

ilkIndeksler = ["simpson","simpson", "simpson", "south park","south park", "south park"]
icIndeksler = ["homer","bart","marge", "cartman", "kenny", "kyle"]

#listeleri birleştirme
birlesmisIndeks = list(zip(ilkIndeksler, icIndeksler))
print(birlesmisIndeks)
#multi index oluşturma
birlesmisIndeks = pd.MultiIndex.from_tuples(birlesmisIndeks)
print(birlesmisIndeks)

benimCizgiFilmListem = [[40,"a"],[10,"b"],[30,"c"],[9,"d"],[10,"e"],[11,"f"]]
cizgiFilmNumpyDizisi = np.array(benimCizgiFilmListem)
cizgiFilmDataFrame = pd.DataFrame(cizgiFilmNumpyDizisi,index = birlesmisIndeks, columns=["yas","meslek"])

print(cizgiFilmDataFrame)
print(cizgiFilmDataFrame.loc["simpson"])
print(cizgiFilmDataFrame.loc["south park"].loc["kenny"])