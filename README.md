# floc-experiments

Testing how many users stay private using FLoC's whitepaper recommendations

## How to use

1. Make sure you use the correct version of `ratings.csv` and `movies.csv`. The
ones available in the repository being the sample ones. You can replace both of
these files with 15, 20 or 25M entries.
2. Prepare the data with `scripts/bash/process_data.sh`, which will prepare the
new CSV files divided by years and with the correct film tags.
3. Launch `scripts/bash/simhash.sh <nb-bits>`, nb-bits being the number of bits
  per cohort. This will process the CSV files and create an aggregated CSV file
  with all the cohort IDs per user per year.
