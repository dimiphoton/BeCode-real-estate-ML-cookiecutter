


for col in ['Area of the garden','Area of the terrace','Surface area of the plot of land','Surface of the land']:
    df0[col].fillna(value=0,inplace=True)
df0.dropna()
