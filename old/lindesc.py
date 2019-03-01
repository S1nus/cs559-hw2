import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from matplotlib import style
from sklearn.model_selection import train_test_split

style.use('fivethirtyeight')
from sklearn.neighbors import KNeighborsClassifier

# 0. Load in the data and split the descriptive and target feature
df = pd.read_csv('wine.data', sep=',', names=
['target','Alcohol','Malic_acid','Ash','Akcakinity','Magnesium','Total_pheonols','Flavanoids','Nonflavanoids','Proanthocyanins','Color_intensity','Hue','OD280','Proline'])

X = df.iloc[:, 1:].copy()
target = df['target'].copy()

X_train, X_test, y_train, y_test = train_test_split(X,target,test_size=0.3,random_state=0)
for col in X_train.columns:
	X_train[col] = StandardScaler().fit_transform(X_train[col].values.reshape(-1,1))
