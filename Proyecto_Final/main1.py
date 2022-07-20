
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
import requests
from shapely.geometry import Point
import geopandas as gpd 
import argparse

query_1 = '''

    SELECT *
    FROM bicimad_stations

    '''

if __name__ == '__main__':

    def to_mercator(lat, long):
     c = gpd.GeoSeries([Point(lat, long)], crs=4326)
     c = c.to_crs(3857)
     return c

    def distance_meters(lat_start, long_start, lat_finish, long_finish):
        start = to_mercator(lat_start, long_start)
        finish = to_mercator(lat_finish, long_finish)
        return start.distance(finish)

    response = requests.get('https://datos.madrid.es/egob/GET/catalogo/209434-0-templos-otros.json')
    jsons_1 = response.json()
    json_trabajado = jsons_1['@graph']

    df_flat_1 = pd.json_normalize(json_trabajado)
    df_flat_1['Type of place'] = "Templos no catolicos"

    responses = requests.get('https://datos.madrid.es/egob/GET/catalogo/209426-0-templos-catolicas.json')
    json = responses.json()

    json_trabajado2 = json['@graph']

    df_flat = pd.json_normalize(json_trabajado2)
    df_flat['Type of place'] = "Templos catolicos"

    df_templos = pd.concat([df_flat, df_flat_1], axis=0)
    templos_df = df_templos.drop(['@id', '@type', 'id','relation','address.district.@id', 'address.area.@id', 'address.locality', 'address.postal-code','organization.organization-desc','organization.accesibility', 'organization.schedule', 'organization.services', 'organization.organization-name'], axis =1)

    connect_str = 'mysql+pymysql://ironhack_user:%Vq=c>G5@173.201.189.217/BiciMAD'
    engine = create_engine(connect_str)
    inspector = inspect(engine)

    df = pd.read_sql_query(query_1, connect_str)

    df[["longitud","latitud"]]=df["geometry.coordinates"].str.split(",",expand=True)
    df['longitud'] = df['longitud'].str.replace('[','',regex=True)
    df["latitud"]=df['latitud'].str.replace(']','',regex=True)

    df['latitud'] = df['latitud'].astype(float)
    df['longitud'] = df['longitud'].astype(float)

    estaciones_df = df.drop(['id', 'light', 'number','activate','no_available','geometry.coordinates', 'total_bases', 'dock_bikes', 'free_bases','reservations_count','geometry.type'], axis =1)

    union = templos_df.assign(key="Union").merge(estaciones_df.assign(key="Union"), how='left', on='key')

    union["distancia_final"] = union.apply(lambda x: distance_meters(x['location.latitude'], x['location.longitude'], x['latitud'], x['longitud']), axis=1)

    union = union.groupby(['distancia_final']).agg('min')
    union = union.sort_values(by=['title', 'distancia_final'])
    union = union.drop_duplicates('title', keep='first')

    resultado = union.drop(['location.latitude','location.longitude', 'key','latitud','longitud'], axis =1)

    resultado_1 = resultado.rename(columns={'title': 'Place of interest', 'address.street-address':'Place address', 'name': 'BiciMAD station', 'address': 'Station location', 'Type_of_pace' : 'Type of place'})

    def argument_parser():  
        parser = argparse.ArgumentParser(description= 'Por favor indica si quieres la información de una estación o todas')
        parser.add_argument('-f','--function', type=str)
        args = parser.parse_args()
        return args

    argument_parser()
    if argument_parser.function() == 'todas':
        result = pd.read_csv('/Users/anadeondarza/Desktop/ironhack_data/dataptmad0522_labs/Proyecto_Final.cvs')
    elif argument_parser.function() == 'una':
        print (input('Qué momento quieres saber?'))
        result =  resultado_1.loc[resultado_1['Place of interest'] == 'Place of interest']
    else:
        result = 'FATAL ERROR...you need to select the correct method'
    print(result)




 
   