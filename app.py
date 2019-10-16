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

########### Set up the layout
app.layout = html.Div(children=[
    html.H1('Nats gonna win'),
    html.Div([
    html.H6('Stop Open'),
            dcc.Slider(
                id ='slider1',
                min=1,
                max=8,
                step=0.1,
                marks= {1:str(i) for i in range(1,9)},
                value=5,
                ),
    html.H6('Stock Close'),
            dcc.Slider(
            id ='slider2',
            min=1,
            max=8,
            step=0.1,
            marks= {1:str(i) for i in range(1,9)},
            value=5,
    ),
    html.Br(),
    html.H6('# of neighbors'),
    dcc.Dropdown(
        id= 'k-drop',
        options =[{'label':'AAPL', 'value':5},
                 {'label': 'F', 'value':10},
                 {'label': 'AMD', 'value': 15},
                 {'label': 'BAC', 'value': 20},
                 {'label': 'GE', 'value': 20}
        ],
        #options =[{'label': i, 'value': 1} for i in [5,10,15,20,25]],
        value=5
    )
    ]),
    html.Div(id='output-message'),
    html.Br(),
    html.A('Code on Github', href='https://github.com/austinlasseter/knn_iris_plotly'),
])

### Callbacks
@app.callback(Output('output-message', 'children'),
                [Input('k-drop', 'value'),
                Input('slider1', 'value'),
                Input('slider2', 'value')
                ])
def my_flunky_function(k, value0, value1):
    file = open(f'resources/_model{}.pkl', 'rb')
    model= pickle.load(file)
    file.close()
    # define the new observation from the chosen values
    new_obs =[[value0, value1]]
    my_prediction = model.predict(new_obs)
    #return (f' you chose {k} and {value0} and {value1}')
    return f' you chose {} and the predicted species number is:{my_prediction}'



############ Execute the app
if __name__ == '__main__':
    app.run_server(debug=True)# automatically reload
