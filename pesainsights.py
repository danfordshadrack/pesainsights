import pandas as pd #(version 0.24.2)
import datetime as dt
import dash         #(version 1.0.0)
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output

import plotly       #(version 4.4.1)
import plotly.express as px







external_stylesheets = ['dbc.themes.BOOTSTRAP']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server


df = pd.read_csv("tarrifs.csv")

trace1 = go.Bar(x=df[('Kiasi')], y=df['Kutuma Vodacom'], name='Kutuma Kwenda Vodacom')
trace2 = go.Bar(x=df['Kiasi'], y=df['Vodacom Mingine '], name='Kwenda Mitandao Mingine')
trace3 = go.Bar(x=df['Kiasi'], y=df['Kutoa Vodacom'], name='Kutoa Kwa wakala/ATM')
trace4 = go.Bar(x=df[('Kiasi')], y=df['Kutuma Tigo'], name='Kutuma Kwenda Tigo')
trace5 = go.Bar(x=df['Kiasi'], y=df['Tigo Mingine'], name='Kutoka Tigo Kwenda Mitandao Mingine')
trace6 = go.Bar(x=df['Kiasi'], y=df['Kutoa Tigo'], name='Kutoa Kwa wakala/ATM Tigo')
trace7 = go.Bar(x=df[('Kiasi')], y=df['Kutuma Airtel'], name='Kutuma Kwenda Airtel')
trace8 = go.Bar(x=df['Kiasi'], y=df['Airtel Mingine'], name='Kutoka Airtel Kwenda Mitandao Mingine')
trace9 = go.Bar(x=df['Kiasi'], y=df['Kutoa Airtel'], name='Kutoa Kwa wakala/ATM Airtel')
trace10 = go.Bar(x=df[('Kiasi')], y=df['Kutuma Halotel'], name='Kutuma Kwenda Halotel')
trace11 = go.Bar(x=df['Kiasi'], y=df['Halotel Mingine'], name='Kutoka Halotel Kwenda Mitandao Mingine')
trace12 = go.Bar(x=df['Kiasi'], y=df['Kutoa Halotel'], name='Kutoa Kwa wakala/ATM Tigo')
trace13 = go.Bar(x=df[('Kiasi')], y=df['Kutuma TTCL'], name='Kutuma Kwenda TTCL')
trace14 = go.Bar(x=df['Kiasi'], y=df['TTCL Mingine'], name='Kutoka TTCL Kwenda Mitandao Mingine')
trace15 = go.Bar(x=df['Kiasi'], y=df['Kutoa TTCL'], name='Kutoa Kwa wakala/ATM TTCL')
trace16 = go.Bar(x=df[('Kiasi')], y=df['Kutuma Ezy'], name='Kutuma Kwenda Ezy')
trace17 = go.Bar(x=df['Kiasi'], y=df['Ezy Mingine'], name='Kutoka Ezy Kwenda Mitandao Mingine')
trace18 = go.Bar(x=df['Kiasi'], y=df['Kutoa Ezy'], name='Kutoa Kwa wakala/ATM Ezy')




app.layout = html.Div(children=[
    nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Active", active=True, href="#")),
        dbc.NavItem(dbc.NavLink("A link", href="#")),
        dbc.NavItem(dbc.NavLink("Another link", href="#")),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("Item 1"), dbc.DropdownMenuItem("Item 2")],
            label="Dropdown",
            nav=True,
        ),
    ]
),
    html.H2(children="PESA INSIGHT",
    style={
        'textAlign': 'center',
    }),

    html.Div(children= '''
        PesaInsight: Inform your financial decision.
    ''',
    style={
        'textAlign': 'center',
    }),



    dcc.Graph(
        id='tarrifs',
        figure={
            'data': [trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8,trace9,trace10,trace11,trace12,trace13,trace14,trace15,trace16,trace17,trace18],
            'layout': 
            go.Layout(title='Makato kwa Tsh', barmode='group', yaxis_title="Gharama Tsh",xaxis_title="Kiasi Cha Muamala", height=400)
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
