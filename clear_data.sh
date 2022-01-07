#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

printf "${GREEN}Clearing all processed data...${NC}\n"

rm -f processed_data/*
rm -f a.out a.exe

printf "${GREEN}Everything is cleared${NC}\n"
