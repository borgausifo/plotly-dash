import plotly.offline as pyo
import plotly.graph_objs as go

y = [1, 14, 14, 15, 17, 18, 18, 18, 18, 20, 20, 23, 25, 29, 43]

# data = [go.Box(y=y, boxpoints='all', jitter=0.3, pointpos=2.0)]

data = [go.Box(y=y, boxpoints='outliers')]

pyo.plot(data)



