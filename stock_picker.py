import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pandas_datareader.data as web
import os
from dash.dependencies import Input, Output
from datetime import datetime

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(id='my_stock_picker', value='TSLA'),
    dcc.Graph(id='my-graph',
              figure={'data': [
        {'x': [1, 2], 'y': [3, 1]}
    ], 'layout': {'title': {'text': 'Default'},
                  'margin': dict(l=20, r=20, t=300, b=20),
                  'showlegend': True}})
])

os.environ["IEX_API_KEY"] = "pk_8d4879f676fe4974b8748a1fc7ae8763"


# start = datetime(2016, 9, 1)
# end = datetime(2018, 9, 1)
# f = web.DataReader('F', 'iex', start, end)
# print(f.loc['2018-08-31'])


@app.callback(Output('my-graph', 'figure'),
              [Input('my_stock_picker', 'value')])
def update_graph(stock_ticker):
    start = datetime(2017, 1, 1)
    end = datetime(2017, 12, 31)
    df = web.DataReader(stock_ticker, 'iex', start, end)
    print(df.head())
    fig = {'data': [{'x': df.index, 'y': df['close']}], 'title': stock_ticker}
    return fig


if __name__ == '__main__':
    app.run_server()
