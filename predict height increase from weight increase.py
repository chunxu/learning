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

#Input Split
X = df['weight'].values[:,np.newaxis]
y = df['height']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# import linear reg model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# sort the values of x in order to plot later *** forgot to do that in the beginning
import operator
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(X_test,y_test), key=sort_axis)
X_test, y_test = np.array(list(zip(*sorted_zip)))
X_test = X_test[:, np.newaxis]

# Degree 2 preprocesses X to 1, x and x^2
pre_process = PolynomialFeatures(degree=2)
X_poly2_train = pre_process.fit_transform(X_train)
X_poly2_test = pre_process.fit_transform(X_test)
#print(X_poly2_train.shape, X_poly2_test.shape, y_train.shape, y_test.shape)

# Degree 3 preprocesses X to 1, x, x^2 and x^3
pre_process = PolynomialFeatures(degree=3)
X_poly3_train = pre_process.fit_transform(X_train)
X_poly3_test = pre_process.fit_transform(X_test)
print(X_poly3_train.shape, X_poly3_test.shape, y_train.shape, y_test.shape)

#linearregression Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# predict the test set
y_linearpred = model.predict(X_test)

# Plot model on the data
plt.scatter(X_test, y_test, c = "yellow")
plt.xlabel("weight")
plt.ylabel("height")
plt.plot(X_test, y_linearpred)

#Evaluate LinearRegression Regression Model   
print("Linear Model Report")
print("MSE:",mean_squared_error(y_test, y_linearpred))
print("coef_", model.coef_)
print("score",model.score(X_test, y_test))

#Implement the second degree Polynomial Regression Model
poly_model = LinearRegression()
poly_model.fit(X_poly2_train, y_train)
y_poly2pred = poly_model.predict(X_poly2_test)
# Plot model on the data
plt.scatter(X_test, y_test, c = "orange")
plt.xlabel("weight")
plt.ylabel("height")
plt.plot(X_test, y_poly2pred)

#Evaluate Polynomial Regression Model
theta0 = poly_model.intercept_
_, theta1, theta2 = poly_model.coef_
#print out results
print("The second degree Polynomial Regression Model Report")
print("MSE:",mean_squared_error(y_test, y_poly2pred))
print("The second degree polynomial regression model as: y =", theta0, " + ", theta1, "x", " + ", theta2, "x^2")
print("score",poly_model.score(X_poly2_test, y_test))

#Implement the third degree Polynomial Regression Model
poly_model = LinearRegression()
poly_model.fit(X_poly3_train, y_train)
y_poly3pred = poly_model.predict(X_poly3_test)
# Plot model on the data
plt.scatter(X_test, y_test, c = "brown")
plt.xlabel("weight")
plt.ylabel("height")
plt.plot(X_test, y_poly3pred)

#Evaluate Polynomial Regression Model
theta0 = poly_model.intercept_
_, theta1, theta2, theta3 = poly_model.coef_

#print out results
print("The third degree Polynomial Regression Model Report")
print("MSE:",mean_squared_error(y_test, y_poly3pred))
print("The third degree polynomial regression model as: y =", theta0, " + ", theta1, "x", " + ", theta2, "x^2"," + ", theta3, "x^3")
print("score",poly_model.score(X_poly3_test, y_test))

'''
Comparing the three models (LinearRegression vs the second and third degree Polynomial Regression) by MSE and scores, the third degree Polynomial Regression Model performs best while the LinearRegression model performs worst.

For LinearRegression model, for every 10 units of increase in weight, the height increase would be: 10 times of 1.78654145 = 17.8654145

For the second and third degree Polynomial Regression Models, for every 10 units of increase in weight, the height increase would be denpending on the baseline of weight:

For example, using the second degree model: 
height increase = 10*(theta1 + theta2) + 20 * theta2 * base_weight
                = 10*(4.220558473637296 -0.038649397968607294) + 20*(-0.038649397968607294)* base_weight
                = 41.82 - 0.7730*base_weight, where base_weight is the weight before increase
            
'''           
