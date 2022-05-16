#!/usr/bin/env python
# coding: utf-8

# #Find Outliers in Data

#import dependencies

import pandas as pd

import numpy as np

import plotly.express as px


#load the data into a dataframe

df = pd.read_csv("uber.csv")

#check the first 5 rows

df.head()



#drop the unnecessary columns

df = df.drop(columns=(['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']))


df.head()


df.describe()[['fare_amount', 'passenger_count']]



#create a histogram

fig = px.histogram(df, x='fare_amount')

fig.show()




#create a box plot

fig = px.box(df, y='fare_amount')

fig.show()



fig = px.scatter(x=df['passenger_count'], y=df['fare_amount'])

fig.show()




#create a function to find outliers using IQR

def find_outliers_IQR(df):

   q1=df.quantile(0.25)

   q3=df.quantile(0.75)

   IQR=q3-q1

   outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]

   return outliers



outliers = find_outliers_IQR(df['fare_amount'])

print('number of outliers: '+ str(len(outliers)))

print('max outlier value: '+ str(outliers.max()))

print('min outlier value: '+ str(outliers.min()))



outliers



outliers = find_outliers_IQR(df[['passenger_count','fare_amount']])



outliers


from scipy import stats
import numpy as np
z = np.abs(stats.zscore(df['fare_amount']))
print(z)




threshold = 3
print(np.where(z > threshold)) #row number


