import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()

app.layout = html.Div(['Outhermost Div!',
                       html.Div(['This is inner Div'],
                                style={'color': 'red'}),
                       html.Div(['Another Div!'],
                                style={'color': 'black', 'border': '3px black solid'})],
                      style={'color': 'green', 'border': '2px green solid'})

if __name__ == '__main__':
    app.run_server()
