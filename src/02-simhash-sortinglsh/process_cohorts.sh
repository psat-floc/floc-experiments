#!/bin/bash

echo "Processing with simhash and sortingLSH"

echo "Getting the amount of users"

nb_users=`tail -n 1 unprocessed_data/ratings.csv | cut -d , -f 1`

echo "Starting to get the cohorts"

# visit 8, 12, 16 and 20 bits
for bits in $(seq 8 4 20);
do
  for year in processed_data/*.csv ; do
    echo "Currently processing on $bits bits file: $year"
    python src/02-simhash-sortinglsh/simhash.py $year $nb_users $bits 
  done
done

exit 0 
  
  dos2unix "../../results_cohort_id/simhash/results/result_$bits_"*.csv
  cp result_base.csv "../../results_cohort_id/simhash/all_cohortID_$bits.csv"
  for file in ../../results_cohort_id/simhash/results/* ; do
    echo $file
    join -t , "../../results_cohort_id/simhash/all_cohortID_$bits.csv" $file >> tmp
    mv tmp "../../results_cohort_id/simhash/all_cohortID_$bits.csv"
  done
done



