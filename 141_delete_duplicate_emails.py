# Get the min ID associated to each email, drop the IDs that do not match with min IDs.

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # person.sort_values(by=['id'], inplace=True)
    # person.groupby(['email'])['id'].min().reset_index() # Cannot do this in-place
    min_id = person.groupby(['email'])['id'].transform('min')
    id_to_delete = person[person['id'] != min_id]
    person.drop(id_to_delete.index, inplace=True)