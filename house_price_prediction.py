#oringinally drafted in jupter notebook
import numpy as np
import pandas as pd
#pip install plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.datasets import load_boston
load_boston = load_boston()
x = load_boston.data
y = load_boston.target

data = pd.DataFrame(x, columns = load_boston.feature_names)
data['SalePrice'] = y
data.head()
