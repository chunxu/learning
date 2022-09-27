#!/usr/bin/env python
# coding: utf-8

#pip install plotly
#pip install cufflinks

import pandas as pd
import numpy as np
import cufflinks as cf
from plotly import __version__


print (__version__)

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot



init_notebook_mode(connected=True) #connect with javascript

cf.go_offline()

# generate some data to play with
df = pd.DataFrame(np.random.randn(100,4), columns="A B C D".split())

df2 = pd.DataFrame({'Category':['A', 'B', 'C'], 'Values':[12,34,56]})


df.head()


df2.head()

get_ipython().run_line_magic('matplotlib', 'inline')


df.plot()



df.iplot()


df.iplot(kind='scatter', x = 'A', y = 'B', mode = 'markers', size = 12, color = 'blue')


df2.iplot(kind='bar', x = 'Category', y = 'Values')


df.mean().iplot(kind = 'bar')


df.iplot(kind = 'box')


df3 = pd.DataFrame({'x':[1,2,3,4,5], 'y':[10,20,30,20,10], 'z':[5,4,3,2,1]})


df3



df3.iplot(kind = 'surface',colorscale = 'rdylbu')

df.iplot(kind = 'hist', bins = 20)


df.iplot(kind= 'spread')

df.scatter_matrix()
# geographic plot
import plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot


#import plotly.plotly as py


#pip install chart-studio
import chart_studio.plotly as py


init_notebook_mode(connected=True)

data = dict(type = 'choropleth',
           locations = ['AZ','CA','NY'],
           locationmode = 'USA-states',
           colorscale = 'Portland',
           text = ['text 1', 'text 2', 'text 3'],
           z = [1,2,3],
           colorbar = {'title':'colorbar title here'})
layout = dict(geo ={'scope':'usa'})

import plotly.graph_objects as go

choromap = go.Figure(data = [data], layout = layout)

iplot(choromap)


df4 = pd.read_csv('09-Geographical-Plotting/2011_US_AGRI_Exports')



df4.head()

data = dict(type = 'choropleth',
           locations = df4['code'],
           locationmode = 'USA-states',
           colorscale = 'Portland',
           text = df4['text'],
           z = df4['total exports'],
           marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
           colorbar = {'title':'Millions USD'}
           )


layout = dict(title = '2011 US Agricultural Exports by States',
              geo =dict(scope='usa',showlakes= True, lakecolor = 'rgb(85,173,240)'))


layout


choromap2 = go.Figure(data = [data], layout = layout)


iplot(choromap2)

#part 2 international
df = pd.read_csv("09-Geographical-Plotting/2014_World_GDP")


df.head()

data = dict(type = 'choropleth',
           locations = df['CODE'],
           text = df['COUNTRY'],
           z = df['GDP (BILLIONS)'],
           colorbar = {'title':'GDP in Billions USD'}
           )

layout = dict(title = '2014 Global GDP',
              geo =dict(showframe= False,projection = {'type':'kavrayskiy7'}))

choromap3 = go.Figure(data = [data], layout = layout) # err due to layout.geo.projection Received value: 'Mercator'


iplot(choromap3)





