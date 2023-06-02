import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd





def get_Choropleth(df, marker_opacity, fig=None):
    # print(df.index)
    # print(geo_data["FIPS"])
    if fig is None:
        fig = go.Figure()

    fig.add_trace(
        go.Choroplethmapbox(
            geojson=eval(df['geometry'].to_json()),
            # locations=df.index,
            # z=df['E_TOTPOP'],
            marker_opacity = marker_opacity,
            # customdata=df["FIPS"]
        )
    )

    return fig

def get_map(df):

    fig = go.Figure()
  

    

    return fig


def get_figure(df):

    print(df)
    fig = get_Choropleth(df, marker_opacity=0.4)
   
    
    fig.update_layout(mapbox_style="carto-positron", 
                            mapbox_zoom=10.4,
                            # mapbox_layers=layer,
                            mapbox_center={"lat": 39.65, "lon": -104.8},
                            margin={"r":0,"t":0,"l":0,"b":0},
                            uirevision='constant')
    
    # if len(geo_tracts_highlights) != 0:
    #     fig = get_Choropleth(df, geo_tracts_highlights, marker_opacity=1.0, fig=fig)
    

    return fig