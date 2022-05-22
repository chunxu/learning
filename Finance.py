#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # Finance Data Project 
# 
# In this data project we will focus on exploratory data analysis of stock prices. Keep in mind, this project is just meant to practice your visualization and pandas skills, it is not meant to be a robust financial analysis or be taken as financial advice.
# ____
# ** NOTE: This project is extremely challenging because it will introduce a lot of new concepts and have you looking things up on your own (we'll point you in the right direction) to try to solve the tasks issued. Feel free to just go through the solutions lecture notebook and video as a "walkthrough" project if you don't want to have to look things up yourself. You'll still learn a lot that way! **
# ____
# We'll focus on bank stocks and see how they progressed throughout the [financial crisis](https://en.wikipedia.org/wiki/Financial_crisis_of_2007%E2%80%9308) all the way to early 2016.

# ## Get the Data
# 
# In this section we will learn how to use pandas to directly read data from Google finance using pandas!
# 
# First we need to start with the proper imports, which we've already laid out for you here.
# 
# *Note: [You'll need to install pandas-datareader for this to work!](https://github.com/pydata/pandas-datareader) Pandas datareader allows you to [read stock information directly from the internet](http://pandas.pydata.org/pandas-docs/stable/remote_data.html) Use these links for install guidance (**pip install pandas-datareader**), or just follow along with the video lecture.*
# 
# ### The Imports
# 
# Already filled out for you.

#pip install pandas-datareader

from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Data
# 
# We need to get data using pandas datareader. We will get stock information for the following banks:
# *  Bank of America
# * CitiGroup
# * Goldman Sachs
# * JPMorgan Chase
# * Morgan Stanley
# * Wells Fargo
# 
# ** Figure out how to get the stock data from Jan 1st 2006 to Jan 1st 2016 for each of these banks. Set each bank to be a separate dataframe, with the variable name for that bank being its ticker symbol. This will involve a few steps:**
# 1. Use datetime to set start and end datetime objects.
# 2. Figure out the ticker symbol for each bank.
# 2. Figure out how to use datareader to grab info on the stock.
# 
# ** Use [this documentation page](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html) for hints and instructions (it should just be a matter of replacing certain values. Use google finance as a source, for example:**
#     
#     # Bank of America
#     BAC = data.DataReader("BAC", 'google', start, end)
# 
# ### WARNING: MAKE SURE TO CHECK THE LINK ABOVE FOR THE LATEST WORKING API. "google" MAY NOT ALWAYS WORK. 
# ------------
# ### We also provide pickle file in the article lecture right before the video lectures.


#df = pd.read_pickle('all_banks')


start = datetime.datetime(2006,1,1)
end = datetime.datetime(2016,1,1)


BAC = data.DataReader('BAC','yahoo', start, end)
C = data.DataReader('C','yahoo', start, end)


# ** Create a list of the ticker symbols (as strings) in alphabetical order. Call this list: tickers**

tickers = ['BAC','C']


# ** Use pd.concat to concatenate the bank dataframes together to a single data frame called bank_stocks. Set the keys argument equal to the tickers list. Also pay attention to what axis you concatenate on.**

bank_stocks = pd.concat([BAC,C], axis=1, keys = tickers)

# ** Set the column name levels (this is filled out for you):**

bank_stocks.columns.names = ['Bank Ticker','Stock Info']


bank_stocks['BAC']['High'][0]


# # EDA
# 
# Let's explore the data a bit! Before continuing, I encourage you to check out the documentation on [Multi-Level Indexing](http://pandas.pydata.org/pandas-docs/stable/advanced.html) and [Using .xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html).
# Reference the solutions if you can not figure out how to use .xs(), since that will be a major part of this project.
# 
# ** What is the max Close price for each bank's stock throughout the time period?**

for name in tickers:
    print(name, bank_stocks[name]['Close'].max())

# ** Create a new empty DataFrame called returns. This dataframe will contain the returns for each bank's stock. returns are typically defined by:**
# 
# $$r_t = \frac{p_t - p_{t-1}}{p_{t-1}} = \frac{p_t}{p_{t-1}} - 1$$

bank_stocks.xs(key = 'Close', axis = 1, level = 'Stock Info').max()


#returns


# ** We can use pandas pct_change() method on the Close column to create a column representing this return value. Create a for loop that goes and for each Bank Stock Ticker creates this returns column and set's it as a column in the returns DataFrame.**

returns = pd.DataFrame()
for name in tickers:
    returns[name+'_return'] = bank_stocks[name]['Close'].pct_change()
    

# ** Create a pairplot using seaborn of the returns dataframe. What stock stands out to you? Can you figure out why?**

import seaborn as sns
sns.pairplot(returns)


# * See solution for details about Citigroup behavior....

# ** Using this returns DataFrame, figure out on what dates each bank stock had the best and worst single day returns. You should notice that 4 of the banks share the same day for the worst drop, did anything significant happen that day?**

returns.idxmin()

returns.idxmax()

returns.std()

returns.loc['2015-01-01':'2015-12-31'].std()

# ** Create a distplot using seaborn of the 2015 returns for Morgan Stanley **

sns.displot(returns['BAC_return'].loc['2015-01-01':'2015-12-31'])

# ** Create a distplot using seaborn of the 2008 returns for CitiGroup **

sns.displot(returns['C_return'].loc['2008-01-01':'2008-12-31'],color='red', bins=50)

    

# # More Visualization
# 
# A lot of this project will focus on visualizations. Feel free to use any of your preferred visualization libraries to try to recreate the described plots below, seaborn, matplotlib, plotly and cufflinks, or just pandas.
# 
# ### Imports

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')

# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()


# ** Create a line plot showing Close price for each bank for the entire index of time. (Hint: Try using a for loop, or use [.xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html) to get a cross section of the data.)**

for name in tickers:
    bank_stocks[name]['Close'].plot(label = name)
plt.legend()

bank_stocks.xs(key = 'Close', axis =1, level = 'Stock Info').plot()

# ## Moving Averages
# 
# Let's analyze the moving averages for these stocks in the year 2008. 
# 
# ** Plot the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008**

BAC['Close'].loc['2008-1-1':'2008-12-31'].rolling(window=30).mean().plot(label = 'rolling')
BAC['Close'].loc['2008-1-1':'2008-12-31'].plot()
plt.legend()

