#!/bin/bash

echo "Processing with simhash and sortingLSH"

echo "Getting the amount of users"

nb_users=`tail -n 1 unprocessed_data/ratings.csv | cut -d , -f 1`


gcc src/02-simhash-sortinglsh/gen_result_base.c

echo "Starting to get the cohorts"

# visit 8, 12, 16 and 20 bits
# for bits in $(seq 8 4 20);
for bits in $(seq 8 8);
do
  for year in processed_data/*.csv ; do
    echo "Currently processing on $bits bits file: $year"
    python src/02-simhash-sortinglsh/simhash.py $year $nb_users $bits 
  done

  dos2unix "processed_data/result_$bits_"*.csv
  echo "id" > "processed_data/all_cohorts_$bits.csv"
  ./a.out $nb_users >> "processed_data/all_cohorts_$bits.csv"

  for file in "processed_data/result_$bits_"* ; do
    echo "Joining file: $file"
    join -t , "processed_data/all_cohorts_$bits.csv" $file \
      >> tmp
    mv tmp "processed_data/all_cohorts_$bits.csv"
  done
  
  rm "processed_data/result_$bits_"*.csv
done

rm a.out

echo ""
echo "Done processing everything. Check processed_data/ for all_* files"

