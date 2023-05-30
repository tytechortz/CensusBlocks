import geopandas as gpd
import pandas as pd



def get_svi_data():
    df = pd.read_csv('DECENNIALDHC2020.P1-Data.csv')
    geo_data = gpd.read_file('Census_Blocks_2020_SHAPE_WGS/Census_Blocks_2020_WGS.shp')
    # print(df.columns)
    df.drop(columns=['Unnamed: 4', 'P1_001NA', 'NAME'], axis=1, inplace=True)
    df = df.drop(df.index[0])
    df['GEOID20'] = df['GEO_ID'].apply(lambda x: x[9:])
    df.drop('GEO_ID', axis=1, inplace=True)
    # print(df)
    # print(df['NAME'])
    # print(geo_data['GEOID20'])
    df = df.rename(columns={'GEOID': 'GEOID20'})
    # df['FIPS'] = df['FIPS'].astype(str)
    # df = df.set_index("FIPS")
    print(df.columns)
    print(geo_data.columns)
    df = geo_data.merge(df, on="GEOID20")
    print(df)

    return df



def get_geo_data():
    geo_data = gpd.read_file('tabblock20/tl_2020_08_tabblock20.shp')
    # print(geo_data)

    return geo_data