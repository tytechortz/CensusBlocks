from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
import json
import random
from figures_utilities import (
    get_figure
)

from utils import (
    get_tract_data,
    # get_block_data,
    # get_block_group_data,
    # get_block_group_geo_data,
    # get_tract_geo_data,
    # get_block_geo_data
)

app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

header = html.Div("Census Blocks", className="h2 p-2 text-white bg-primary text-center")

bgcolor = "#f3f3f1"  # mapbox light map land color

template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

tract_geo_data = get_tract_data()
# bg_geo_data = get_block_group_geo_data()
# block_geo_data = get_block_geo_data()
all_tracts = tract_geo_data["GEOID"].values


def blank_fig(height):
    """
    Build blank figure with the requested height
    """
    return {
        "data": [],
        "layout": {
            "height": height,
            "template": template,
            "xaxis": {"visible": False},
            "yaxis": {"visible": False},
        },
    }

app.layout = dbc.Container([
    header,
    dbc.Row(dcc.Graph(id='sa-map', figure=blank_fig(500))),
    dbc.Row([
        dbc.Col([
            dcc.RadioItems(
                id="geometry",
                options=[
                    {"label": i, "value": i}
                    for i in ["Blocks", "Block Groups", "Tracts"]
                ],
                value="Tracts",
                inline=True
            ),
        ], width=2),
        dbc.Col([
            dcc.Dropdown(
                id="tracts",
                # options=[
                #     {"label": i, "value": i}
                #     for i in all_tracts
                # ],
                multi=True,
                style={"color": "black"},
                # value=(),
            ),
            # dcc.Dropdown(id='graph-type')
        ], width=4)
    ]),
    # dcc.Store(id='pop-data', storage_type='session'),
])

@app.callback(
        Output("tracts", "value"),
        Input("sa-map", "clickData"),
        Input("sa-map", "selectedData"),
        State("tracts", "value"),
        State("sa-map", "clickData")
)

def update_tract_dropdown(clickData, selectedData, tracts, clickData_state):

    if ctx.triggered[0]["value"] is None:
        return tracts
   
    changed_id = [p["prop_id"] for p in ctx.triggered][0]
    

    if clickData is not None and "customdata" in clickData["points"][0]:
        tract = clickData["points"][0]["customdata"]
      
        if tract in tracts:
            tracts.remove(tract)
        elif len(tracts) < 10:
            tracts.append(tract)
    
  
    return tracts

@app.callback(
    Output("sa-map", "figure"),
    # Input("pop-data", "data"),
    Input("geometry", "value"),
    Input("tracts", "value")
)
def update_Choropleth(geometry, tracts):
    if geometry == "Block Groups":
        df = get_block_group_data()
        geo_data = bg_geo_data
        # print(geo_data)
        # print(geo_data.columns)
        # print(geo_data['GEOID20'])
    elif geometry == "Blocks":
        df = get_block_data()
        geo_data = block_geo_data
    elif geometry == "Tracts":
        df = get_tract_data()
        # geo_data = tract_geo_data
    
    geo_tracts_highlights = ()
    # print(geo_data)
    if tracts != None:
        tracts = list(map(str, tracts))
        geo_tracts_highlights = df[df['GEOID'].isin(tracts)]
    
    
    fig = get_figure(df, geo_tracts_highlights)


    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)