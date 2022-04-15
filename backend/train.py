# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

from keras import Sequential
from keras.layers import Dense
from keras.optimizers import adam_v2
from keras import backend as K
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import mean_squared_error as msle
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

import os
from pathlib import Path

DATASET_PATH = os.path.join(Path(__file__).parent, "datasets", "carsale.csv")
MODEL_OUTPUT_PATH = os.path.join(Path(__file__).parent, "model")

rs = 0

data = pd.read_csv(DATASET_PATH)
data = data.drop(['min_cost_price', 'max_cost_price'] , axis=1)
data.head()

train, test = train_test_split(data, test_size=1/20, random_state=rs)
train, valid = train_test_split(train, test_size=1/19, random_state=rs)

test_new = train.drop(['selling_price'] , axis=1)
nrow_train = train.shape[0]
y = np.log1p(train["selling_price"])
merge: pd.DataFrame = pd.concat([train, test_new])

# convert all data to matrices the AI can understand
transformer = make_column_transformer(
    (MinMaxScaler(), 
        ['engine', 'mileage', 'seats', 
         'vehicle_age', 'km_driven', 'max_power']),
    (OneHotEncoder(handle_unknown='ignore'), 
        ['brand', 'model', 'fuel_type', 'sale_state'])
)

X_train, X_test, y_train, y_test = train_test_split(
    test_new, y, test_size=0.05, random_state=42
)

# Fit
transformer.fit(X_train)

# Apply the transformation
X_train = transformer.transform(X_train)
X_test = transformer.transform(X_test)

# Make an rmse function to see progress
def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))

tf.random.set_seed(0)
model = Sequential([
    Dense(256, activation='relu'),
    Dense(256, activation='relu'),
    Dense(128, activation='relu'),
    Dense(1)
])

model.compile(
    loss=rmse,
    optimizer='Adam',
    metrics=[rmse]
)

model.fit(X_train.toarray(), y_train, epochs=175)
model.save(MODEL_OUTPUT_PATH)
