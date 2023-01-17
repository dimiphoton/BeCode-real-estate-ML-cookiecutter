import pandas as pd

sale_cols=['Living Area', 'Number of facades',
       'Number of rooms', 'Open fire', 'Price', 'State of the building',
       'Surface area of the plot of land', 'Surface of the land',
       'Terrace','type','zipcode']
rent_cols=['Living Area', 'Number of facades',
       'Number of rooms', 'Open fire', 'Price', 'State of the building',
       'Terrace','type','zipcode']

def x1000(df_sale):
    if (df_sale['Price']<40000) & (df_sale['Living Area']>80):
        return 1000*df_sale['Price']

def step0():
    """load csv file and creates indexed panda

    Args:
        file (str, optional): _description_. Defaults to 'data-a.csv'.
    """
    df0=pd.read_csv("data_a.csv",index_col="Id")



    for col in ['Area of the garden','Area of the terrace','Surface area of the plot of land','Surface of the land']:
        df0[col].fillna(value=0,inplace=True)
    df0.dropna
    
    df_sale=df0.loc[df0['To sell']==True][sale_cols]
    df_rent=df0.loc[df0['To rent']==True][rent_cols]
    return df_sale.dropna(), df_rent.dropna()

def step1bis(df_sale):
    """

    Args:
        df (_type_): _description_
    """
    df_sale['Cleaned Price']= 0
    for index, row in df_sale.iterrows():
        if (row['Price']<50000) & (row['Living Area']>100):
            #print('anormal')
            row['Cleaned Price']=1000*row['Price']

        else:
            row['Cleaned Price']=row['Price']
    return df_sale

def step1(df):
    df["Price"] = df["Cleaned Price"].apply(lambda x: x*1000 if x < 1000 else x)
    return df

def postcode2province(postcode):
    if postcode<1300:
        return 'Brussels'
    elif postcode<1500:
        return 'Walloon Brabant'
    elif postcode<2000:
        return 'FLemish Brabant'
    elif postcode<3000:
        return 'Antwerp'
    elif postcode<3500:
        return 'FLemish Brabant'
    elif postcode<4000:
        return 'Limburg'
    elif postcode<5000:
        return 'Liege'
    elif postcode<5681:
        return 'Namur'
    elif postcode<6600:
        return 'Hainaut'
    elif postcode<7000:
        return 'Luxemburg'
    elif postcode<8000:
        return 'Hainaut'
    elif postcode<9000:
        return 'West Flanders'
    elif postcode<10000:
        return 'East Flanders'
