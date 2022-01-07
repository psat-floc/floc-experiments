#!/bin/bash

bits=$1

python3 src/03-measures/path-fingerprint.py \
  "processed_data/all_simhash_$bits"_fingerprint.csv

python3 src/03-measures/path-fingerprint.py \
  "processed_data/all_sortinglsh_$bits"_fingerprint.csv

python3 src/03-measures/path-no-fingerprint.py \
  "processed_data/all_simhash_$bits.csv"

python3 src/03-measures/path-no-fingerprint.py \
  "processed_data/all_sortinglsh_$bits.csv"

python3 src/03.2-measures_distance_evolution/measures_stability.py \
  "processed_data/all_simhash_$bits"_fingerprint.csv

python3 src/03.2-measures_distance_evolution/measures_stability.py \
  "processed_data/all_sortinglsh_$bits"_fingerprint.csv

python3 src/03.2-measures_distance_evolution/measures_evolution.py \
  "processed_data/all_simhash_$bits"_fingerprint.csv

python3 src/03.2-measures_distance_evolution/measures_evolution.py \
  "processed_data/all_sortinglsh_$bits"_fingerprint.csv

python3 src/03.2-measures_distance_evolution/measures_size.py $bits

for year in processed_data/1*.csv; do
  echo "calculating cohort similarity on $bits bits file: $year"
  python3 src/03.2-measures_distance_evolution/measures_distance.py $year $bits
done

for year in processed_data/2*.csv; do
  echo "calculating cohort similarity on $bits bits file: $year"
  python3 src/03.2-measures_distance_evolution/measures_distance.py $year $bits
done



