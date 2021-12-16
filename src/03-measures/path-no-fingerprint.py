import sys
import pandas as pd
import csv
from collections import Counter

#0 = id
#1 = 1995
#25 = 2019


filename = sys.argv[1]
plotname = filename[:-4] + "_plot.csv"

data = pd.read_csv(sys.argv[1], header=0).to_numpy()
len_data = len(data)

for user in range(len_data):
    for year in range(1, 25):
        if(data[user][year] != "0x0" and data[user][year+1] == "0x0"):
            data[user][year+1] = data[user][year]

#    fichier = open("whatv.csv", "w",newline='')
#    writer = csv.writer(fichier)
#    writer.writerows(data)

nb_years = 26
counter = Counter()

for years in range(1, nb_years):
    year_counter = "1995-"+str(1994+years)
    print(year_counter)
    counter[year_counter] = Counter()


    for user in range(0, len_data):
        str_cat = ''.join(str(e) for e in data[user][1: years])
        counter[year_counter][str_cat] += 1

plot_file = open(plotname, "w",newline='')
plot_writer = csv.writer(plot_file)
plot_writer.writerow([0]) # necessary for the graph

for years in counter:
    nb_identified_users = 0

    for key in counter[years]:
        if(counter[years][key] == 1):
            nb_identified_users += 1
        
    if len_data > 0:
        avg = (nb_identified_users / len_data) * 100
    else:
        avg = 0
    plot_writer.writerow([avg])
    print(years + ": " + str(avg))

plot_writer.writerow([0]) # necessary for the graph

"""
0
0.01
0.02
0
"""
