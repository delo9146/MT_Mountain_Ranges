# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 19:13:34 2022

@author: dlogan
"""

from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('castlePoints.csv')

fig = go.Figure(data=go.Scattergeo(
    lon=df['X'],
    lat=df['Y'],
))

fig.update_layout(
    geo_scope='usa',
    title_text = 'Montana Mountain Ranges'
)

app.layout = html.Div(children=[
    html.H1(children='Identified Geothermal Systems of the Western USA'),
    html.Div(children='''
        This data was provided by the USGS.
    '''),

    dcc.Graph(
        id='example-map',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)