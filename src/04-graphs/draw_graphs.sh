#!/bin/bash

for file in processed_data/*plot*.csv ; do
  echo "Plotting $file"
  python3 src/04-graphs/plots.py $file
done
