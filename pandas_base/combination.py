sales = {'Tony': 103,
         'Sally': 202,
         'Randy': 380,
         'Ellen': 101,
         'Fred': 82
        }

df_sales = pd.DataFrame(sales.items(), columns=["name", "sales"])
df_sales
#   name	sales
# 0	Tony	103
# 1	Sally	202
# 2	Randy	380
# 3	Ellen	101
# 4	Fred	82

region = {'Tony': 'West',
          'Sally': 'South',
          'Carl': 'West',
          'Archie': 'North',
          'Randy': 'East',
          'Ellen': 'South',
          'Fred': np.nan,
          'Mo': 'East',
          'HanWei': np.nan,
         }
df_region = pd.DataFrame(region.items(), columns=["name", "region"])
df_region
# 	name	region
# 0	Tony	West
# 1	Sally	South
# 2	Carl	West
# 3	Archie	North
# 4	Randy	East
# 5	Ellen	South
# 6	Fred	NaN
# 7	Mo	    East
# 8	HanWei	NaN

joined_df = df_region.join(df_sales.set_index("name"), on="name", how="left")
joined_df
# name	    region	sales
# 0	Tony	West	103.0
# 1	Sally	South	202.0
# 2	Carl	West	NaN
# 3	Archie	North	NaN
# 4	Randy	East	380.0
# 5	Ellen	South	101.0
# 6	Fred	NaN	    82.0
# 7	Mo	    East	NaN
# 8	HanWei	NaN	    NaN

joined_df = df_region.join(df_sales.set_index("name"), on="name", how="inner")
joined_df
# 	name	region	sales
# 0	Tony	West	103
# 1	Sally	South	202
# 4	Randy	East	380
# 5	Ellen	South	101
# 6	Fred	NaN	    82