import pandas as pd
import argparse


resultado = pd.read_csv('/Users/anadeondarza/Desktop/ironhack_data/dataptmad0522_labs/Proyecto_Final/final.csv')


if __name__ == '__main__':
    def argument_parser():  
        parser = argparse.ArgumentParser(description= 'Por favor indica si quieres la informacion de una estacion o todas')
        parser.add_argument('-f','--function', type=str)
        args = parser.parse_args()
        return args
    

    argument_parser()
    if argument_parser().function == 'todas':
        result = pd.read_csv('/Users/anadeondarza/Desktop/ironhack_data/dataptmad0522_labs/Proyecto_Final/final.csv')
        print(result)
    elif argument_parser().function == 'una':
        print('Que monumento quieres saber?')
        x = input()
        dfi = resultado.set_index('Place of interest')
        print(dfi.loc[x])
    else:
        result = 'FATAL ERROR...you need to select the correct method'
        print(result)

