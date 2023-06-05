import geopandas as gpd
import pandas as pd



def get_svi_data():
    # df = pd.read_csv('DECENNIALDHC2020.P1-Data.csv')
    df1 = pd.read_csv('BlockGroupPop.csv', dtype=str)
    # geo_data = gpd.read_file('Census_Blocks_2020_SHAPE_WGS/Census_Blocks_2020_WGS.shp')
    geo_data = gpd.read_file('tl_2022_08_bg (1)/tl_2022_08_bg.shp')
    # print(geo_data)
    # print(geo_data['STATEFP'])
    # print(geo_data['COUNTYFP'])
    # print(geo_data['TRACTCE'])
    # print(geo_data['BLKGRPCE'])
    # print(geo_data['GEOID'])
    # print(df.columns)
    # print(df.dtypes)
    
    geo_arap = geo_data[geo_data['COUNTYFP'] == "005"]
    
    # df1['GEOID'] = df1['GEOID'].astype(int)
    # geo_arap['GEOID'] = geo_arap['GEOID'].astype(int)
    # geo_arap = geo_arap.sort_values(by=['GEOID'], ascending=True)
    # print("DF1")
    # print(df1['GEOID'])
    # print("GEO_ARAP")
    # df1['Total'].astype(int)
    df1['Total'] = df1['Total'].str.replace(',', '').astype(int)
    
    # print(geo_arap['GEOID'])
    print(df1.dtypes)
    # geo_arap.to_csv('GEO.csv')
    # df1.to_csv('DF1.csv')
    
    # df.drop(columns=['Unnamed: 4', 'P1_001NA', 'NAME'], axis=1, inplace=True)
    # df = df.drop(df.index[0])
    # df['GEOID'] = df['GEO_ID'].apply(lambda x: x[9:])
    # df.drop('GEO_ID', axis=1, inplace=True)
    # print(df['GEOID'])
    # print(df['NAME'])
    # print(geo_data['GEOID20'])
    # df = df.rename(columns={'GEOID': 'GEOID20'})
    # df1['GEOID'] = df1['GEOID'].astype(str)
    # df = df.set_index("FIPS")
    # print(df.columns)
    # print(geo_data.columns)
    df = geo_arap.merge(df1, on="GEOID")
    df.to_csv("GEOID.csv")
    # print(df.columns)
    # print(df['GEOID'])

    return df



def get_geo_data():
    geo_data = gpd.read_file('tabblock20/tl_2020_08_tabblock20.shp')
    # print(geo_data)

    return geo_data