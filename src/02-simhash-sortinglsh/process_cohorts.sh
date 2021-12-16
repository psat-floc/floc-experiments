#!/bin/bash

echo "Processing with simhash and sortingLSH"

echo "Getting the amount of users"

nb_users=`tail -n 1 unprocessed_data/ratings.csv | cut -d , -f 1`
bits=$1

gcc src/02-simhash-sortinglsh/gen_result_base.c

echo "Starting to get the cohorts"

# visit 8, 12, 16 and 20 bits
for year in processed_data/*.csv ; do
  echo "Currently processing on $bits bits file: $year"
  python3 src/02-simhash-sortinglsh/simhash.py $year $nb_users $bits 
done

echo "PROCESSING SIMHASH"

dos2unix "processed_data/simhash_$bits_"*.csv
echo "id" > "processed_data/all_simhash_$bits.csv"
./a.exe $nb_users >> "processed_data/all_simhash_$bits.csv"
dos2unix "processed_data/all_simhash_$bits.csv"

for file in "processed_data/simhash_$bits_"* ; do
  echo "Joining file: $file"
  join -t , "processed_data/all_simhash_$bits.csv" $file \
    >> tmp
  mv tmp "processed_data/all_simhash_$bits.csv"
done

echo "Adding fingerprinting"
for file in "processed_data/all_simhash_$bits_"* ; do
  echo ""
  python3 src/02-simhash-sortinglsh/fingerprint.py $file 
done

rm "processed_data/simhash_$bits"_*

echo "PROCESSING SORTINGLSH"

dos2unix "processed_data/sortinglsh_$bits_"*.csv
echo "id" > "processed_data/all_sortinglsh_$bits.csv"
./a.exe $nb_users >> "processed_data/all_sortinglsh_$bits.csv"
dos2unix "processed_data/all_sortinglsh_$bits.csv"

for file in "processed_data/sortinglsh_$bits_"* ; do
  echo "Joining file: $file"
  join -t , "processed_data/all_sortinglsh_$bits.csv" $file \
    >> tmp
  mv tmp "processed_data/all_sortinglsh_$bits.csv"
done

echo "Adding fingerprinting"
for file in "processed_data/all_sortinglsh_$bits_"* ; do
  echo ""
  python3 src/02-simhash-sortinglsh/fingerprint.py $file 
done

rm "processed_data/sortinglsh_$bits"_*

rm a.exe

echo ""
echo "Done processing everything. Check processed_data/ for all_* files"

