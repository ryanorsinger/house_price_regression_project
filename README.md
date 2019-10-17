# House Price Regression Project

## Objective
Use property data to predict the values of single unit properties for properties sold in May and June of 2017.

Additional information we need outside of the linear model:
- Determine what state and county for each address
- Determine the distribution of *tax rates* for each county using the provided tax amount and tax value of each house.

## Notes
- For the first iteration of your model, use only square feet of the home, number of bedrooms, and number of bathrooms to estimate the properties assessed value, 'taxvaluedollarcnt'. You can expand this to other fields after you have completed an mvp (minimally viable product).
- You will want to read and re-read the requirements given by your stakeholders to be sure you are meeting all of their needs and representing it in your data, report and model.
- You will want to do some data validation or QA (quality assurance) to be sure the data you gather is what you think it is.
- You will want to make sure you are using the best fields to represent square feel of home, number of bedrooms and number of bathrooms. best => the most accurate and available information. You will need to do some data investigation in the database and use your domain expertise to make some judgement calls.

## Stakeholder and Deliverables
- Stakeholder is the zillow data science team. State goals as if this is an internal deliverable to the DS team.
- Deliverables:
1. A report (in the form of a presentation, both verbal and through a slides)
2. A github repository containing your jupyter notebook that walks through the pipeline along with the .py files necessary to reproduce your model.


## Pipeline
- Plan: Gin up a model as quickly as possible for square feet of the home, number of bedrooms, and number of bathrooms in order to estimate each property's assessed value - the "taxvaluedollarcnt".
- Acquire: Select taxvaluedollarcnt, #bedrooms, #bathrooms, and sqft from the properties_2017 table joined w/ propeprtylandusetype table. Filter on propertylandusetype and 
- Prepare: 