import sys
import pandas as pd
import numpy as np
import csv
from collections import Counter
from scipy import spatial

raw_year = sys.argv[1]
nb_bits = int(sys.argv[2])
year = raw_year[-8:-4]

filename_cohort_interest = "processed_data/cohort_interests_" + str(year) + ".csv"
filename_cohort_id = "processed_data/simhash_" + str(nb_bits) + "_" + str(year) + ".csv"
filename_user_interset = "processed_data/intermediary_data_" + str(year) + ".csv"

data_cohort_interest = pd.read_csv(filename_cohort_interest, header=None).to_numpy()
data_cohort_id = pd.read_csv(filename_cohort_id, header=0).to_numpy()
data_user_interest = pd.read_csv(filename_user_interset, header=None).to_numpy()

nb_users = len(data_cohort_id)
nb_cohorts = len(data_cohort_interest)
size_vector_interest = len(data_cohort_interest[0])

max_nb_cohorts = pow(2, nb_bits)
sum_cos_by_cohort = [0 for i in range(max_nb_cohorts)]
nb_users_by_cohort = [0 for i in range(max_nb_cohorts)]
for i in range(nb_users) :
    if(data_cohort_id[i][1] != "0x0"):
        cohort_id = data_cohort_id[i][1]
        decimal_cohort_id = int(cohort_id, 16)
        cohort_interest = None
        for j in range(nb_cohorts):
            if(data_cohort_interest[j][0] == cohort_id) :
                cohort_interest = data_cohort_interest[j][1:size_vector_interest]
        cos = np.dot(cohort_interest, data_user_interest[i])/np.linalg.norm(cohort_interest)/np.linalg.norm(data_user_interest[i])
        cos_distance = spatial.distance.cosine(cohort_interest, data_user_interest[i])
        sum_cos_by_cohort[decimal_cohort_id] += cos
        nb_users_by_cohort[decimal_cohort_id] += 1

filename = "processed_data/cohort_similarity_" + str(year) + "_" + str(nb_bits) + ".csv"
file_similarity = open(filename, "w",newline='')
file_writer = csv.writer(file_similarity)
file_writer.writerow([0]) # necessary for the graph
sum_all_cohorts = 0
sum_all_users = 0
for i in range(max_nb_cohorts) :
    if(nb_users_by_cohort[i] != 0):
        sum_all_cohorts += sum_cos_by_cohort[i]
        sum_all_users += nb_users_by_cohort[i]
        sum_cos_by_cohort[i] /= nb_users_by_cohort[i]
        file_writer.writerow([sum_cos_by_cohort[i]])
        

filename_global = "processed_data/global_cohort_similarity_" + str(nb_bits) + ".csv"
file_global = open(filename_global, "a",newline='')
global_writer = csv.writer(file_global)
avg = 0
if(sum_all_users != 0):
    avg = sum_all_cohorts/sum_all_users
global_writer.writerow([year, avg])



