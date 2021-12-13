import sys
import pandas as pd
import csv
from collections import Counter

filename = sys.argv[1]

data = pd.read_csv(filename, header=0).to_numpy()
len_data = len(data)
sum_all_users = 0
nb_users_with_one_cohort = 0
nb_users_with_one_cohort_or_zero = 0
for user in range(len_data):
    nb_unique_cohorts = 0
    unique_cohorts = []
    for year in range(1,26):
        if(data[user][year] not in unique_cohorts) :
            unique_cohorts.append(data[user][year])
            nb_unique_cohorts += 1
    sum_all_users += nb_unique_cohorts
    if(nb_unique_cohorts == 1) :
        nb_users_with_one_cohort += 1
        nb_users_with_one_cohort_or_zero += 1
    elif(nb_unique_cohorts == 2) :
        if(('0x0' in data[user]) | ('0x00' in data[user]) | ('0x000' in data[user])) :
            nb_users_with_one_cohort_or_zero += 1

print("Il y a en moyenne ", sum_all_users/len_data, " cohortes différentes par utilisateur")
print("Il y a ", (nb_users_with_one_cohort/len_data)*100, "% d'utilisateurs avec un seul cohortId")
print("Il y a ", (nb_users_with_one_cohort_or_zero/len_data)*100, "% d'utilisateurs avec un seul cohortId en dehors des zéros")