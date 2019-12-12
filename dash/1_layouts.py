import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children=[
    html.H1('Hello Dash!'),
    html.Div('Dash: Web Dashboards with Python'),
    dcc.Graph(id='id1',
              figure={'data': [
                  {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                  {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'}
              ],
                  'layout': {
                  'title': 'Bar Plots'
              }})
])

if __name__ == '__main__':
    app.run_server()

