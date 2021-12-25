import sys
import pandas as pd
import numpy as np
import csv
from collections import Counter
from scipy import spatial, linalg, mat, dot

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

for i in range(nb_users) :
    if(data_cohort_id[i][1] != "0x0"):
        cohort_id = data_cohort_id[i][1]
        cohort_interest = None
        for j in range(nb_cohorts):
            if(data_cohort_interest[j][0] == cohort_id) :
                cohort_interest = data_cohort_interest[j][1:size_vector_interest]
        cos = dot(cohort_interest, data_user_interest[i])/np.linalg.norm(cohort_interest)/np.linalg.norm(data_user_interest[i])
        cos_distance = spatial.distance.cosine(cohort_interest, data_user_interest[i])
        print("cosine user n°" + str(i) + " = ", str(cos))
        print("cosine distance (= 1 - cosine) user n°" + str(i) + " = ", str(cos_distance))
        print()


