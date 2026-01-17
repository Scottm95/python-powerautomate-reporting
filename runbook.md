
# Runbook (Reporting Automation Pipeline)

## Schedule
- 08:00 – Power Automate (cloud): export 8 SharePoint Lists → CSV (raw folder)
- 08:30 – Windows Task Scheduler: run `clean_and_convert_csv.py`
- 09:00 – Power Automate (cloud): publish cleaned Excel outputs to reporting folder

## Inputs
- Source: 8 SharePoint Lists (cloud export)
- Raw output location: SharePoint Folder
- Expected: 8 CSV files present before 08:30

## Processing (Python)
- Cleans column headers (removes non-ASCII characters / whitespace)
- Standardises date fields (e.g., `Created`)
- Names each sheet to assist with SQL/Alteryx code for Tableau
- Exports to `.xlsx` with consistent sheet naming

## Outputs
- Cleaned Excel location: SharePoint Folder
- Consumer: Tableau dashboard refresh

## Success checks
- All 8 Excel files updated
- File sizes non-zero; spot-check row counts for one file if investigating issues
