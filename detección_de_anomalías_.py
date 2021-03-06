# -*- coding: utf-8 -*-
"""detección de anomalías .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hVlICEOrTRlSMKUWUUUZMO6OrouZqJzt
"""

import pandas as pd
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from numpy import where

data = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

df = data[["sepal_length", "sepal_width"]]

model = OneClassSVM(kernel = 'rbf', gamma = 0.001, nu = 0.03).fit(df)

y_pred = model.predict(df)
y_pred

outlier_index = where(y_pred == -1)
outlier_values = df.iloc[outlier_index]
outlier_values

plt.scatter(data["sepal_length"], df["sepal_width"])
plt.scatter(outlier_values["sepal_length"], outlier_values["sepal_width"], c = "r")