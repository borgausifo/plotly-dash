import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pandas_datareader.data as web
import os
from dash.dependencies import Input, Output, State
from datetime import datetime

app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker'),
    html.Div([html.H3('Enter a stock symbol:', style={'paddingRight': '30px'}),
              dcc.Input(id='my_stock_picker',
                        value='TSLA',
                        style={'fontSize': 24, 'width': 75})],
             style={'display': 'inline-block', 'verticalAllign': 'top'}),
    html.Div([html.H3('Start and End Date Selection:'),
              dcc.DatePickerRange(id='date_picker',
                                  min_date_allowed=datetime(2015, 1, 1),
                                  max_date_allowed=datetime.today(),
                                  start_date=datetime(2018, 1, 1),
                                  end_date=datetime.today())
              ], style={'display': 'inline-block'}),
    dcc.Graph(id='my-graph',
              figure={'data': [
                  {'x': [1, 2], 'y': [3, 1]}],
                  'layout': {'title': {'text': 'Default'},
                            'margin': dict(l=20, r=20, t=300, b=20),
                            'showlegend': True}})
])

os.environ["IEX_API_KEY"] = "pk_8d4879f676fe4974b8748a1fc7ae8763"


# start = datetime(2016, 9, 1)
# end = datetime(2018, 9, 1)
# f = web.DataReader('F', 'iex', start, end)
# print(f.loc['2018-08-31'])


@app.callback(Output('my-graph', 'figure'),
              [Input('my_stock_picker', 'value'),
               Input('date_picker', 'start_date'),
               Input('date_picker', 'end_date')])
def update_graph(stock_ticker, start_date, end_date):
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    df = web.DataReader(stock_ticker, 'iex', start, end)
    print(df.head())
    fig = {'data': [{'x': df.index, 'y': df['close']}], 'title': stock_ticker}
    return fig


if __name__ == '__main__':
    app.run_server()
