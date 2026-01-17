
# Data Preparation & Quality (Automation Pipeline)

## Standardisation
- Removed non-ASCII artifacts and whitespace from CSV column headers (consistent schema across refreshes)
- Standardised date fields (e.g., `Created`) for consistent downstream parsing
- Exported to Excel with consistent sheet naming

## Sanity checks (operational)
- Confirmed all 8 CSV extracts exist before the scheduled Python run
- Verified output files refresh daily (modified timestamps) and are non-empty
