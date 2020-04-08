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

# Planning

## Overall Plan:
- State initial hypotheses of drivers of tax value
- Get an MVP out the door w/ a subset of features 
- Conduct deeper analysis 

## Project Deliverables
- Report (verbal, slides)
- Reproducible data pipeline
- Jupyter notebook that consumes the data pipeline and produces a predictive model
- Add county and state data for each address
- Demonstrate the distribution of tax rates for each county. The data has the tax amounts and tax values for each home, so the rate is a simple calculation. This is separate from the predicted tax values we'll get from the model.

## Minimum Viable Product 
- Predictive model for values of single unit properties sold in 2017 May-June. 

## Initial Hypotheses and Ideas
- bathroom count correlates with bedroom count
- bed/bath count both correlate with square footage
- A feature like squarefootage per room may be a useful feature, since the initial 3 features are likely tightly correlated w/ eachother
- Location will be a strong driver of tax value