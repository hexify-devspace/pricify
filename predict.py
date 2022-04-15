from tensorflow.keras import models
from keras.optimizers import adam_v2
from keras import backend as K
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import numpy as np

def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))

model = models.load_model("./tensorflow", custom_objects={"rmse": rmse, "Adam": adam_v2})

X_train = np.empty((1, 181)) #something to make an empty 1, 181 array i forgot syntax lmao
# print(X_train)

transformer = make_column_transformer(
    (MinMaxScaler(), 
        ['engine', 'mileage', 'seats', 
         'vehicle_age', 'km_driven', 'max_power']),
    (OneHotEncoder(handle_unknown='ignore'), 
        ['brand', 'model', 'fuel_type', 'sale_state'])
)

transformer.fit(X_train)

X_train = transformer.transform(X_train)

predict = model.predict(X_train)

print(predict)
