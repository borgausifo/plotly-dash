import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(options=[{'label': 'New York City',
                           'value': 'NYC'},
                          {'label': 'Turkey',
                           'value': 'TRY'}],
                 value='NYC'),
    html.P(html.Label('Slider')),
    dcc.Slider(min=-9, max=10, step=1, value=0, marks={i: i for i in range(-9, 10)}),
    html.P(html.Label('Radio Items')),
    dcc.RadioItems(options=[{'label': 'New York City',
                             'value': 'NYC'},
                            {'label': 'Turkey',
                             'value': 'TRY'}],
                   value='NYC')
])

if __name__ == '__main__':
    app.run_server()
