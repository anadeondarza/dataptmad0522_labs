from sqlalchemy import create_engine
from sqlalchemy import inspect
import pandas as pd
import requests

def acquisition_1(path):
    response = requests.get(path)
    jsons = response.json()
    return(jsons)

def acquisition_2(connect_str):
    engine = create_engine(connect_str)
    inspector = inspect(engine)
    return(inspector)