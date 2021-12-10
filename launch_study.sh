#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

if [ $# -eq 0 ]; then
  printf "Please provide a number of bits: 8, 12, 16 or 20\n"
  exit 1
fi

nb_bits=$1

file=processed_data/2019.csv
if test -f "$file"; then
    printf "${RED}Since $file exists, we have deemed un-necessary to reprocess the ratings and movies CSV files.\n\n${NC}"
else
    printf "${RED}Pre-processing the data to have it comply with the scripts${NC}\n\n"
    ./src/01-process-data/process_data.sh
fi

sleep 2.5


printf "${RED}Computing the cohort IDs using SimHash and SortingLSH on ${nb_bits} bits${NC}\n\n"
sleep 2

./src/02-simhash-sortinglsh/process_cohorts.sh $nb_bits


printf "${RED}Measuring the uniqueness of each user in the dataset${NC}\n\n"
sleep 2

./src/03-measures/measures.sh $nb_bits

printf "${RED}Plotting everything to graphs${NC}\n\n"
sleep 2

./src/04-graphs/draw_graphs.sh

printf "${GREEN}Everything is ready${NC}\n"
