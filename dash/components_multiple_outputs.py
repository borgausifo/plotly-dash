import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('/Users/borgausifo/Python-Projects/plotly-dash/plotly-basic/data/wheels.csv')

app = dash.Dash()

app_layout = html.Div([
    dcc.RadioItems(id='wheels',
                   options=[{'label': i, 'value': i} for i in df['wheels'].unique()],
                   value=1),
    html.Div(id='wheels-output'),
    html.Hr(),
    dcc.RadioItems(id='colors',
                   options=[{'label': i, 'value': i} for i in df['color'].unique()],
                   value='blue'
                   ),
    html.Div(id='colors-output')
], style={'font': 'helvatica', 'fontSize': 18})


@app.callback(Output('wheels-output', 'children'),
              [Input()])
def callback_a(wheels_value):
    return f'You choose {wheels_value}'


@app.callback(Output(),
              [Input()])
def callback_b(colors_value):
    return f'You choose {colors_value}'


