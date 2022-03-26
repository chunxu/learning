# Use regression models to predict height increase from weight increase

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
%matplotlib inline
warnings.filterwarnings('ignore')

#Loading the dataset
df = pd.read_csv('C:/Users/gaoch/Downloads/candidate_project/height_data.csv')
#see what the data look like
df.head()

# statistical information on the numbers in the dataset
df.describe()

# datatype information
df.info()

# check for null values
df.isnull().sum() #perfect! No null values found.

# create box plots to check outliers:
fig, ax = plt.subplots(ncols=4, nrows=1, figsize=(10, 5))
index = 0
ax = ax.flatten()

for col, value in df.items():
    sns.boxplot(y=col, data=df, ax=ax[index])
    index += 1
plt.tight_layout(pad=0.5, w_pad=0.5, h_pad=5.0) # seems weight data points have outliers


#Calculate corelation between features (weight, age, male) and target (height)
corr = df.corr()
plt.figure(figsize=(10,5))
sns.heatmap(corr, annot=True, cmap='coolwarm')


'''
It looks like 'male' has little impact on height (coefficient=0.14).
Age showed strong and similar correlation with both height and weight so it is not an independent feature from weight.
To predict height increase from weight increase, will use weight values only to fit models
'''

#visualize height by weight
sns.regplot(y=df['height'], x=df['weight'])
# A simple linear reg model kinds of fit the data, but not very well.

# try polynormial regression with one increased degree
sns.regplot(data=df, y = 'height',x = 'weight', order =2)


# try polynormial regression with one increased degree
sns.regplot(data=df, y = 'height',x = 'weight', order =3)

'''
The polynormial regression model fit the data much better compared to simple linear regression.
Will use both methods and then compare their performances by mean_squared_error.
Final calculation of increased height based on increased weight will be via formular from the Regression Models
'''
