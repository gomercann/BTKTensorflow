import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from keras.optimizers.optimizer_v1 import rmsprop
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from  tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.python.keras.saving.saved_model_experimental import sequential

df = pd.read_excel('bisiklet_fiyatlari.xlsx')
#print(df.head()) #veriyi ön incelemeye sokma

##############VERİYİ BÖLME#############
#denklemi unutma -> y = wx + b
#y-> label
y = df["Fiyat"].values

#x (özellik)
x = df[["BisikletOzellik1","BisikletOzellik2"]].values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33,random_state=15)
print(x_train.shape)
print(x_test.shape)


#########SCALING#################
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

############### MODEL OLUŞTURMA ###############
model = Sequential()

model.add(Dense(4,activation="relu"))  ##hidden layer içine 1 katman ve içine 4 nöron ekledik
model.add(Dense(4,activation="relu"))  ##hidden layer içine 1 katman ve içine 4 nöron ekledik
model.add(Dense(4,activation="relu"))  ##hidden layer içine 1 katman ve içine 4 nöron ekledik

model.add(Dense(1))
model.compile(optimizer = "rmsprop", loss="mse")


########## MODELİ EĞİTİME BAŞLATMA ############
model.fit(x_train,y_train,epochs=250)

loss =model.history.history["loss"]
sbn.lineplot(x=range(len(loss)),y=loss)

trainLoss = model.evaluate(x_train,y_train, verbose= 0)
testLoss = model.evaluate(x_test, y_test, verbose = 0)
plt.show()


################## PREDICTION (TAHMİN) #####################
tahmin =model.predict(x_test)
print(tahmin)
##array olarak gelen tahminleri seriye çevirdik
tahmin = pd.Series(tahmin.reshape(330,))

##tahminlerle gerçek verileri tek tabloya topladık
tahminDf = pd.DataFrame(y_test,columns=["Gerçek Y"])
tahminDf = pd.concat([tahminDf,tahmin],axis=1)
tahminDf.columns=["Gerçek Y","Tahmin Y"]
print(tahminDf)

sbn.scatterplot(x="Gerçek Y", y = "Tahmin Y", data=tahminDf)

from sklearn.metrics import mean_absolute_error, mean_squared_error
mean_absolute_error(tahminDf["Gerçek Y"],tahminDf["Tahmin Y"])


############ MODELİ YENİ VERİLERLE TEST ETME
yeniBisiklet = [[1760,1758]]
yeniBisiklet = scaler.transform(yeniBisiklet)
print(model.predict(yeniBisiklet))


############ MODELİ KAYDETME ##############
from tensorflow.keras.models import load_model
model.save("bisiklet_modeli.h5")

########### MODELİ ÇAĞIRMA ##############
cagirilan = load_model("bisiklet_modeli.h5")


##########ÇAĞIRILAN MODELDEN SORGULAMA YAPMA
cagirilan.predict(yeniBisiklet)
