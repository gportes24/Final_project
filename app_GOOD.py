import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://raw.githubusercontent.com/gportes24/Final_project/master/top5.csv')


app.layout = html.Div([
    dcc.Graph(
        id='volume',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['ticker'] == i]['High'],
                    y=df[df['ticker'] == i]['Volume'],
                    text=df[df['ticker'] == i]['Date'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.ticker.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'High'},
                yaxis={'title': 'Volume'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
