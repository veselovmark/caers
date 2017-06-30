'''
    cleaning and exploring CAERS data
'''
import pandas
import os
import sys



def main():

    caersDir = os.environ['CAERS']

    caersFile = os.path.join(caersDir, 'data', 
        'CAERS_ASCII_2004_2017Q1.csv')

    cData = pandas.read_csv(caersFile, dtype=str)

    cData.rename(columns=lambda x: (x.replace(' ', '_')
        .replace('#', 'No')), inplace=True)

    cDataOutFile = os.path.join(caersDir, 'data', 
        'caers_clean.csv')

    cData.to_csv(cDataOutFile, index=False)

if __name__ == '__main__':
    main()