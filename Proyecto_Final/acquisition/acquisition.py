import pandas as pd
import requests

def acquisition(path):
    response = requests.get(path)
    jsons = response.json()
    return(json)

def acquisition2(path):
    engine = create_engine(connect_str)
    inspector = inspect(engine)
    return(inspector)