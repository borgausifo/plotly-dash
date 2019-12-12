import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Creating data

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Creating the layout and plots

app.layout = html.Div([dcc.Graph(id='scatter',
                                 figure={'data': [
                                     go.Scatter(
                                         x=random_x, y=random_y, mode='markers',
                                         marker={'size': 12,
                                                 'color': 'rgb(44, 32, 444)',
                                                 'symbol': 'pentagon',
                                                 'line': {'width': 2}}
                                     )],
                                     'layout': go.Layout(title='Scatter Plot')}
                                 ),
                       dcc.Graph(id='scatter2',
                                 figure={'data': [
                                     go.Scatter(
                                         x=random_x, y=random_y, mode='markers',
                                         marker={'size': 12,
                                                 'color': 'rgb(89, 39, 490)',
                                                 'symbol': 'pentagon',
                                                 'line': {'width': 2}}
                                     )],
                                     'layout': go.Layout(title='Scatter Plot 2')}
                                 )
                       ])
if __name__ == '__main__':
    app.run_server()
