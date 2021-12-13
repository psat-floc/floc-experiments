import sys
import pandas as pd
import csv
from collections import Counter

filename = sys.argv[1]

data = pd.read_csv(filename, header=0).to_numpy()
len_data = len(data)

sum_all_users = 0
for user in range(len_data):
    nb_unique_cohorts = 0
    unique_cohorts = []
    for year in range(2,26):
        if(data[user][year] not in unique_cohorts) :
            unique_cohorts.append(data[user][year])
            nb_unique_cohorts += 1
            print("unique cohort found for user ", user, " for year ", year, " cohort id = ", data[user][year])
    sum_all_users += nb_unique_cohorts

print("Il y a en moyenne ", sum_all_users/len_data, " cohortes différentes par utilisateur")
