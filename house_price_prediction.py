#oringinally drafted in jupter notebook
import numpy as np
import pandas as pd
#pip install plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.datasets import load_boston
load_boston = load_boston()
x = load_boston.data
y = load_boston.target

data = pd.DataFrame(x, columns = load_boston.feature_names)
data['SalePrice'] = y
data.head()

print(load_boston.DESCR)
data.shape
data.info()
data.describe()

data.isnull().sum()

sns.pairplot(data,height=2.5)
plt.tight_layout()

sns.distplot(data['SalePrice'])
print('Skewness: %f' % data['SalePrice'].skew())
print('Kurtosis: %f' % data['SalePrice'].kurt())

fig, ax = plt.subplots()
ax.scatter(x = data['CRIM'], y= data['SalePrice'])
plt.ylabel('SalePrice', fontsize = 13)
plt.xlabel('CRIM', fontsize = 13)
plt.show()

fig, ax = plt.subplots()
ax.scatter(x = data['AGE'], y= data['SalePrice'])
plt.ylabel('SalePrice', fontsize = 13)
plt.xlabel('AGE', fontsize = 13)
plt.show()

from scipy import stats
from scipy.stats import norm, skew
sns.distplot(data['SalePrice'], fit=norm);
(mu, sigma) = norm.fit(data['SalePrice'])

print('\n mu={:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

plt.legend(['Normal dist.($\mu=${:.2f} and $\sigma=${:.2f})'.format(mu,sigma)],
          loc='best')
plt.ylabel('Frequency')
plt.title('SalePrice distribution')

#get qq plot
fig = plt.figure()
res= stats.probplot(data['SalePrice'], plot=plt)
plt.show()

data['SalePrice'] = np.log1p (data['SalePrice'])
sns.distplot(data['SalePrice'], fit=norm);
(mu, sigma) = norm.fit(data['SalePrice'])
print('\n mu={:.2f} and sigma = {:.2f}\n'.format(mu, sigma))

plt.legend(['Normal dist.($\mu=${:.2f} and $\sigma=${:.2f})'.format(mu,sigma)],
          loc='best')
plt.ylabel('Frequency')
plt.title('SalePrice distribution')

#get qq plot
fig = plt.figure()
res= stats.probplot(data['SalePrice'], plot=plt)
plt.show()


#Data correlation

plt.figure(figsize=(10,10))
cor = data.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.PuBu)
plt.show()

cor_target = abs(cor['SalePrice']) # absolute value of corelation
relevant_features = cor_target[cor_target>0.2] #highly correlated features
names  = [index for index, value in relevant_features.iteritems()]
names.remove('SalePrice') #remove target feature

print(names)
print(len(names))

from sklearn.model_selection import train_test_split
X =data.drop('SalePrice', axis=1)
y =data['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

predictions = lr.predict(X_test)
print("Actual value of the house: - ", y_test[0])
print("Model predicted value: - ", predictions[0])

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, predictions)
rmse=np.sqrt(mse)
print (mse)
print (rmse)
