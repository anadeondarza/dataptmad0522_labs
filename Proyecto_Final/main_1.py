
from typing import final
import pandas as pd
import acquisition as ac
import transformation as ta
import manipulation as mp 
import geofunciones as lam
import argparse

path1 = 'https://datos.madrid.es/egob/GET/catalogo/209434-0-templos-otros.json'
path2 = 'https://datos.madrid.es/egob/GET/catalogo/209426-0-templos-catolicas.json'
connect_str = 'mysql+pymysql://ironhack_user:%Vq=c>G5@173.201.189.217/BiciMAD'
new_col_1 = ["longitud"]
new_col_2 = ["latitud"]
col6 = ["geometry.coordinates"]
x = ","
y = '['
c = ']'
cols = ['id', 'light', 'number','activate','no_available','geometry.coordinates', 'total_bases', 'dock_bikes', 'free_bases','reservations_count','geometry.type']
cols2 = ['@id', '@type', 'id','relation','address.district.@id', 'address.area.@id', 'address.locality', 'address.postal-code','organization.organization-desc','organization.accesibility', 'organization.schedule', 'organization.services', 'organization.organization-name']
col1 = 'location.latitude'
col2 = 'location.longitude'
col3 = 'latitud'
col4 = 'longitud'
key= "i"
how='left'
on='key'
col_output = ["distancia_final"]
columns={'colz': 'colz_newname', 'coly':'coly_newname', 'colx': 'colx_newname', 'colw': 'colw_newname', 'colv' : 'colv_newname'}
colz = 'title'
colz_newname = 'Place of interest'
coly = 'address.street-address'
coly_newname = 'Place address'
colx = 'name'
colx_newname = 'BiciMAD station'
colw = 'address'
colw_newname = 'Station location'
colv = 'Type_of_pace'
colv_newname = 'Type of place'
colf = 'distancia_final'
cola = 'title'


if __name__ == '__main_1__':

    json_1 = ac.acquisition(path1)
    json_2 = ac.acquisition(path2)
    df = ac.acquisition2(connect_str)
    df1 = ta.transformatio_api(json_1)
    df2 = ta.transformatio_api(json_2)
    df3 = ta.transformation_df(df1)
    df4 = ta.transformation_df(df2)
    df_final = ta.unir_dfs(df3, df4)
    df_sql = ta.transformation_sql_df(connect_str)
    df_newcolumnsql = mp.new_columns_df (df_sql, new_col_1, new_col_2, col6, x , y, c)
    df_casisql = mp.drop_columns(df_newcolumnsql,cols)
    df_casiapi = mp.drop_columns(df_final, cols2)
    df_resultado = mp.union(df_casiapi,df_casisql, key, how, on)
    df__func = lam.apply_lamda (df_resultado, col_output, col1, col2, col3, col4)
    df_result = mp.mindistance (df_resultado,colf, cola)
    resultado = mp.rename (df_result,columns)

    def argument_parser():  
        parser = argparse.ArgumentParser(description= 'Por favor indica si quieres la información de una estación o todas' )
        parser.add_argument('-f', '--function', type=str)
        args = parser.parse_args()
        return args


    print(type(argument_parser()))
    if argument_parser() == 'todas':
        result = pd.read_csv('/Users/anadeondarza/Desktop/ironhack_data/dataptmad0522_labs/Proyecto_Final.cvs')
    elif argument_parser() == 'una':
        print (input('Qué momento quieres saber?'))
        result =  resultado.loc[resultado['Place of interest'] == 'Place of interest']
    else:
        print(result = 'FATAL ERROR...you need to select the correct method')
    print(f'The result is => {result}')

    