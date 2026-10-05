This is to validate the backfill job.

1. Extract unique id records in prod or any table in database.
2. You must have the IDs of missing records.
3. CSV must be read using pd.read_csv. 
4. Replace the IDs to the designated unique ID in your table.
5. If you want to check the data first then you must print the designated variable and put head()
6. You can now extract the data using to_csv