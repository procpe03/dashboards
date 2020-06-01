#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:09:04 2020

@author: petrprochazka
"""
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_excel('data_input.xlsx')
df2 = df.copy()
df2['Value'] = df2['Value'] * 2

df8 = df.copy()
df8['Value'] = df8['Value'] * 8

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


fig = px.bar(df, x='City', y='Value')



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    dcc.Input(id='my-id2', value='initial value', type='text'),

    dcc.Checklist( id='my_checklist',
    options=[
        {'label': 'Praha', 'value': 'Praha'},
        {'label': 'Brno', 'value': 'Brno'},
        {'label': 'Ostrava', 'value': 'Ostrava'},
        {'label': 'Moskva', 'value': 'Moskva'},
        {'label': 'Londyn', 'value': 'Londyn'}
    ],
    value=['Praha', 'Brno'],
    labelStyle={'display': 'inline-block'},

),  dcc.RadioItems(id='radio',       
    options=[
        {'label': 'Jedna', 'value': 'jedna'},
        {'label': 'Dve', 'value': 'dve'},
        {'label': 'Osm', 'value': 'osm'}
    ],
    value='jedna',  labelStyle={'display': 'inline-block'}
), 
                   dcc.Checklist( id='countries',
    options=[
        {'label': 'Cesko', 'value': 'CZ'},
        {'label': 'Rusko', 'value': 'RU'},
        {'label': 'Britanie', 'value': 'GB'}
    ],
    value=['CZ'],
    labelStyle={'display': 'inline-block'},

),  html.Div(id='radijko'),
    html.Div(id='mesta'), 
    html.Div(id='my-div'), 
    html.Div(id='mu-div2'),
    html.Div(id='cities'),
    html.Div(id='filtr'),
    dcc.Graph(id='graf_data_framy',
              figure=fig),
    dcc.Graph(id='graf3',
              figure=fig),
    dcc.Graph(id='graf2',
              figure=fig),
    dcc.Graph(id='graf1',
              figure=fig)
])

                   

@app.callback(
    Output(component_id='radijko', component_property='children'),
    [Input(component_id='radio', component_property='value')]
)
def update_output_div44(input_value):
    
    return 'V radiu je prave "{}"'.format(input_value)


@app.callback(
    Output(component_id='graf_data_framy', component_property='figure'),
    [Input(component_id='radio', component_property='value')]
)     
def set_display_children2(selected_radio):
    if selected_radio == 'jedna':
        dfff = df
    elif selected_radio == 'dve':
        dfff = df2
    else:
        dfff = df8
    fig = px.bar(dfff, x='City', y='Value')
    return fig




@app.callback(
    Output(component_id='graf3', component_property='figure'),
    [Input('countries', 'value'),
     Input('my_checklist', 'value')])
def update_graf_2(input_country, input_city):
    dff = df[df['Country'].isin(input_country)].copy()
    fig = px.bar(dff[dff['City'].isin(input_city)], x='City', y='Value')
    
    return fig


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

@app.callback(
    Output(component_id='mu-div2', component_property='children'),
    [Input(component_id='my-id2', component_property='value')]
)
def update_output_div2(input_value):
    return 'You\'ve not entered entered "{}"'.format(input_value)

@app.callback(
    Output(component_id='filtr', component_property='children'),
    [Input(component_id='my_checklist', component_property='value')]
)
def update_output_div4(input_value):
    
    return 'You\'ve not entered entered "{}"'.format(input_value)


@app.callback(
    Output(component_id='graf2', component_property='figure'),
    [Input(component_id='my_checklist', component_property='value')]
)
def update_graf(input_value):
    fig = px.bar(df[df['City'].isin(input_value)], x='City', y='Value')
    
    return fig


@app.callback(
    Output(component_id='cities', component_property='children'),
    [Input(component_id='my_checklist', component_property='value')]
)
def update_output_div3(input_value):
    dff = df[df['City'].isin(input_value)]
    return 'You\'ve not entered entered "{}"'.format(dff['Value'].sum())

if __name__ == '__main__':
    app.run_server(debug=True)
