Lesson 0 - focus ruthlessly on the Minimum Viable Product. Get a model for a feature or two before you get fancy.

Lesson 1 - use two "%" characters with like inside a SQL query string going into pd.read_sql.
- `query = "SELECT * from predictions_2017 where transactiondate like '2017-05%%' or transactiondate like '2017-06%%' limit 10"` does the trick where
- `query = "SELECT * from predictions_2017 where transactiondate like '2017-05%' or transactiondate like '2017-06%' limit 10"` gives an unsupported character error
- Why? Legacy python behavior for "%" inside of strings being for formatted strings.




