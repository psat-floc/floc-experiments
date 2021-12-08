#!/bin/bash

echo "Starting merge of both ratings and movies"

rm -rf processed_data/*

dos2unix unprocessed_data/*.csv


# merging movies and ratings together
# https://superuser.com/a/26869
sort -t , -k 2,2 unprocessed_data/ratings.csv > processed_data/sort1.csv
sort -t , -k 1,1 unprocessed_data/movies.csv > processed_data/sort2.csv

join -t , -1 2 -2 1 processed_data/sort1.csv processed_data/sort2.csv | \
  sort -t , -k 1,1 > processed_data/ratings_tmp.csv

echo "Files have been joined together"

rm processed_data/sort*.csv

echo "Adding the year and cleaning everything"

awk -f src/01-process-data/process_ratings.awk \
  processed_data/ratings_tmp.csv | \
  sed '1h;1d;$!H;$!d;G' | \
  sed '1 s/1970/year/g' \
  > processed_data/ratings_processed.csv

rm processed_data/ratings_tmp.csv

echo "Done! movies.csv and ratings.csv have been merged"
echo ""

echo "Starting to divide ratings_processed.csv to years files"

for i in $(seq 1995 2019);
do
  echo "$i"
  echo "movieId,userId,rating,timestamp,title,genres,year" > \
    "processed_data/$i.csv"
  grep ",$i$" processed_data/ratings_processed.csv >> "processed_data/$i.csv"
done

echo "Cleaning processed_data"

rm processed_data/ratings_processed.csv

echo "Done: your files are ready to be used for FLoC analysis"

