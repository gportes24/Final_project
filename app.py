import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from datetime import datetime
import pandas as pd
import numpy as np
import pickle

app = dash.Dash()

app.layout = html.Div([
    html.Label ("Pick a stock ticker"),
    dcc.Dropdown(
        id = 'first-dropdown',
        options = [
            {'label': 'Apple', 'value': 'AAPL'},
            {'label': 'Ford', 'value': 'F'},
            {'label': 'Advanced Micro Device', 'value': 'AMD'},
            {'label': 'Apple', 'value': 'BAC'}
        ],
        value = 'AAPL'
    )
])

# tickers = pd.read_csv('tickers.csv')
# tickers.set_index('Ticker', inplace=True)
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app=dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.run_server
# app.title ='knn'
#
# #### read in the model and the dataset
# training =pd.read_pickle('resources/BAC_fitted_scaler.pkl')
# filename = open('resources/BACstock_model.pkl', 'rb')
# model=pickle.load(filename)
# filename. close()
#
#
# ####set up the layout
#
# app.layout = html.Div([
#     html.H1('This is my stock model'),
#     dcc.Slider(
#     id='slider-no-1',
#     min=1,
#     max=10,
#     marks= {i:str(i) for i in range (1,10)},
#     step = 0.5,
#     value =5
#     ),
#     dcc.Slider(
#     id='slider-no-2',
#     min=1,
#     max=10,
#     marks= {i:str(i) for i in range (1,11)},
#     ),
#     html.Br(),
#     html.H6(id='my-output-message-here', children='')
# ])
#
# ##### add a Callbacks
# @app.callback(Output('my-output-message-here', 'children'),
#             [Input('slider-no-1', 'value'),
#              Input('slider-no-2', 'value')]
# )
# def make_prediction(input0, input1):
#     new_observation = [[input0, input1]]
#     prediction = model.predict(new_observation)
#     specieslist=['High', 'Low', 'Open']
#     return f'The predicted species of your input is {specieslist[prediction[0]]}'
#     #return f'my choices are{input} and {input1}'
# ###### deploy my happen
if __name__ == '__main__':
    app.run_server(debug=True)
