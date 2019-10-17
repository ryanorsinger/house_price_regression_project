import pandas as pd
from os import path

def get_url(database_name):
    from env import user, password, host
    return f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

def write_csv_of_data():
    df = get_zillow_data()
    df.to_csv("./zillow.csv")

def read_csv_of_data():
    return 

def get_zillow_data():
    # Single family only
    # Number of bedrooms
    # Number of bathrooms
    # square feet of the house
    # taxvaluedollarcnt

    # Use a double "%" in order to escape %'s default string formatting behavior.
    query = """SELECT bathroomcnt, bedroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt
        from properties_2017 
        join predictions_2017 using(parcelid)
        join propertylandusetype using(propertylandusetypeid)
        where predictions_2017.transactiondate like '2017-05%%' or predictions_2017.transactiondate like '2017-06%%'
        and propertylandusetype.propertylandusedesc = 'Single Family Residential'
        """

    url = get_url("zillow") 
    df = pd.read_sql(query, url)
    return df

def get_data():
    """
        reads from .csv or issues slq query, writes that sql as a .csv, and returns the data.
    """
    filename = "./zillow.csv"
    if path.exists(filename):
        print(f'Reading data from {filename}')
    else:
        print(f'Reading data from query, writing to {filename}, and returning the dataframe')
        write_csv_of_data()

    # Return the dataframe read from the csv
    return pd.read_csv(filename)
