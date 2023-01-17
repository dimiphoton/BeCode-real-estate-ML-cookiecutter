import pandas as pd

sale_cols=['Living Area', 'Number of facades',
       'Number of rooms', 'Open fire', 'Price', 'State of the building',
       'Surface area of the plot of land', 'Surface of the land',
       'Terrace','type','zipcode']
rent_cols=['Living Area', 'Number of facades',
       'Number of rooms', 'Open fire', 'Price', 'State of the building',
       'Terrace','type','zipcode']

def x1000(df_sale):
    if (df_sale['Price']<50000) & (df_sale['Living Area']>100):
        return 1000*df_sale['Price']

def step0():
    """load csv file and creates indexed panda

    Args:
        file (str, optional): _description_. Defaults to 'data-a.csv'.
    """
    df0=pd.read_csv("data_a.csv",index_col="Id")



    for col in ['Area of the garden','Area of the terrace','Surface area of the plot of land','Surface of the land']:
        df0[col].fillna(value=0,inplace=True)
    
    df_sale=df0.loc[df0['To sell']==True][sale_cols]
    df_rent=df0.loc[df0['To rent']==True][rent_cols]
    return df_sale, df_rent

def step1(df_sale):
    """

    Args:
        df (_type_): _description_
    """
    for index, row in df_sale.iterrows():
        if (row['Price']<50000) & (row['Living Area']>100):
            #print('anormal')
            row['Cleaned Price']=1000*row['Price']
        else:
            row['Cleaned Price']=row['Price']
