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

