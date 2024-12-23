import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from tensorflow.keras.models import load_model

model = load_model("arabamodeli.h5")


from sklearn.metrics import mean_squared_error, mean_absolute_error
tahminDizisi = model.predict()