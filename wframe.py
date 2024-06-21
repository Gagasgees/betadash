from dash import Dash, dcc, Output, Input, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

filepath = "../Datasets/hasil_output.csv"

raw_df = pd.read_csv(filepath, parse_dates=["acq_date"])
main_df = raw_df.dropna(subset=["regency_city", "province"])

# Build Components

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
mytitle = html.H2("Pemantauan Titik Api di Indonesia")
description = """ 3 jam."""

dropdown = dcc.Dropdown(options=[{"label": str(year), "value": year} for year in main_df["year"].unique()],
                        value=2021,  # initial value
                        clearable=False)

app.layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                mytitle,
                html.Label("Pilih Tahun"),
                dropdown,
                html.Hr(),
                html.P(description, style={'text-align': 'justify'}),
            ], width=2),
            dbc.Col([
                dbc.Row([
                    dbc.Col(dcc.Graph(figure={}, id="barfig1"), width=10, style={"height": "40%"})
                ]),
                dbc.Row([
                    dbc.Col(dcc.Graph(figure={}, id="barfig2"), width=10, style={"height": "40%"})
                ]),
                dbc.Row([
                    dbc.Col(dcc.Graph(figure={}, id="mapfig"), width=10, style={"height": "50%"})
                ]), 
                dbc.Row([
                    dbc.Col(dcc.Graph(figure={}, id="linefig"), width=10, style={"height": "30%"}),
                    dbc.Col(dcc.Graph(figure={}, id="piefig"), width=4, style={"height": "30%"}) 
                ], style={'display': 'flex', 'flex-direction': 'row'}),
            ], width=3)
        ]),
    ], 
    fluid=True)

# ------ Run App -------

if __name__ == '__main__':
    app.run_server(debug=True, port=1651)