
from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd



query_1 = '''

SELECT *
FROM bicimad_stations
'''

def transformatio_api(json, key):
    json = json[key]
    return json

def transformation_df(json):
    df = pd.json_normalize(json)
    return df

def unir_dfs (df1, df2):
    df = pd.concat([df1, df2], axis=0)
    return df

def transformation_sql_df(path, query_1):
    df = pd.read_sql_query(query_1, path)
    return df