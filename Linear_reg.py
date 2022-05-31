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

