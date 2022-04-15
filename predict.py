from turtle import left
from keras import models
from keras.optimizers import adam_v2
from keras import backend as K
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np
import pandas as pd

def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))

model = models.load_model("./tensorflow", custom_objects={"rmse": rmse, "Adam": adam_v2})

#make empty numpy array, copy format of the other one and then add an extra row for input.
y = np.zeros((2, 181)) #FIXME
y2 = pd.DataFrame(y)
X_train = pd.read_csv('carsaledataset.csv')
X_train = X_train.drop(X_train.index.to_list(), axis = 0)
X_train = X_train.drop(['selling_price', 'min_cost_price', 'max_cost_price', 'sale_state'], axis = 1)
X_train.add(y)

transformer = make_column_transformer(
    (MinMaxScaler(), 
        ['engine', 'mileage', 'seats', 
         'vehicle_age', 'km_driven', 'max_power']),
    (OneHotEncoder(handle_unknown='ignore'), 
        ['brand', 'model', 'fuel_type'])
)

transformer.fit(X_train)

X_train = transformer.transform(X_train)

predict = model.predict(X_train + y) 

print(predict)
