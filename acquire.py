import pandas as pd
from os import path

def get_url(database_name):
    from env import user, password, host
    return f'mysql+pymysql://{user}:{password}@{host}/{database_name}'

def write_csv_of_data():
    df = get_zillow_data()
    df.to_csv("./zillow.csv")

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

def get_data(refresh = False):
    """
        reads from .csv or issues slq query, writes that sql as a .csv, and returns the data.
        run get_data() to get a dataframe from
        run get_data(refresh = True) to 
    """
    filename = "./zillow.csv"

    if path.exists(filename) and refresh:
        # delete file
        os.remove(filename)
        print(f'The old version of {filename} is now deleted')

        # delete filename
        write_csv_of_data()
        print(f"A new {filename} is created from a fresh SQL query")
        
    elif path.exists(filename):
        print(f'Data read from {filename}')
    else:
        print(f'Reading data from SQL, writing to {filename}, and returning the dataframe')
        write_csv_of_data()

    # Return the dataframe read from the csv
    return pd.read_csv(filename)
