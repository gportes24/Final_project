import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle

########### Initiate the app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
df = pd.read_csv(
    'https://raw.githubusercontent.com/gportes24/Final_project/master/top5.csv')
server = app.server
app.title='Stock prices'
colors = {
    'background': '#111111',
    'text': '#3183DC'
}
########### Set up the layout

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
#app.layout = html.Div(children=[
    html.H1(
        children = 'Stock Closing Prices',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
    html.H6('LOW'),
            dcc.Slider(
                id ='slider1',
                min=-2,
                max=4,
                step=0.5,
                marks= {1:str(i) for i in range(1,7)},
                value=2,
                ),
    html.H6('HIGH'),
            dcc.Slider(
                id ='slider2',
                min=-2,
                max=4,
                step=0.5,
                marks= {1:str(i) for i in range(1,7)},
                value=2,
                ),
    html.H6('OPEN'),
            dcc.Slider(
                id ='slider3',
                min=-2,
                max=4,
                step=0.5,
                marks= {1:str(i) for i in range(1,7)},
                value=2,
                ),
    html.H6('SMA_5'),
            dcc.Slider(
                id ='slider4',
                min=-2,
                max=4,
                step=0.5,
                marks= {1:str(i) for i in range(1,7)},
                value=2,
                ),
    html.H6('Volume'),
            dcc.Slider(
                id ='slider5',
                min=-2,
                max=4,
                step=0.5,
                marks= {1:str(i) for i in range(1,7)},
                value=2,
                ),
    html.H6('Daily Change'),
            dcc.Slider(
            id ='slider6',
            min=-2,
            max=4,
            step=0.5,
            marks= {1:str(i) for i in range(1,7)},
            value=2,
    ),
    html.Br(),
    #html.H6('STOCK MARKET TICKERS'),
    html.H6(
    children = 'STOCK MARKET TICKERS',
    style={
        'textAlign': 'center',
        'color': colors['text']
    }
    ),
    dcc.Dropdown(
        id= 'k-drop',
        options =[{'label':'Apple', 'value':'AAPL'},
                 {'label': 'Ford', 'value':'F'},
                 {'label': 'Advanced Micro Devices', 'value': 'AMD'},
                 {'label': 'Bank of America', 'value': 'BAC'},
                 {'label': 'GE', 'value': 'GE'}
        ],
        #options =[{'label': i, 'value': 1} for i in [5,10,15,20,25]],
        value='AAPL',
        ),
        html.Div(id='output-message'),
        html.Br(),

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
    ]),
    # html.Div(id='output-message'),
    # html.Br(),


    html.A('Code on Github', href='https://github.com/gportes24/Final_project'),
])


### Callbacks
@app.callback(Output('output-message', 'children'),
                [Input('k-drop', 'value'),
                Input('slider1', 'value'),
                Input('slider2', 'value'),
                Input('slider3', 'value'),
                Input('slider4', 'value'),
                Input('slider5', 'value'),
                Input('slider6', 'value')
                ])
def my_flunky_function(k, value1, value2, value3, value4, value5, value6):
    file = open(f'Resources/{k}_final_model.pkl', 'rb')
    model= pickle.load(file)
    file.close()
    # define the new observation from the chosen values
    new_obs =[[value1, value2, value3, value4, value5, value6]]
    my_prediction = model.predict(new_obs)
    return f' you chose {k} and the predicted closing price is ${round(my_prediction[0],2)}'


############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)# automatically reload
