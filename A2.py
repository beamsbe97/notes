import tensorflow as tf
from keras.models import Sequential, Model
from keras.layers import Dense, Embedding, Flatten, Input, Concatenate
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
import os
import sklearn


os.chdir(r"C:\Users\nguye\Downloads\316_Assignments\NguyenQuocAn_A2")
df = pd.read_csv("secondary_data.csv", delimiter = ';')

categorical_columns=["class","cap-shape","cap-surface","cap-color", "does-bruise-or-bleed", "gill-attachment","gill-spacing","gill-color","season",\
                                 "stem-root","stem-surface","stem-color","veil-type","veil-color","has-ring","ring-type","spore-print-color", "habitat"]

numeric_columns = ["cap-diameter", "stem-height", "stem-width"]
#df = pd.get_dummies(df, columns=["class","cap-shape","cap-color", "does-bruise-or-bleed", "gill-attachment","gill-spacing","gill-color","season",\
#                                 "stem-root","stem-surface","stem-color","veil-type","veil-color","has-ring","ring-type","spore-print-color", "habitat"])
print(len(categorical_columns) + len(numeric_columns))
one_hot = OneHotEncoder(sparse_output=False)
transformer = ColumnTransformer([("one_hot",
                                 one_hot,
                                 categorical_columns)],
                                 remainder="passthrough")
encoded_df = transformer.fit_transform(df)
pd.DataFrame(encoded_df)
for col in numeric_columns:
    df[col] = StandardScaler().fit_transform(df[col].values.reshape(-1,1))

for col in categorical_columns:
    df[col] = OneHotEncoder().fit_transform(df[col])

df.info()

np.unique(df["class"])
tf.one_hot(df["class"], 2)




####
one_hot_features = df[[categorical_columns]]
numerical_features = df[[numeric_columns]]

one_hot_input = Input(shape=(one_hot_features.shape[1],), name='one_hot_input')
numerical_input = Input(shape=(numerical_features.shape[1],), name='numerical_input')

one_hot_layer = Dense(units=64, activation='relu')(one_hot_input)

# Numerical features
numerical_layer = Dense(units=64, activation='relu')(numerical_input)

concatenated = Concatenate()([one_hot_layer, numerical_layer])

# Add more layers as needed
output_layer = Dense(units=1, activation='sigmoid')(concatenated)
model = Model(inputs=[one_hot_input, numerical_input], outputs=output_layer)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x=[one_hot_features, numerical_features], y=target, epochs=epochs, batch_size=batch_size)


