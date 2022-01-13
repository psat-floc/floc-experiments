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
  python3 src/03.2-measures_distance_evolution/measures_cohort_similarity.py $year $bits
done

for year in processed_data/2*.csv; do
  echo "calculating cohort similarity on $bits bits file: $year"
  python3 src/03.2-measures_distance_evolution/measures_cohort_similarity.py $year $bits
done

python3 src/03.3-measures_knn/generate_knn_distribution.py $bits

for year in processed_data_knn/cohorts_knn_*.csv; do
  echo "calculating knn cohort interests on $bits bits file: $year"
  python3 src/03.3-measures_knn/average_interest_by_cohort_knn.py $year $bits
  echo "calculating knn cohort similarity on $bits bits file: $year"
  python3 src/03.3-measures_knn/cohort_similarity_knn.py $year $bits
done

python3 src/03.4-measures_random/generate_random_distribution.py $bits

for year in processed_data_random/cohorts_random_*.csv; do
  echo "calculating random cohort interests on $bits bits file: $year"
  python3 src/03.4-measures_random/average_interest_by_cohort_random.py $year $bits
  echo "calculating random cohort similarity on $bits bits file: $year"
  python3 src/03.4-measures_random/cohort_similarity_random.py $year $bits
done




