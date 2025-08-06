
**Python + Power Automate Reporting Automation**

---
## Overview
This project automates a manual reporting process using Python and Power Automate.  
It reduces a 30-minute daily task down to 5 minutes by  cleaning and formatting 8 csv files before saving these as excel files.
---

---
##  Tools Used
- **Python (Pandas + Pathlib)** — for data cleaning and Excel export  
- **Power Automate** — for file extraction and automated flow scheduling  
- **SharePoint** — destination for updated daily files 
---

---
##  Workflow Summary
1. **Power Automate** extracts 8 raw CSV files from a data source each morning  
2. CSV files are saved to a Sharepoint folder  
3. **Python script**:
   - Cleans column headers (removes special characters like `Â`, `\n`)  
   - Converts date/time fields to `dd/mm/yyyy`  
   - Exports cleaned data to Excel format with renamed sheet  
4. Final Excel files are saved to a Sharepoint folder which are used as data sources in a **Tableau dashboard**
---

---
## Example Files
Included  one sample CSV (with all sensitive data removed) to demonstrate the cleaning steps:
- `sample_raw.csv`: uncleaned version - csv file  
- `sample_cleaned.xlsx`: Excel file created after Python processing
---

---
## Python Script Highlights
df = pd.read_csv("sample_raw.csv")
df.columns = df.columns.str.encode("ascii", errors="ignore").str.decode("ascii").str.strip()
df["Created"] = pd.to_datetime(df["Created"]).dt.strftime('%d/%m/%Y')
df.to_excel("Payment_Support_Excel_File.xlsx", sheet_name="Query (1)", index=False)
---


---
## Folder Output
The cleaned Excel files are uploaded via Power Automate to a SharePoint folder used for departmental dashboards
---

---
## Impact
- Reduced task time from 30+ minutes to under 5 minutes  
- Improved consistency and accuracy of audit reporting  
- Enabled dashboard automation for senior analysts
---


---
## Project Structure
README.md
clean_and_convert_csv.py
sample_raw.csv
sample_cleaned.xlsx
flow_overview.png
---



## Note

Sample files included here are stripped of any sensitive customer or employee information.
