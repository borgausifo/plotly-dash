import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

df = pd.read_csv('data/mocksurvey.csv', index_col=0)

data = [go.Bar(x=df.index, y=df[response], name=response) for response in df.columns]

layout = go.Layout(title='Survey', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)

