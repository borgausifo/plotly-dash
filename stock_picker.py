import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(id='my_stock_picker', value='TSLA'),
    dcc.Graph(id='my-graph', figure={'data': [
        {'x': [1, 2], 'y': [3, 1]}
    ], 'layout': {'title': 'Default Title'}}),
html.Div([html.H1('Hello')])
])


@app.callback(Output('my-graph', 'figure'),
              [Input('my_stock_picker', 'value')])
def update_graph(stock_ticker):
    fig = {'data': [{'x': [1, 2], 'y': [3, 1]}], 'title': stock_ticker}
    return fig


if __name__ == '__main__':
    app.run_server()
