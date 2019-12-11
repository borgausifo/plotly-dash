import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2

hist_data = [x1, x2, x3]
group_labels = ['X1', 'X2', 'X3']

fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels)
pyo.plot(fig)
