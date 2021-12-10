#!/bin/bash

for bits in $(seq 8 8); do
  python src/03-measures/path-fingerprint.py \
    "processed_data/all_simhash_$bits"_fingerprint.csv

  python src/03-measures/path-fingerprint.py \
    "processed_data/all_sortinglsh_$bits"_fingerprint.csv
  
  python src/03-measures/path-no-fingerprint.py \
    "processed_data/all_simhash_$bits.csv"

  python src/03-measures/path-no-fingerprint.py \
    "processed_data/all_sortinglsh_$bits.csv"

done
