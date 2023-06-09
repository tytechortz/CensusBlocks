import geopandas as gpd
import pandas as pd

# block_geo_data = gpd.read_file('Census_Blocks_2020_SHAPE_WGS/Census_Blocks_2020_WGS.shp')
# print(block_geo_data.columns)
# block_geo_data = block_geo_data[block_geo_data['COUNTYFP20'] == "005"]

# def get_block_group_data():
bg_geo_data = gpd.read_file('tl_2022_08_bg (1)/tl_2022_08_bg.shp')
bg_geo_arap = bg_geo_data[bg_geo_data['COUNTYFP'] == "005"]
bg_geo_arap['GEOID'] = bg_geo_arap['GEOID'].astype(int)

block_geo_data = gpd.read_file('Census_Blocks_2020_SHAPE_WGS/Census_Blocks_2020_WGS.shp')
block_geo_data['GEOID'] = block_geo_data['GEOID'].apply(lambda x: x[9:])
block_geo_data['GEOID'] = block_geo_data['GEOID'].astype(int)

tract_geo_data = gpd.read_file('2020_CT/ArapahoeCT.shp')
tract_geo_data = tract_geo_data.rename(columns={'FIPS':'GEOID'})
tract_geo_data['GEOID'] = tract_geo_data['GEOID'].astype(int)

def get_block_group_data():
   
    df1 = pd.read_csv('Data/BlockGroupPop.csv')
   
    geo_data = gpd.read_file('tl_2022_08_bg (1)/tl_2022_08_bg.shp')
   
    geo_arap = geo_data[geo_data['COUNTYFP'] == "005"]
   
    df1['Total'] = df1['Total'].str.replace(',', '').astype(int)
   
    geo_arap['GEOID'] = geo_arap['GEOID'].astype(int)
    df = geo_arap.merge(df1, on="GEOID")
    df.to_csv("GEOID.csv")
   

    return df

def get_block_data():
    df1 = pd.read_csv('Data/BlockPop.csv')
    
    # geo_data = gpd.read_file('Census_Blocks_2020_SHAPE_WGS/Census_Blocks_2020_WGS.shp')
    # geo_arap = block_geo_data[geo_data['COUNTYFP'] == "005"]
    # print(geo_arap.columns)
    print(block_geo_data.columns)
    # block_geo_data['GEOID'] = block_geo_data['GEOID'].apply(lambda x: x[9:])
    df1['Total'] = df1['Total'].str.replace(',', '').astype(int)
   
    block_geo_data['GEOID'] = block_geo_data['GEOID'].astype(int)
    print(block_geo_data)
    
    df = block_geo_data.merge(df1, on="GEOID")
   
    

    return df

def get_tract_data():
    df1 = pd.read_csv('Data/TractPop.csv')
    
    # geo_data = gpd.read_file('2020_CT/ArapahoeCT.shp')
    # geo_data = geo_data.rename(columns={'FIPS':'GEOID'})
  
    # geo_data['GEOID'] = geo_data['GEOID'].astype(int)
    df1['Total'] = df1['Total'].str.replace(',', '').astype(int)
    
   
    df = tract_geo_data.merge(df1, on="GEOID")
   
    
    return df


# def get_block_group_geo_data():
#     geo_data = gpd.read_file('tabblock20/tl_2020_08_tabblock20.shp')
#     geo_data = geo_data.rename(columns={'GEOID20':'FIPS'})

#     # print(geo_data.columns)

#     return geo_data

# def get_tract_geo_data():
#     geo_data = gpd.read_file('2020_CT/ArapahoeCT.shp')
#     # print(geo_data)

#     return geo_data

# def get_block_geo_data():
#     geo_data = gpd.read_file('tl_2022_08_bg (1)/tl_2022_08_bg.shp')
#     geo_arap = geo_data[geo_data['COUNTYFP'] == "005"]
#     # print(geo_data)

#     return geo_arap
