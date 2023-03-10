def clean(df):
    """clean data: either nothing, or tax infis

    Args:
        df (dataframe): _description_

    Returns:
        dataframe: _description_
    """

    df_subset_0 = df.loc[:, (slice(None), ['Number of rooms'])]
    df.dropna(subset=df_subset_0.columns, inplace=True)

    

    df[('misc','Price/m2')]=df[('Target','Price')]/df[('Group 1','Living Area')]


    #df.loc['rent'][('Target','Price')]=df.loc['rent'].apply(x1000, axis=1)

    # hard price cleaning


    # select  price and area for dropna:
    df_subset_1 = df.loc[:, (slice(None), ['Price','Living Area'])]
    df.dropna(subset=df_subset_1.columns, inplace=True)


    # select state of the building for fillna(\nÀrafraîchir\n')
    df_subset_1 = df.loc[:, (slice(None), ['State of the building'])]
    df.update(df_subset_1.fillna('\nÀrafraîchir\n'))

    #select specs for fillna(False)
    df_subset_2 = df.loc[:, (slice(None), ['Fully equipped kitchen','Furnished',
                                            'Open fire','Terrace','Garden','Swimming pool'])]
    df.update(df_subset_2.fillna(False))


    #select area for fillna(0)
    df_subset_3 = df.loc[:, (slice(None), ['Area of the terrace','Surface of the land','Area of the garden'])]
    df.update(df_subset_3.fillna(0))

    # drop houses with big living area

    df=df[df[('Group 1','Living Area')] < 500]

    #oublié number of facades!

    return df


def x1000(df):
    """multiply price per 1000

    Args:
        df (): dataframe

    Returns:
        _type_: _description_
    """
    if ((df[('misc','Price/m2')]<200)):
        return 1000*df[('Target','Price')]