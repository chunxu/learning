#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install plotly
#pip install cufflinks


# In[2]:


import pandas as pd
import numpy as np
import cufflinks as cf
from plotly import __version__


# In[3]:


print (__version__)


# In[4]:


from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[5]:


init_notebook_mode(connected=True) #connect with javascript


# In[6]:


cf.go_offline()


# In[7]:


# generate some data to play with
df = pd.DataFrame(np.random.randn(100,4), columns="A B C D".split())


# In[8]:


df2 = pd.DataFrame({'Category':['A', 'B', 'C'], 'Values':[12,34,56]})


# In[9]:


df.head()


# In[10]:


df2.head()


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


df.plot()


# In[13]:


df.iplot()


# In[14]:


df.iplot(kind='scatter', x = 'A', y = 'B', mode = 'markers', size = 12, color = 'blue')


# In[15]:


df2.iplot(kind='bar', x = 'Category', y = 'Values')


# In[16]:


df.mean().iplot(kind = 'bar')


# In[17]:


df.iplot(kind = 'box')


# In[18]:


df3 = pd.DataFrame({'x':[1,2,3,4,5], 'y':[10,20,30,20,10], 'z':[5,4,3,2,1]})


# In[19]:


df3


# In[20]:


df3.iplot(kind = 'surface',colorscale = 'rdylbu')


# In[21]:


df.iplot(kind = 'hist', bins = 20)


# In[22]:


df.iplot(kind= 'spread')


# In[23]:


df.scatter_matrix()


# In[24]:


# geographic plot
import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot


# In[25]:


#import plotly.plotly as py


# In[26]:


#pip install chart-studio
import chart_studio.plotly as py


# In[27]:


init_notebook_mode(connected=True)


# In[28]:


data = dict(type = 'choropleth',
           locations = ['AZ','CA','NY'],
           locationmode = 'USA-states',
           colorscale = 'Portland',
           text = ['text 1', 'text 2', 'text 3'],
           z = [1,2,3],
           colorbar = {'title':'colorbar title here'})


# In[29]:


layout = dict(geo ={'scope':'usa'})


# In[30]:


import plotly.graph_objects as go


# In[31]:


choromap = go.Figure(data = [data], layout = layout)


# In[32]:


iplot(choromap)


# In[33]:


df4 = pd.read_csv('09-Geographical-Plotting/2011_US_AGRI_Exports')


# In[34]:


df4.head()


# In[35]:


data = dict(type = 'choropleth',
           locations = df4['code'],
           locationmode = 'USA-states',
           colorscale = 'Portland',
           text = df4['text'],
           z = df4['total exports'],
           marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
           colorbar = {'title':'Millions USD'}
           )


# In[36]:


layout = dict(title = '2011 US Agricultural Exports by States',
              geo =dict(scope='usa',showlakes= True, lakecolor = 'rgb(85,173,240)'))


# In[37]:


layout


# In[38]:


choromap2 = go.Figure(data = [data], layout = layout)


# In[39]:


iplot(choromap2)


# In[40]:


#part 2 international
df = pd.read_csv("09-Geographical-Plotting/2014_World_GDP")


# In[41]:


df.head()


# In[42]:


data = dict(type = 'choropleth',
           locations = df['CODE'],
           text = df['COUNTRY'],
           z = df['GDP (BILLIONS)'],
           colorbar = {'title':'GDP in Billions USD'}
           )


# In[50]:


layout = dict(title = '2014 Global GDP',
              geo =dict(showframe= False,projection = {'type':'kavrayskiy7'}))


# In[51]:


choromap3 = go.Figure(data = [data], layout = layout) # err due to layout.geo.projection Received value: 'Mercator'


# In[52]:


iplot(choromap3)


# In[ ]:




