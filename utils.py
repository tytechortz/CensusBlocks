import geopandas as gpd
import pandas as pd



def get_block_group_data():
    # df = pd.read_csv('DECENNIALDHC2020.P1-Data.csv')
    df1 = pd.read_csv('BlockGroupPop.csv', dtype=str)
    # geo_data = gpd.read_file('Census_Blocks_2020_SHAPE_WGS/Census_Blocks_2020_WGS.shp')
    geo_data = gpd.read_file('tl_2022_08_bg (1)/tl_2022_08_bg.shp')
   
    geo_arap = geo_data[geo_data['COUNTYFP'] == "005"]
   
    df1['Total'] = df1['Total'].str.replace(',', '').astype(int)
    
    
    df = geo_arap.merge(df1, on="GEOID")
    df.to_csv("GEOID.csv")
   

    return df

def get_block_data():
    df1 = pd.read_csv('DECENNIALDHC2020.P1-Data.csv')
    # df1 = pd.read_csv('BlockGroupPop.csv', dtype=str)
    geo_data = gpd.read_file('Census_Blocks_2020_SHAPE_WGS/Census_Blocks_2020_WGS.shp')
    # geo_data = gpd.read_file('tl_2022_08_bg (1)/tl_2022_08_bg.shp')
    # print(geo_data.columns)
    # print(df1.columns)
    # print(geo_data['GEOID20'])
    # df1.columns.values[0] = 'GEOID20'
    df1['GEOID20'] = df1['GEO_ID'].apply(lambda x: x[9:])
    # print(df1['GEOID20'])
    df1.columns.values[2] = 'Total'
    print(df1.columns)
    print(df1['Total'])
    geo_arap = geo_data[geo_data['COUNTYFP20'] == "005"]
    # print(geo_arap['geometry'])
    # df1['Total'] = df1['Total'].str.replace(',', '').astype(int)
    
    
    df = geo_arap.merge(df1, on="GEOID20")
    # print(df['geometry'])
    

    return df


def get_block_group_geo_data():
    geo_data = gpd.read_file('tabblock20/tl_2020_08_tabblock20.shp')
    # print(geo_data)

    return geo_data