import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_excel("merc.xlsx")

###### VERİYİ İNCELEME ve ANLAMA ##########
#ilk 5 veri
print(df.head())
#verinin açıklaması
print(df.describe())

##eksik veri sayısını sütun isimlerine göre sırala
print(df.isnull().sum())
df = df.drop(["transmission"],axis=1)

sbn.displot(df["price"])
sbn.countplot(df["year"])
plt.show()
###fiyatı hangi sütunun ne kadar etkilediğine göre çıkarım oluşturma (korelasyon)
print(df.corr()["price"].sort_values())

sbn.scatterplot(x="mileage",y="price",data=df)
plt.show()


##########VERİYİ TEMİZLEME #########
#### Dataframe içerisindeki en yüksek fiyatlı 130 aracı ortalamayı çok bozdukları için attık.
df = df.sort_values("price", ascending=False).iloc[131:]

plt.figure(figsize =(7,5))
sbn.displot(df["price"])
plt.show()

print(df.groupby("year").mean(["price"]))

### MODELİ OLUŞTURMAK #######
y = df["price"].values
x = df.drop("price", axis=1).values

from sklearn.model_selection import train_test_split

x_train, x_test , y_train, y_test = train_test_split(x,y,test_size = 0.33, random_state=10)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))
model.add(Dense(12,activation="relu"))

model.add(Dense(1))
model.compile(optimizer = "adam", loss= "mse")

model.fit(x = x_train,y=y_train,validation_data=(x_test,y_test),epochs=300, batch_size=250)

from tensorflow.keras.models import load_model
model.save("arabamodeli.h5")