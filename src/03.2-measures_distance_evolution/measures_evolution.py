import sys
import pandas as pd
import csv
from collections import Counter

filename = sys.argv[1]
plotname = filename[:-4] + "_evolution_plot.csv"
plot_file = open(plotname, "w",newline='')
plot_writer = csv.writer(plot_file)
plot_writer.writerow([0]) # necessary for the graph

data = pd.read_csv(filename, header=0).to_numpy()
len_data = len(data)
all_nb_users_staying_in_cohort = 0
all_nb_users_staying_in_cohort_or_changing_from_0 = 0
for year in range(1, 25):
    nb_users_staying_in_cohort = 0
    nb_users_staying_in_cohort_or_changing_from_0 = 0
    for user in range(len_data):
        if(data[user][year] == data[user][year+1]):
            nb_users_staying_in_cohort += 1
            nb_users_staying_in_cohort_or_changing_from_0 += 1
        elif((data[user][year] == '0x0') | (data[user][year] == '0x00') | (data[user][year] == '0x000')):
            nb_users_staying_in_cohort_or_changing_from_0 += 1
    all_nb_users_staying_in_cohort += nb_users_staying_in_cohort
    all_nb_users_staying_in_cohort_or_changing_from_0 += nb_users_staying_in_cohort_or_changing_from_0
    percentage_all_nb_users_staying_in_cohort = 0
    percentage_all_nb_users_staying_in_cohort_or_changing_from_0 = 0
    if(len_data != 0):
        percentage_all_nb_users_staying_in_cohort = (nb_users_staying_in_cohort/len_data)*100
        percentage_all_nb_users_staying_in_cohort_or_changing_from_0 = (nb_users_staying_in_cohort_or_changing_from_0/len_data)*100
    print("Entre ", year + 1994, " et ", year + 1995, " il y a eu ", percentage_all_nb_users_staying_in_cohort, "% d'utilisateurs restant stables dans leur cohorte")
    print("Entre ", year + 1994, " et ", year + 1995, " il y a eu ", percentage_all_nb_users_staying_in_cohort_or_changing_from_0, "% d'utilisateurs restant stables dans leur cohorte ou obtenant un cohortId alors qu'ils était à 0")
    plot_writer.writerow([percentage_all_nb_users_staying_in_cohort, percentage_all_nb_users_staying_in_cohort_or_changing_from_0]) # Faire un graphe pour la première colonne et un graphe pour la deuxième colonne
#print("En moyenne, il y a ", (all_nb_users_staying_in_cohort/(len_data*25))*100, "% d'utilisateurs ayant un cohortId stable entre 2 années")
#print("En moyenne, il y a ", (all_nb_users_staying_in_cohort_or_changing_from_0/(len_data*25))*100, "% d'utilisateurs ayant un cohortId stable entre 2 années ou ne faisant qu'obtenir un cohortId alors qu'ils n'en avaient pas")
plot_writer.writerow([0]) # necessary for the graph