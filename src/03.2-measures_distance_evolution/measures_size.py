import sys
import pandas as pd
import numpy as np
import csv
from collections import Counter

nb_bits = int(sys.argv[1])
max_nb_cohorts = pow(2, nb_bits)

#   Simhash
filename_nb_cohorts_sim = "processed_data/nb_cohorts_simhash_" + str(nb_bits) + ".csv"
file_nb_cohorts_sim = open(filename_nb_cohorts_sim, "w",newline='')
nb_cohorts_writer_sim = csv.writer(file_nb_cohorts_sim)

filename_size_cohorts_sim = "processed_data/size_cohorts_simhash_" + str(nb_bits) + ".csv"
file_size_cohorts_sim = open(filename_size_cohorts_sim, "w",newline='')
size_cohorts_writer_sim = csv.writer(file_size_cohorts_sim)

for year in range(1995, 2020) :
    nb_users_by_cohort = [0 for i in range(max_nb_cohorts)]
    filename_cohort_id = "processed_data/simhash_" + str(nb_bits) + "_" + str(year) + ".csv"
    data_cohort_id = pd.read_csv(filename_cohort_id, header=0).to_numpy()
    len_data = len(data_cohort_id)
    for i in range(len_data):
        if(data_cohort_id[i][1] != '0x0'):
            nb_users_by_cohort[int(data_cohort_id[i][1], 16)] += 1

    nb_cohorts = 0
    sum_users = 0
    for i in range(max_nb_cohorts):
        if(nb_users_by_cohort[i] != 0):
            nb_cohorts += 1
            sum_users += nb_users_by_cohort[i]
    nb_cohorts_writer_sim.writerow([year, nb_cohorts])
    avg = 0
    if(nb_cohorts != 0):
        avg = sum_users/nb_cohorts
    size_cohorts_writer_sim.writerow([year, avg])

#   Sorting lsh
filename_nb_cohorts_lsh = "processed_data/nb_cohorts_sortinglsh_" + str(nb_bits) + ".csv"
file_nb_cohorts_lsh = open(filename_nb_cohorts_lsh, "w",newline='')
nb_cohorts_writer_lsh = csv.writer(file_nb_cohorts_lsh)

filename_size_cohorts_lsh = "processed_data/size_cohorts_sortinglsh_" + str(nb_bits) + ".csv"
file_size_cohorts_lsh = open(filename_size_cohorts_lsh, "w",newline='')
size_cohorts_writer_lsh = csv.writer(file_size_cohorts_lsh)

for year in range(1995, 2020) :
    filename_cohort_id = "processed_data/sortinglsh_" + str(nb_bits) + "_" + str(year) + ".csv"
    data_cohort_id = pd.read_csv(filename_cohort_id, header=0).to_numpy()
    len_data = len(data_cohort_id)
    for i in range(len_data):
        if(data_cohort_id[i][1] != '0x0'):
            nb_users_by_cohort[int(data_cohort_id[i][1], 16)] += 1

    nb_cohorts = 0
    sum_users = 0
    for i in range(max_nb_cohorts):
        if(nb_users_by_cohort[i] != 0):
            nb_cohorts += 1
            sum_users += nb_users_by_cohort[i]
    nb_cohorts_writer_lsh.writerow([year, nb_cohorts])
    avg = 0
    if(nb_cohorts != 0):
        avg = sum_users/nb_cohorts
    size_cohorts_writer_lsh.writerow([year, avg])



