# Drop the rows with amount <= 500. Group the unique customer IDs in the table and get the count of them.
# Return the count in the form of a DataFrame. 

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store = store[store['amount'] > 500]
    rich_count = store.groupby('customer_id')['amount'].nunique()
    return pd.DataFrame([len(rich_count)], columns=['rich_count'])