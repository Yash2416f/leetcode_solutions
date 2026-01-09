#leetcode problem 196: delete duplicate emails
# https://leetcode.com/problems/delete-duplicate-emails/description/

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(subset='email', inplace=True)