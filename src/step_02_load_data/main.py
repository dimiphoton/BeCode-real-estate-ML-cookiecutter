import pandas as pd
import os

def load():
    """this function loads a csv in a precise folder and returns a well indexed dataframe

    Args:
        dataset_name (str, optional): _name of the folder in the data/raw _. Defaults to 'dataset_01'.

    Returns:
        _type_: _description_
    """
    #script_directory = os.getcwd()
    #data_directory = os.path.abspath(os.path.join(script_directory, os.pardir, os.pardir, "data", "raw", dataset_name))
    #data_path = os.path.join(data_directory, 'data.csv')
    df=pd.read_csv("/home/dimi/BeCode/BeCode-real-estate-ML-cookiecutter/data/raw/dataset_01/data.csv")
    

    df['Offer'] = df.apply(lambda row: 'rent' if row['To rent'] else 'sale', axis=1)
    df.drop(['To rent', 'To sell','Surface area of the plot of land'], axis = 1, inplace = True)
    df = df.set_index(['Offer','Id'])
    columns_tuple=[]
    for f in df.columns:
        if f=='Price':
            columns_tuple.append(('Target',f))
        elif f in ['Number of rooms', 'Living Area','State of the building']:
            columns_tuple.append(('Group 1',f))
        elif f == 'zipcode':
            columns_tuple.append(('Spatial',f))
        else:
            columns_tuple.append(('Group 2', f))

    df.columns=pd.MultiIndex.from_tuples(columns_tuple)
    df.reindex(columns = ['Target','Group 1','Group 2','Spatial'], level=0)
    
    return df

