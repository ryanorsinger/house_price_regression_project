from acquire import get_data
from prep import prep_data

# Get the raw data from .csv or MySQL query
raw = get_data()

# Remove nulls
df = prep_data(raw)

# Milestones before Friday:
# 2. Scale
# 3. Super basic Model

df.info()
df.describe()

# First pass for outlier detection:
# Do the value counts and distribution make sense?
# Is there anything way out of line here?
df.bedrooms.value_counts()      # encode as discrete
df.bathrooms.value_counts()     # encode as discrete
df.sqft.value_counts()          # can bin or scale
df.taxvalue.value_counts()      # scale this (also our target variable)
