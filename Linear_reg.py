# Linear Regression with Python
# 
# ** This is mostly just code for reference. Please watch the video lecture for more info behind all of this code.**
# 
# Your neighbor is a real estate agent and wants some help predicting housing prices for regions in the USA. It would be great if you could somehow create a model for her that allows her to put in a few features of a house and returns back an estimate of what the house would sell for.
# 
# She has asked you if you could help her out with your new data science skills. You say yes, and decide that Linear Regression might be a good path to solve this problem!
# 
# Your neighbor then gives you some information about a bunch of houses in regions of the United States,it is all in the data set: USA_Housing.csv.
# 
# The data contains the following columns:
# 
# * 'Avg. Area Income': Avg. Income of residents of the city house is located in.
# * 'Avg. Area House Age': Avg Age of Houses in same city
# * 'Avg. Area Number of Rooms': Avg Number of Rooms for Houses in same city
# * 'Avg. Area Number of Bedrooms': Avg Number of Bedrooms for Houses in same city
# * 'Area Population': Population of city house is located in
# * 'Price': Price that the house sold at
# * 'Address': Address for the house

# **Let's get started!**
# ## Check out the data
# We've been able to get some data from your neighbor for housing prices as a csv set, let's get our environment ready with the libraries we'll need and then import the data!
# ### Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


USAhousing = pd.read_csv('USA_Housing.csv')

USAhousing.head()

USAhousing.info()

USAhousing.describe()

USAhousing.columns

sns.pairplot(USAhousing)

sns.distplot(USAhousing['Price'])

sns.heatmap(USAhousing.corr())

# ## Training a Linear Regression Model
# 
# Let's now begin to train out regression model! We will need to first split up our data into an X array that contains the features to train on, and a y array with the target variable, in this case the Price column. We will toss out the Address column because it only has text info that the linear regression model can't use.
# 
# ### X and y arrays

X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = USAhousing['Price']


# ## Train Test Split
# 
# Now let's split the data into a training set and a testing set. We will train out model on the training set and then use the test set to evaluate the model.

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)


# ## Creating and Training the Model

from sklearn.linear_model import LinearRegression

lm = LinearRegression()

lm.fit(X_train,y_train)

