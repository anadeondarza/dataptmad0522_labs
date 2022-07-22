import pandas as pd

def new_columns_df (df,new_col_1,new_col_2, col, x, y ,c):
    df[['new_col_1', 'new_col_2']] = df['col'].str.split('x' ,expand=True)
    df['new_col_1'] = df['new_col_1'].str.replace('y','',regex=True)
    df['new_col_2'] = df['new_col_2'].str.replace('c','',regex=True)
    df['new_col_2'] = df['new_col_2'].astype(float)
    df['new_col_1'] = df['new_col_1'].astype(float)
    return(df)

def drop_columns(df,col1, col2, col3,col4,col5, col6, col7, col8,col9,col10, col11, col12, col13):
    df = df.drop(['col1', 'col2', 'col3','col4','col5', 'col6', 'col7', 'col8','col9','col10', 'col11', 'col12', 'col13'], axis =1)
    return df
def drop_columns2 (df,col1, col2, col3,col4,col5, col6, col7, col8,col9,col10, col11):
    df = df.drop(['col1', 'col2', 'col3','col4','col5', 'col6', 'col7', 'col8','col9','col10', 'col11'], axis =1)
    return df

def union (df1, df2, hey,how, on):
    df = df1.assign(key="i").merge(df2.assign(key="i"), how='left', on='key')
    return df

def mindistance (df, colf, cola):
    df = df.groupby(['colf']).agg('min')
    df= df.sort_values(by=['colf', 'cola'])
    df = df.drop_duplicates('colf', keep='first')
    return 


def rename (df, columns):
    df = df.rename(columns={'colz': 'colz_newname', 'coly':'coly_newname', 'colx': 'colx_newname', 'colw': 'colw_newname', 'colv' : 'colv_newname'})
    return df
