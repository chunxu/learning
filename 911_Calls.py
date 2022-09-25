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

# ** Import numpy and pandas **

import numpy as np
import pandas as pd


# ** Import visualization libraries and set %matplotlib inline. **


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ** Read in the csv file as a dataframe called df **


df = pd.read_csv("911.csv")


# ** Check the info() of the df **


df.info()


# ** Check the head of df **


df.head(3)


# ## Basic Questions
# ** What are the top 5 zipcodes for 911 calls? **
df['zip'].value_counts().head(5)


# ** What are the top 5 townships (twp) for 911 calls? **
df['twp'].value_counts().head(5)


# ** Take a look at the 'title' column, how many unique title codes are there? **
len(df['title'].unique())


# ## Creating new features

# ** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.** 
# 
# **For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. **

df['Reason'] = df['title'].apply(lambda x : x.split(':')[0])

df['Reason'].value_counts()


# ** What is the most common Reason for a 911 call based off of this new column? **


sns.countplot(df['Reason'])


# ** Now use seaborn to create a countplot of 911 calls by Reason. **
sns.countplot(x= 'Reason', data = df)

# ** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **

type(df['timeStamp'][0])


# ** You should have seen that these timestamps are still strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) to convert the column from strings to DateTime objects. **

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

df['timeStamp'][0].dayofweek


# ** You can now grab specific attributes from a Datetime object by calling them. For example:**
# 
#     time = df['timeStamp'].iloc[0]
#     time.hour
# 
# **You can use Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.**

df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)

df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of week'] = df['timeStamp'].apply(lambda x: x.dayofweek)


# ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **
# 
#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


df['Day of week'] = df['Day of week'].map({0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'})


# ** Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **

sns.countplot(x = 'Day of week', data = df, hue = 'Reason')
plt.legend(loc = 2)

# **Now do the same for Month:**

sns.countplot(x = 'Month', data = df, hue = 'Reason')
plt.legend(loc = 1)


# **Did you notice something strange about the Plot?**

# ** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **

# ** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **

byMonth = df.groupby('Month').count()

byMonth.head()

# ** Now create a simple plot off of the dataframe indicating the count of calls per month. **

byMonth['lat'].plot()


# ** Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. **

sns.lmplot(x= 'Month', y = 'twp', data = byMonth.reset_index())


# **Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. ** 

df['Date'] = df['timeStamp'].apply(lambda x: x.date())

# ** Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

byDate = df.groupby(df['Date']).count()


byDate['lat'].plot()
plt.tight_layout()


# ** Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call**

df[df['Reason'] == 'Traffic'].groupby('Date').count()['lat'].plot()
#plt.title('traffic')
plt.tight_layout()


df[df['Reason'] == 'Fire'].groupby('Date').count()['lat'].plot()
#plt.title('traffic')
plt.tight_layout()


df[df['Reason'] == 'EMS'].groupby('Date').count()['lat'].plot()
#plt.title('traffic')
plt.tight_layout()

# ** Now let's move on to creating  heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an [unstack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) method. Reference the solutions if you get stuck on this!**


df.groupby(['Day of week','Hour']).count().unstack()['lat']


# ** Now create a HeatMap using this new DataFrame. **
sns.heatmap(df.groupby(['Day of week','Hour']).count().unstack()['lat'], cmap='viridis')


# ** Now create a clustermap using this DataFrame. **
sns.clustermap(df.groupby(['Day of week','Hour']).count().unstack()['lat'], cmap='viridis')


# ** Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **
sns.heatmap(df.groupby(['Day of week','Month']).count().unstack()['lat'], cmap='viridis')
sns.clustermap(df.groupby(['Day of week','Month']).count().unstack()['lat'], cmap='viridis')
