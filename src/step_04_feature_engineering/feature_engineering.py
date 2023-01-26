import pandas as pd
import numpy as np

def feature_engineering_0(df):
    df[('my features', 'basic count')]=0
    df[('my features', 'advanced count')]=0

    coeff=np.array([-3,-2,-1,0,1,2])
    state_dic={'\nÀrestaurer\n':coeff[0],
                '\nÀrénover\n':coeff[1],
                '\nÀrafraîchir\n':coeff[2],
                '\nBon\n':coeff[3],
                '\nFraîchementrénové\n':coeff[4],
                '\nExcellentétat\n':coeff[5]}
    df[('my features','state_note')]=df[('Group 1','State of the building')].map(state_dic)

    df[('my features','malus')]=-df[('my features','state_note')]*df[('Group 1','Living Area')]

    tests_basic={'has kitchen':df['Group 2','Fully equipped kitchen'],
            'is furnished':df['Group 2','Furnished'],
            'has lot of facades':df['Group 2','Number of facades']>1,
            }

    tests_advanced={
    'has garden':df['Group 2','Garden'],
    'garden is big':df['Group 2','Area of the garden']>100,
    'has lot of land':df['Group 2','Area of the garden']>300,
    'has a swimming pool': df['Group 2','Swimming pool']
}

    for key, test in tests_basic.items():
        df.loc[test, ('my features','basic count')] += 1

    for key, test in tests_advanced.items():
        df.loc[test, ('my features','advanced count')] += 1

    df[('Target','logPrice')] = df[('Target','Price')].apply(lambda x: np.log(x))

    df2=df[[('Target','Price'),('Target','logPrice'),('Group 1','Living Area'),
        ('Group 1','Number of rooms'),('my features','basic count'),
        ('my features','advanced count'),('my features','malus')]]

    return df2