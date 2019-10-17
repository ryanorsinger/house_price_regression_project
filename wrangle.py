from acquire import get_data
from prep import prep_data

raw = get_data()
df = prep_data(raw)

# TO DOs

# 1. plot distributions of individual variables to identify outliers
#        beds vs. baths, baths vs. sqft, sqft vs, price, etc...

# 2. Add a data dictionary that defines all fields used in model or analysis
#        with explanation of why that field? Why one field over another, etc...

# Milestones before Friday:
# 1. drop nulls
# 2. Scale
# 3. Super basic Model