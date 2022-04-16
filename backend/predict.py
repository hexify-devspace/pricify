from turtle import left
from keras import models
from keras import models
from keras.optimizers import adam_v2
from keras import backend as K
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
import pandas as pd

import os
from pathlib import Path

MODEL_PATH = os.path.join(Path(__file__).parent, "model")
DATASET_PATH = os.path.join(Path(__file__).parent, "datasets", "carsale.csv")


def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))

model = models.load_model(
    MODEL_PATH,
    custom_objects={
        "rmse": rmse,
        "Adam": adam_v2
    }
)


#make empty numpy array, copy format of the other one and then add an extra row for input.
y = pd.read_csv(DATASET_PATH)
y = y.drop(['min_cost_price', 'max_cost_price', 'selling_price'] , axis=1)

transformer = make_column_transformer(
    (MinMaxScaler(), 
        ['engine', 'mileage', 'seats', 
         'vehicle_age', 'km_driven', 'max_power']),
    (OneHotEncoder(handle_unknown='ignore'), 
        ['brand', 'model', 'fuel_type', 'sale_state'])
)

transformer.fit(y)

y = transformer.transform(y)
y = y.toarray()[:, 0:180]
prediction = model.predict(y)

print(np.expm1(prediction[:5]))
