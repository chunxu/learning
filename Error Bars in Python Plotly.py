#Error Bars in Python Plotly 

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

