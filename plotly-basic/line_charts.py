import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)
x_values = np.random.randint(0, 1, 100)
y_values = np.random.randn(100)

print(x_values)
print('-------')
print(y_values)


trace0 = go.Scatter(x=x_values, y=y_values+5,
                    mode='markers', name='markers')
trace1 = go.Scatter(x=x_values, y=y_values,
                    mode='lines', name='mylines')

data = [trace0, trace1]
layout = go.Layout(title='Line Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='box_plot.html')