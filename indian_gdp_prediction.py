# -*- coding: utf-8 -*-
"""indian-gdp-prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hV5icDerw_zyvGU1XXafj1kE9ExBgdEp
"""

from google.colab import drive

drive.mount('/content/gdrive')

cd /content/gdrive/My Drive/indian_gdp_prediction

ls

import numpy as np 
import pandas as pd

import codecs
path = 'gdp_1960_2020.csv'
with codecs.open(path, 'r', 'utf-8', 'ignore') as f:
    gdp = pd.read_csv(f)
gdp[0:2]

gdp.columns

gdp['country'].unique()

india_gdp=gdp[gdp['country']=='India']
india_gdp

india_gdp.drop(['rank','state','gdp_percent'], axis = 1, inplace = True)

india_gdp

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize = (10,7))
sns.barplot(x = 'year',
y = 'gdp',
hue = 'country',
data = india_gdp)
plt.xticks(rotation = 90)
plt.title("India's GDP")
plt.show()

x1 = india_gdp.drop(['gdp', 'country'], axis=1)
y1 = india_gdp['gdp']

print(x1.shape)
print(y1.shape)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x1, y1, test_size = 0.2)

model_india=LinearRegression()
model_india.fit(x1,y1)

print("Coefficient: ",model_india.coef_)
print("intercept: ",model_india.intercept_)
pred = model_india.predict(x1)

plt.figure(figsize=(8,6))
plt.scatter(x1,y1,label='Acutal value')
plt.plot(x1,pred,color='tab:orange',label='Predicted value')
plt.legend()
plt.title("India",color='m')
plt.xlabel("Years",color='r')
plt.ylabel("per year INDIAN gdp",color='c')
plt.tight_layout()
plt.show()

years=[2021,2022,2023,2024,2025]
for i in years:
    print(model_india.predict([[i]]))

year=int(input("Enter year : "))
print(model_india.predict([[year]]))