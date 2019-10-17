import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle

########### Initiate the app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.title='Stock prices'
colors = {
    'background': '#111111',
    'text': '#566573'
}
########### Set up the layout

#app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
app.layout = html.Div(children=[
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
                min=0,
                max=10,
                step=0.1,
                marks= {1:str(i) for i in range(1,11)},
                value=4,
                ),
    html.H6('HIGH'),
            dcc.Slider(
                id ='slider2',
                min=0,
                max=4,
                step=0.1,
                marks= {1:str(i) for i in range(1,4)},
                value=4,
                ),
    html.H6('OPEN'),
            dcc.Slider(
                id ='slider3',
                min=0,
                max=4,
                step=0.1,
                marks= {1:str(i) for i in range(1,4)},
                value=4,
                ),
    html.H6('SMA_5'),
            dcc.Slider(
                id ='slider4',
                min=0,
                max=4,
                step=0.1,
                marks= {1:str(i) for i in range(1,4)},
                value=4,
                ),
    html.H6('Volume'),
            dcc.Slider(
                id ='slider5',
                min=0,
                max=4,
                step=0.1,
                marks= {1:str(i) for i in range(1,4)},
                value=4,
                ),
    html.H6('Daily Change'),
            dcc.Slider(
            id ='slider6',
            min=0,
            max=4,
            step=0.1,
            marks= {1:str(i) for i in range(1,20)},
            value=4,
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
        options =[{'label':'AAPL', 'value':'AAPL'},
                 {'label': 'F', 'value':'F'},
                 {'label': 'AMD', 'value': 'AMD'},
                 {'label': 'BAC', 'value': 'BAC'},
                 {'label': 'GE', 'value': 'GE'}
        ],
        #options =[{'label': i, 'value': 1} for i in [5,10,15,20,25]],
        value='AAPL'
    )
    ]),
    html.Div(id='output-message'),
    html.Br(),

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
    file = open(f'resources/{k}_final_model.pkl', 'rb')
    model= pickle.load(file)
    file.close()
    # define the new observation from the chosen values
    new_obs =[[value1, value2, value3, value4, value5, value6]]
    my_prediction = model.predict(new_obs)
    #return (f' you chose {k} and {value0} and {value1}')
    return f' you chose {k} and the predicted closing price is $:{my_prediction}'




############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)# automatically reload
