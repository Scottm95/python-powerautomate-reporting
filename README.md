
**Python + Power Automate Reporting Automation**


## Overview
Automates daily reporting file delivery for downstream dashboards (Tableau). A Power Automate cloud flow exports 8 SharePoint Lists to CSV, a scheduled Python job cleans/standardises the files, and a follow-up flow publishes the cleaned Excel outputs back to SharePoint.


## Problem
- Daily extracts from multiple SharePoint Lists required repetitive cleaning/formatting before they were usable in reporting.
- Manual preparation took 30+ minutes/day and introduced inconsistency risk.
- Reporting needed a reliable, repeatable output schema across all 8 datasets.


## Approach
- **Extract (Power Automate – cloud @ 08:00):** pull data from 8 SharePoint Lists and generate CSV extracts in a raw SharePoint folder.
- **Transform (Python – Task Scheduler @ 08:30):** clean headers (remove non-ASCII artifacts), standardise date fields (e.g., `Created`), and export each dataset to Excel with consistent sheet naming.
- **Publish (Power Automate – cloud @ 09:00):** upload cleaned Excel files to the SharePoint reporting folder used by Tableau.



## Tools
- **Power Automate**
- **Python**
- **SharePoint**
- **Excel**



## Results
- Reduced manual effort for daily file preparation from 30+ minutes to a mostly automated workflow.
- Improved consistency by standardising column naming, date formats, and output structure across all 8 files.
- Enabled reliable downstream dashboard refresh using SharePoint-hosted Excel outputs.


## Pipeline (high level)
1. 08:00 – Power Automate exports 8 SharePoint Lists → CSV (raw folder)
2. 08:30 – Task Scheduler runs Python: CSV → cleaned Excel (standard schema)
3. 09:00 – Power Automate publishes Excel outputs to SharePoint (reporting folder)



## Files
- `clean_and_convert_csv.py` – transformation script*
- `sample_raw.csv` – anonymised example input
- `sample_cleaned.xlsx` – example output after processing
- `flow_overview.png` – automation overview
- `runbook.md` – schedule, inputs/outputs, operational checks
- `data_quality.md` – cleaning/standardisation rules and validation notes

> Note: This repo includes a simplified example script showing the core transforms (header cleaning + `Created` standardisation). In production, the same logic is applied across 8 daily CSV extracts on a scheduled run.



