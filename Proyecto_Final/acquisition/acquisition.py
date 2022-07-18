from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests
from shapely.geometry import Point
import geopandas as gpd 


def acquisition(path):
    response = requests.get(path)
    jsons = response.json()
    return(jsons)

def acquisition2(connect_str):
    engine = create_engine(connect_str)
    inspector = inspect(engine)
    return(inspector)