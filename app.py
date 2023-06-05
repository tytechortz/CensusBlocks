from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
import json
from figures_utilities import (
    get_figure
)

from utils import (
    get_block_data,
    get_block_group_data,
    get_block_group_geo_data
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

# df = get_svi_data()
# geo_data = get_geo_data()
# print(df)

# all_tracts = geo_data["FIPS"].values

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
                value="Blocks",
                inline=True
            ),
        ], width=2),
        dbc.Col([
            # dcc.Dropdown(
            #     id="tracts",
            #     options=[
            #         {"label": i, "value": i}
            #         for i in all_tracts
            #     ],
            #     multi=True,
            #     style={"color": "black"},
            #     value=(),
            # ),
            # dcc.Dropdown(id='graph-type')
        ], width=4)
    ]),
    # dcc.Store(id='pop-data', storage_type='session'),
])

# @app.callback(
#         Output('pop-data', 'data'),
#         Input('geometry', 'value')
# )
# def get_pop_data(geometry):
#     if geometry == 'Block Groups':
#         df_sel = get_block_group_data()
#         print(df_sel)

#     return df_sel.to_json()

@app.callback(
    Output("sa-map", "figure"),
    # Input("pop-data", "data"),
    Input("geometry", "value"),
    # Input("tracts", "value")
)
def update_Choropleth(geometry):
    if geometry == "Block Groups":
        df = get_block_group_data()
    elif geometry == "Blocks":
        df = get_block_data()
    

    # print(df)
    # df = pd.DataFrame(data["result"])
    # print(df)
    # changed_id = ctx.triggered[0][['prop_id'].split('.')[0]]
    # print(changed_id)
    
    # geo_tracts_highlights = ()
    
    # if tracts != None:
    #     geo_tracts_highlights = geo_data[geo_data['FIPS'].isin(tracts)]
    
        # print(geo_tracts_highlights)
    # print(df)
    
    fig = get_figure(df)




    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)