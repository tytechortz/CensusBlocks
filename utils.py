import geopandas as gpd
import pandas as pd



def get_svi_data():
    df = pd.read_csv('Colorado_SVI_2020.csv')
    geo_data = gpd.read_file('2020_CT/ArapahoeCT.shp')

    df['FIPS'] = df['FIPS'].astype(str)
    df = df.set_index("FIPS")
    df = geo_data.merge(df, on="FIPS")

    return df



def get_geo_data():
    geo_data = gpd.read_file('tabblock20/tl_2020_08_tabblock20.shp')
    # print(geo_data)

    return geo_data