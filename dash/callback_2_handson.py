import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('/Users/borgausifo/Python-Projects/plotly-dash/plotly-basic/data/gapminderDataFiveYear.csv')

app = dash.Dash()

year_options = [{'label': str(year), 'value': year} for year in df['year'].unique()]

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker', options=year_options,
                 value=df['year'].min())
])


@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value')])
def update_figure(selected_year):
    # Data ONLY FOR SELECTED YEAR FROM DROPDOWN
    filtered_df = df[df['year'] == selected_year]

    traces = []
    for continent_name in filtered_df['continent'].unique():
        df_by_continent = filtered_df[filtered_df['continent'] == continent_name]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            mode='markers',
            opacity=0.5,
            marker={'size': 15},
            name=continent_name
        ))

    return {'data': traces,
            'layout': go.Layout(title='Plot',
                                xaxis={'title': 'GDP Per Capita', 'type': 'log'},
                                yaxis={'title': 'Life Expectancy'})}


if __name__ == '__main__':
    app.run_server()
