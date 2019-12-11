import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mpg.csv')

data = [go.Scatter(x=df['horsepower'], y=df['mpg'],
                   text = df['mpg'],
                   mode='markers',
                   marker=dict(size=2*df['cylinders'],
                               color=df['weight'],
                               showscale=True))]


layout = go.Layout(title='Bubble Chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)