#Error Bars in Python Plotly  - a third party library

'''
Plotly Express is the easy-to-use, high-level interface to Plotly, which operates on a variety of types of data and produces easy-to-style figures. For functions representing 2D data points such as px.scatter, px.line, px.bar etc., error bars are given as a column name which is the value of the error_x (for the error on x position) and error_y (for the error on y position).
'''

import plotly.express as px
df = px.data.iris()
df["e"] = df["sepal_width"]/100
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 error_x="e", error_y="e")
fig.show()

#Asymmetric Error Bars with Plotly Express
import plotly.express as px
df = px.data.iris()
df["e_plus"] = df["sepal_width"]/100
df["e_minus"] = df["sepal_width"]/40
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 error_y="e_plus", error_y_minus="e_minus")
fig.show()

#Error Bars with graph_objects
#Basic Symmetric Error Bars

import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
        x=[0, 1, 2],
        y=[6, 10, 2],
        error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=[1, 2, 3],
            visible=True)
    ))
fig.show()

#Asymmetric Error Bars
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
        x=[1, 2, 3, 4],
        y=[2, 1, 3, 4],
        error_y=dict(
            type='data',
            symmetric=False,
            array=[0.1, 0.2, 0.1, 0.1],
            arrayminus=[0.2, 0.4, 1, 0.2])
        ))
fig.show()

#Error Bars as a Percentage of the y Value
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
        x=[0, 1, 2],
        y=[6, 10, 2],
        error_y=dict(
            type='percent', # value of error bar given as percentage of y value
            value=50,
            visible=True)
    ))
fig.show()


#Asymmetric Error Bars with a Constant Offset
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
        x=[1, 2, 3, 4],
        y=[2, 1, 3, 4],
        error_y=dict(
            type='percent',
            symmetric=False,
            value=15,
            valueminus=25)
    ))
fig.show()

#Horizontal Error Bars
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
        x=[1, 2, 3, 4],
        y=[2, 1, 3, 4],
        error_x=dict(
            type='percent',
            value=10)
    ))
fig.show()


#Bar Chart with Error Bars
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(
    name='Control',
    x=['Trial 1', 'Trial 2', 'Trial 3'], y=[3, 6, 4],
    error_y=dict(type='data', array=[1, 0.5, 1.5])
))
fig.add_trace(go.Bar(
    name='Experimental',
    x=['Trial 1', 'Trial 2', 'Trial 3'], y=[4, 7, 3],
    error_y=dict(type='data', array=[0.5, 1, 2])
))
fig.update_layout(barmode='group')
fig.show()


#Colored and Styled Error Bars
import plotly.graph_objects as go
import numpy as np

x_theo = np.linspace(-4, 4, 100)
sincx = np.sinc(x_theo)
x = [-3.8, -3.03, -1.91, -1.46, -0.89, -0.24, -0.0, 0.41, 0.89, 1.01, 1.91, 2.28, 2.79, 3.56]
y = [-0.02, 0.04, -0.01, -0.27, 0.36, 0.75, 1.03, 0.65, 0.28, 0.02, -0.11, 0.16, 0.04, -0.15]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x_theo, y=sincx,
    name='sinc(x)'
))
fig.add_trace(go.Scatter(
    x=x, y=y,
    mode='markers',
    name='measured',
    error_y=dict(
        type='constant',
        value=0.1,
        color='purple',
        thickness=1.5,
        width=3,
    ),
    error_x=dict(
        type='constant',
        value=0.2,
        color='purple',
        thickness=1.5,
        width=3,
    ),
    marker=dict(color='purple', size=8)
))
fig.show()


