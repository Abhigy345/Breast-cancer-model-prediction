import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df = sklearn.datasets.load_breast_cancer()
print(df)
df_2 = pd.DataFrame(df.data, columns = df.feature_names)
df_2.head()
df_2.describe()
df_2.isnull().sum()
df_2['label'] = df.target
df_2.head()
df_2.value_counts('label')
df_2.groupby('label').mean()
X = df_2.drop(columns = 'label', axis = 1)
Y = df_2['label']
print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 3)
print(X.shape, X_train.shape, X_test.shape)
print(Y.shape, Y_train.shape, Y_test.shape)
model = LogisticRegression()
model.fit(X_train, Y_train)
acurracy_train_score = accuracy_score(model.predict(X_train), Y_train)
print(acurracy_train_score)
acurracy_test_score = accuracy_score(model.predict(X_test), Y_test)
print(acurracy_test_score)
input_data= (13.03,18.42,82.61,523.8,0.08983,0.03766,0.02562,0.02923,0.1467,0.05863,0.1839,2.342,1.17,14.16,0.004352,0.004899,0.01343,0.01164,0.02671,0.001777,13.3,22.81,84.46,545.9,0.09701,0.04619,0.04833,0.05013,0.1987,0.06169)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)
if (prediction[0] == 0):
  print('The Breast cancer is Malignant')
else:
  print('The Breast Cancer is Benign')
