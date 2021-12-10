#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "${RED}Pre-processing the data to have it comply with the scripts${NC}\n\n"

./src/01-process-data/process_data.sh

printf "${RED}Computing the cohort IDs using SimHash and SortingLSH${NC}\n\n"

./src/02-simhash-sortinglsh/process_cohorts.sh

printf "${RED}Measuring the uniqueness of each user in the dataset${NC}\n\n"

./src/03-measures/measures.sh

printf "${RED}Plotting everything to graphs${NC}\n\n"

./src/04-graphs/draw_graphs.sh

printf "${GREEN}Everything is ready${NC}"
