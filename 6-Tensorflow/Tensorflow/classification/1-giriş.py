import pandas as pd
import numpy as np
from pandas import read_excel
import matplotlib.pyplot as plt
import seaborn as sbn

df = read_excel("maliciousornot.xlsx")

print((df.info()))
print((df.describe()))
print(df.corr()["Type"].sort_values())



y = df["Type"].values
x = df.drop("Type",axis=1).values

######### veriyi test ve train olarak bölme
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=15)

#### df'i scale etme
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

############# modeli oluşturma ############
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping

model = Sequential()

model.add(Dense(units=30,activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(units=15,activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(units=15,activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(units=1,activation="sigmoid")),

model.compile(loss="binary_crossentropy", optimizer="adam")
early = EarlyStopping(monitor="val_loss",mode = "min",verbose=1,patience=25)


model.fit(x=x_train,y=y_train,epochs=700,validation_data=(x_test,y_test),verbose=1,callbacks=[early])

from tensorflow.keras.models import load_model
model.save("siniflandırma_modeli.h5")

kayipDf = pd.DataFrame(model.history.history)
kayipDf.plot()
tahmin = (model.predict(x_test) > 0.5).astype("int32")


##test sonuçları
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test,tahmin))
print(confusion_matrix(y_test,tahmin))



