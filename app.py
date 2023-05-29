from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import geopandas as gpd
import plotly.graph_objects as go

app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.DARKLY])

header = html.Div("Arapahoe Census Tract SVI Data", className="h2 p-2 text-white bg-primary text-center")

bgcolor = "#f3f3f1"  # mapbox light map land color

template = {"layout": {"paper_bgcolor": bgcolor, "plot_bgcolor": bgcolor}}

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

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
    dbc.Row(dcc.Graph(id='ct-map', figure=blank_fig(500))),
])

@app.callback(
    Output("sa-map", "figure"),
    Input("map-category", "value"),
    # Input("graph-type", "value"),
    Input("tracts", "value")
)
def update_Choropleth(category, tracts):

    # changed_id = ctx.triggered[0][['prop_id'].split('.')[0]]
    # print(changed_id)
    
    geo_tracts_highlights = ()
    
    if tracts != None:
        geo_tracts_highlights = geo_data[geo_data['FIPS'].isin(tracts)]
    
        # print(geo_tracts_highlights)

    
    fig = get_figure(df, geo_data, geo_tracts_highlights)




    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)