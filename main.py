import pandas as pd

#prod_id must be extracted in prod table
prod_id = pd.read_csv("csv_name.csv")

#missing id mostly attached in the ticket
missing_id = pd.read_csv("csv_name1.csv")

result = []

for id in missing_id["id"]:
    if id not in prod_id["id"].values:
        result.append({
                "id": id,
                "status": "missing"
                }
                )

##result variable must be converted to a DataFrame and saved as a CSV file
result_df = pd.DataFrame(result)

#print(result_df.head())
result_df.to_csv("missing_ids.csv", index=False)