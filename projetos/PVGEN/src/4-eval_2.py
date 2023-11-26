import numpy as np
import pandas as pd
from keras.models import load_model
import sklearn.metrics as metrics
import tensorflow as tf
import keras
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, InputLayer

###############################################################
##                       STRATEGY 1                          ##
###############################################################

'''
TL Strategy 1: In the first strategy, the weights of the initial layers are frozen and the only trainable weights
are the weights of the last hidden layer. This strategy is known as weight freezing and it is widely used in
order to extract features from the source domain and carry them to the target domain. This is a widely used
scheme when treating images, where the first layers are used as feature extraction layers and the last layers
are used to adapt to new data.
'''

## SEEDS
np.random.seed(42)
tf.random.set_seed(42)
random.seed(42)

# CONFIG 1
path_sets = f'sets_pv/gecad_from-unicamp/' #gecad_from-unicamp or gecad_from-unicamp-holanda
path_models = f'models_pv/' #PRE-TRAINED MODEL
horizont  = 15
days_backs = 3
exp = 1
path_model_best = f"{path_models}/best_model_h{horizont}_s{exp}.h5"

# Load the training, validation, and test datasets
x_valid = np.load(f'{path_sets}x_valid_{days_backs}_h{horizont}.npy')
y_valid = np.load(f'{path_sets}y_valid_{days_backs}_h{horizont}.npy')
x_test = np.load(f'{path_sets}x_test_{days_backs}_h{horizont}.npy')
y_test = np.load(f'{path_sets}y_test_{days_backs}_h{horizont}.npy')
y_valid = y_valid.reshape(y_valid.shape[0],y_valid.shape[1])
y_test = y_test.reshape(y_test.shape[0],y_test.shape[1])

model = keras.models.load_model(path_model_best)
print(model.summary())


# Evaluate the model on the test dataset
y_pred_test = model.predict(x_test, verbose=0)
mae_test = metrics.mean_absolute_error(y_test, y_pred_test)
rmse_test = np.sqrt(metrics.mean_squared_error(y_test, y_pred_test))
print(f'**** Performance without TL ****\n')
print(f'MAE {mae_test:.5f}')
print(f'RMSE {rmse_test:.5f}')

# Freeze all layers except the last hidden layer
for layer in model.layers[:-1]:
    layer.trainable = False

# Compile the model with frozen weights and a learning rate of 0.00001
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), loss='mean_squared_error')

# Train the model using only the validation dataset
history = model.fit(x_valid, y_valid, validation_data=(x_test, y_test), epochs=200)  

# Evaluate the model on the test dataset
y_pred_test = model.predict(x_test, verbose=0)
mae_test = metrics.mean_absolute_error(y_test, y_pred_test)
rmse_test = np.sqrt(metrics.mean_squared_error(y_test, y_pred_test))
print(f'**** Performance E1 TL ****\n')
print(f'MAE {mae_test:.5f}')
print(f'RMSE {rmse_test:.5f}')


###############################################################
##                       STRATEGY 2                          ##
###############################################################

'''
TL Strategy 2: In the second strategy, the base model is used as a weight initialization scheme for the TL
model. The weights of all layers of the TL model are initialized based on data from the source domain and they
are fine-tuned based on data from the target domain. This approach is extensively used with problems where
there is an abundance of data in the source domain, but a scarcity of data in the target domain. However, a
high degree of similarity between the source and the target domain is a necessary condition.
'''

model = keras.models.load_model(path_model_best)

model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.00001), loss='mean_squared_error')

# Fine-tune the model on the new dataset
history = model.fit(x_valid, y_valid, validation_data=(x_test, y_test), epochs=200)  # Adjust the number of epochs as needed

# Evaluate the model on the test dataset
y_pred_test = model.predict(x_test, verbose=0)
mae_test = metrics.mean_absolute_error(y_test, y_pred_test)
rmse_test = np.sqrt(metrics.mean_squared_error(y_test, y_pred_test))
print(f'**** Performance E2 TL ****\n')
print(f'MAE {mae_test:.5f}')
print(f'RMSE {rmse_test:.5f}')

###############################################################
##                       STRATEGY 3                          ##
###############################################################

'''
TL Strategy 3: In the third strategy, the initial layers of the TL model are frozen and the last layer is trained
from scratch, popping the last layer of the base model and adding a new layer after the frozen layers. This
approach is similar to the first one, but it differs in the fact that the weights of the last layer are not initialized
based on data from the source domain. Thus, the TL model serves as a feature extraction mechanism because
of the frozen layers, but it can also be fine-tuned to the target domain because of the random initialization
of the last layers weights.
'''

# Load the pre-trained model
model = keras.models.load_model(path_model_best)

# Remove the last layer
model.pop()

# Freeze all the remaining layers
for layer in model.layers:
    layer.trainable = False

# Add a new last layer for the target domain
# The number of units in the last layer should match the number of outputs you need
new_last_layer = Dense(15, activation='linear', name='new_dense')  # Adjust the number of units and activation function as needed
model.add(new_last_layer)

# Compile the model with a small learning rate for fine-tuning
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), loss='mean_squared_error')

# Fine-tune the model on the new dataset
history = model.fit(x_valid, y_valid, validation_data=(x_test, y_test), epochs=200)  # Adjust the number of epochs as needed

# Evaluate the model on the test dataset
y_pred_test = model.predict(x_test, verbose=0)
mae_test = metrics.mean_absolute_error(y_test, y_pred_test)
rmse_test = np.sqrt(metrics.mean_squared_error(y_test, y_pred_test))
print(f'**** Performance E3 TL ****\n')
print(f'MAE {mae_test:.5f}')
print(f'RMSE {rmse_test:.5f}')