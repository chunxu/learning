#!/usr/bin/env python
# coding: utf-8

# # 911 Calls Capstone Project

# For this capstone project we will be analyzing some 911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). The data contains the following fields:
# 
# * lat : String variable, Latitude
# * lng: String variable, Longitude
# * desc: String variable, Description of the Emergency Call
# * zip: String variable, Zipcode
# * title: String variable, Title
# * timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# * twp: String variable, Township
# * addr: String variable, Address
# * e: String variable, Dummy variable (always 1)
# 
# Just go along with this notebook and try to complete the instructions or answer the questions in bold using your Python and Data Science skills!

# ## Data and Setup

# ____
# ** Import numpy and pandas **

# In[1]:


import numpy as np
import pandas as pd


# ** Import visualization libraries and set %matplotlib inline. **

# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ** Read in the csv file as a dataframe called df **

# In[4]:


df = pd.read_csv("911.csv")


# ** Check the info() of the df **

# In[6]:


df.info()


# ** Check the head of df **

# In[8]:


df.head(3)


# ## Basic Questions

# ** What are the top 5 zipcodes for 911 calls? **

# In[15]:


df['zip'].value_counts().head(5)


# ** What are the top 5 townships (twp) for 911 calls? **

# In[20]:


df['twp'].value_counts().head(5)


# ** Take a look at the 'title' column, how many unique title codes are there? **

# In[136]:


len(df['title'].unique())


# ## Creating new features

# ** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.** 
# 
# **For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. **

# In[41]:


df['Reason'] = df['title'].apply(lambda x : x.split(':')[0])


# In[45]:


df['Reason'].value_counts()


# ** What is the most common Reason for a 911 call based off of this new column? **

# In[50]:


sns.countplot(df['Reason'])


# ** Now use seaborn to create a countplot of 911 calls by Reason. **

# In[49]:


sns.countplot(x= 'Reason', data = df)


# ___
# ** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **

# In[52]:


type(df['timeStamp'][0])


# ** You should have seen that these timestamps are still strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) to convert the column from strings to DateTime objects. **

# In[56]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[67]:


df['timeStamp'][0].year

