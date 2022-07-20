import pandas as pd
import argparse

resultado = pd.read_csv('/Users/anadeondarza/Desktop/ironhack_data/dataptmad0522_labs/Proyecto_Final.cvs')

if __name__ == '__main__':
    def argument_parser():  
        parser = argparse.ArgumentParser(description= 'Por favor indica si quieres la informacion de una estacion o todas')
        parser.add_argument('-f','--function', type=str)
        args = parser.parse_args()
        return args

    argument_parser()
    if argument_parser().function == 'todas':
        result = pd.read_csv('/Users/anadeondarza/Desktop/ironhack_data/dataptmad0522_labs/Proyecto_Final.cvs')
    elif argument_parser().function == 'una':
        print (input('Que monumento quieres saber?'))
        result =  resultado.loc[resultado['Place of interest'] == 'Place of interest']
    else:
        result = 'FATAL ERROR...you need to select the correct method'
    print(result)