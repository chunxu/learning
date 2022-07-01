
# Welcome to the code notebook for Recommender Systems with Python. In this lecture we will develop basic recommendation systems using Python and pandas. There is another notebook: *Advanced Recommender Systems with Python*. That notebook goes into more detail with the same data set.
# 
# In this notebook, we will focus on providing a basic recommendation system by suggesting items that are most similar to a particular item, in this case, movies. Keep in mind, this is not a true robust recommendation system, to describe it more accurately,it just tells you what movies/items are most similar to your movie choice.
# 


import numpy as np
import pandas as pd

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep='\t', names=column_names)

movie_titles = pd.read_csv("Movie_Id_Titles")

df = pd.merge(df,movie_titles,on='item_id')
df.head()

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
get_ipython().run_line_magic('matplotlib', 'inline')



df.groupby('title')['rating'].mean().sort_values(ascending=False).head()

df.groupby('title')['rating'].count().sort_values(ascending=False).head()

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()

ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()

plt.figure(figsize=(10,4))
ratings['num of ratings'].hist(bins=70)


plt.figure(figsize=(10,4))
ratings['rating'].hist(bins=70)

sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)

# ## Recommending Similar Movies

moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()

ratings.sort_values('num of ratings',ascending=False).head(10)

starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
starwars_user_ratings.head()


# We can then use corrwith() method to get correlations between two pandas series:

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)

corr_starwars = pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()

# Now if we sort the dataframe by correlation, we should get the most similar movies, however note that we get some results that don't really make sense. This is because there are a lot of movies only watched once by users who also watched star wars (it was the most popular movie). 

corr_starwars.sort_values('Correlation',ascending=False).head(10)

corr_liarliar.sort_values('Correlation',ascending=False).head(10)


# Let's fix this by filtering out movies that have less than 100 reviews (this value was chosen based off the histogram from earlier).

corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()

corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()

corr_liarliar = pd.DataFrame(similar_to_liarliar,columns=['Correlation'])
corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['num of ratings'])
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation',ascending=False).head()
