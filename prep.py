import pandas as pd

def prep_data(df): 
    """ Drop any null rows and those Single Family houses with 0 bedrooms and 0 bathrooms """
    df = df.dropna()
    df = df[df.bathroomcnt != 0]
    df = df[df.bedroomcnt != 0]
    df.drop(["Unnamed: 0"], axis=1, inplace=True)

    rename_columns = {
        "bathroomcnt": "bathrooms",
        "bedroomcnt": "bedrooms",
        "calculatedfinishedsquarefeet": "sqft",
        "taxvaluedollarcnt": "taxvalue"
    }

    df = df.rename(columns=rename_columns)

    return df
