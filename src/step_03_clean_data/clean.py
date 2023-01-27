def clean(df):
    """clean data: either nothing, or tax infis

    Args:
        df (dataframe): _description_

    Returns:
        dataframe: _description_
    """
    df[('misc','Price/m2')]=df[('Target','Price')]/df[('Group 1','Living Area')]


    df[('Target','Price')]=df.apply(x1000, axis=1)


    # select  price and area for dropna:
    df_subset_0 = df.loc[:, (slice(None), ['Price','Living Area'])]
    df.dropna(subset=df_subset_0.columns, inplace=True)


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

    #oublié number of facades!

    return df


def x1000(df):
    if ((df[('misc','Price/m2')]<200)):
        return 1000*df[('Target','Price')]