import pandas as pd
import requests

def new_columns_df (df):
    df[['new_col_1', 'new_col_2']] = df['col'].str.split('x' ,expand=True)
    df['new_col_1'] = df['new_col_1'].str.replace('y','',regex=True)
    df['new_col_2'] = df['new_col_2'].str.replace('y','',regex=True)
    df['new_col_2'] = df['new_col_2'].astype(float)
    df['new_col_1'] = df['new_col_1'].astype(float)
    return(df)

def drop_columns(df):
    df = df.drop(['col1', 'col2', 'col3','col4','col5', 'col6', 'col7', 'col8','col9','col10', 'col11', 'col12', 'col13'], axis =1)
    return df

def union (df1, df2):
    df = df1.assign(key="i").merge(df2.assign(key="i"), how='left', on='key')
    return df

#def mindistance (df):
    #df = union.groupby([col]).agg('min')
    #return df

def rename (df):
    df = df.rename(columns={'col1': 'col1_newname', 'col2':'col2_newname', 'col3': 'col3_newname', 'col4': 'col4_newname', 'col5' : 'col5_newname'})
    return df
