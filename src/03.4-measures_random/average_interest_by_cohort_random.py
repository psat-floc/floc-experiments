import sys
import pandas as pd
import csv

def add_tabs(tab1, tab2) :
    len_1 = len(tab1)
    len_2 = len(tab2)
    if (len_1 != len_2 & len_1 != 0) :
        raise Exception('Error : tabs must have the same size')
    elif (len_1 == 0) :
        new_tab = tab2
    else :
        new_tab = [0 for i in range(len_1)]
        for i in range(len_1) :
            new_tab[i] = tab1[i] + tab2[i]
    return new_tab

raw_year = sys.argv[1]
nb_bits = int(sys.argv[2])
year = raw_year[-8:-4]
filename_cohort_id = "processed_data_random/cohorts_random_" + str(nb_bits) + "_" + str(year) + ".csv"
filename_user_interset = "processed_data/intermediary_data_" + str(year) + ".csv"

data_cohort_id = pd.read_csv(filename_cohort_id, header=0).to_numpy()
data_user_interset = pd.read_csv(filename_user_interset, header=None).to_numpy()

nb_cohorts = pow(2, nb_bits)
cohort_interests = [[] for i in range(nb_cohorts)]
nb_users_by_cohort = [0 for i in range(nb_cohorts)]
nb_users = len(data_cohort_id)
for i in range(nb_users):
    cohort_interests[data_cohort_id[i][1]] = add_tabs(cohort_interests[data_cohort_id[i][1]], data_user_interset[data_cohort_id[i][0]])
    nb_users_by_cohort[data_cohort_id[i][1]] += 1

fichier_output = open("processed_data_random/cohort_interests_" + str(nb_bits) + "_" + str(year) + ".csv", "w",newline='')
writer = csv.writer(fichier_output)
for i in range(nb_cohorts) :
    if(nb_users_by_cohort[i] != 0) :
        cohort_interests[i] = [cohort_interest / nb_users_by_cohort[i] for cohort_interest in cohort_interests[i]]
        writer.writerow([i] + cohort_interests[i])
