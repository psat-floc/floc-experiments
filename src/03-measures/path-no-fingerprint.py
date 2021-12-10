import sys
import pandas as pd
import csv
from collections import Counter

#0 = id
#1 = 1995
#25 = 2019



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

for years in counter:
    nb_identified_users = 0

    for key in counter[years]:
        if(counter[years][key] == 1):
            nb_identified_users += 1
        
    avg = (nb_identified_users / len_data) * 100
    print(years + ": " + str(avg))

"""
    years_averages = []
    # min = 0 (for 1 year), max = 24 (for 25 years) 
    for nb_years in range(0, 25):
        average = 0

        # Prepare the csv file for each test
        for year in range(1, 26 - nb_years) :
            tab_concat = []
            for user in range(0, len_data) :
                c = ""
                for k in range(0, nb_years+1):
                    c += str(data[user][year+k])
                tab_concat.append(c)

            counter = Counter(tab_concat)
            
            nb_of_identified_users = 0
            
            for key in counter:
                if(counter[key] == 1):
                    nb_of_identified_users += 1
            
            average += nb_of_identified_users 
            #print('y = '+ str(nb_years) + ' et unique = '+ str(nb_of_identified_users))
            
            #ecriture sur le fichier csv
        
        year_average = (average/(162541*(25-nb_years)))*100
        years_averages.append(year_average)
        print("moyenne d'utilisateur unique sur une periode de", nb_years+1, "ans :", year_average )
        print(counter["0x0"])

    # Prepare the global average csv file 
    fichier2 = open("processed_data/results_averages_"+str(nb_bits)+"bits.csv", "w",newline='')
    writer2 = csv.writer(fichier2)
    for y in range(0, 25):
        writer2.writerow([y+1, years_averages[y]])
        """
