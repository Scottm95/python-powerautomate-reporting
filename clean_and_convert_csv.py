

import pandas as pd
from pathlib import Path


# csv read into python script
df = pd.read_csv(r"C:\Users\SMacArthur\OneDrive - Three\Data Projects\Scorecard Data\sample_raw.csv")

output_folder = Path(r"C:\Users\SMacArthur\OneDrive - Three\Data Projects\Excel Test Output")

output_file = output_folder / "sample_cleaned.xlsx"



# Created column changed to date format
df["Created"] = pd.to_datetime(df['Created'])


# Time removed from Created column - leaving d/m/yyyy
df["Created"] = df["Created"].dt.strftime('%d/%m/%Y')



# **.str** - treats each column like a string so that methods like encode/decode can be applied

# remove non ASCII characters from column headings eg Â
cleaned_columns = df.columns.str.encode("ascii", errors="ignore")

# decode back into normal strings
cleaned_columns = cleaned_columns.str.decode("ascii")

# trim whitespaces from column headings
cleaned_columns = cleaned_columns.str.strip()

# update df with cleaned column names
df.columns = cleaned_columns





# save csv file as excel file
# rename tab to 'Query (1)'
excel_file = df.to_excel(output_file, sheet_name='Query (1)', index=False)

