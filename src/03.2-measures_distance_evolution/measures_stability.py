import sys
import pandas as pd
import csv
from collections import Counter

filename = sys.argv[1]
plotname = filename[:-4] + "_stability.csv"

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
avg_cohorts_by_user = sum_all_users/len_data
percentage_only_one_cohort = (nb_users_with_one_cohort/len_data)*100
percentage_only_one_cohort_or_zeros = (nb_users_with_one_cohort_or_zero/len_data)*100
print("Il y a en moyenne ", avg_cohorts_by_user, " cohortes différentes par utilisateur")
print("Il y a ", percentage_only_one_cohort, "% d'utilisateurs avec un seul cohortId")
print("Il y a ", percentage_only_one_cohort_or_zeros, "% d'utilisateurs avec un seul cohortId en dehors des zéros")

plot_file = open(plotname, "w",newline='')
plot_writer = csv.writer(plot_file)
plot_writer.writerow([0]) # necessary for the graph
plot_writer.writerow(['average different cohorts for one user', avg_cohorts_by_user])
plot_writer.writerow(['% users with only one cohortId', percentage_only_one_cohort])
plot_writer.writerow(['% users with only one cohortId except 0', percentage_only_one_cohort_or_zeros])
plot_writer.writerow([0]) # necessary for the graph