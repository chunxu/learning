#!/usr/bin/env python
# coding: utf-8

# #Find Outliers in Data

# In[1]:


#import dependencies

import pandas as pd

import numpy as np

import plotly.express as px


# In[4]:


#load the data into a dataframe

df = pd.read_csv("uber.csv")

#check the first 5 rows

df.head()


# In[6]:


#drop the unnecessary columns

df = df.drop(columns=(['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']))


# In[7]:


df.head()


# In[9]:


df.describe()[['fare_amount', 'passenger_count']]


# In[11]:


#create a histogram

fig = px.histogram(df, x='fare_amount')

fig.show()


# In[12]:


#create a box plot

fig = px.box(df, y='fare_amount')

fig.show()


# In[14]:


fig = px.scatter(x=df['passenger_count'], y=df['fare_amount'])

fig.show()


# In[15]:


#create a function to find outliers using IQR

def find_outliers_IQR(df):

   q1=df.quantile(0.25)

   q3=df.quantile(0.75)

   IQR=q3-q1

   outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]

   return outliers


# In[20]:


outliers = find_outliers_IQR(df['fare_amount'])

print('number of outliers: '+ str(len(outliers)))

print('max outlier value: '+ str(outliers.max()))

print('min outlier value: '+ str(outliers.min()))


# In[21]:


outliers


# In[23]:


outliers = find_outliers_IQR(df[['passenger_count','fare_amount']])


# In[24]:


outliers


# In[28]:


from scipy import stats
import numpy as np
z = np.abs(stats.zscore(df['fare_amount']))
print(z)


# In[30]:


threshold = 3
print(np.where(z > threshold)) #row number


# In[31]:
