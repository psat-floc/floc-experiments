import pandas as pd
import csv
from collections import Counter

#0 = id
#1 = 1995
#25 = 2019

for nb_bits in range(8,9):
    data = pd.read_csv('processed_data/all_cohorts_'+str(nb_bits)+'.csv', header=0).to_numpy()
    len_data = len(data)

    years_averages = []
    for y in range(0, 25):
        average = 0
        nb_years = y # min = 0 (for 1 year), max = 24 (for 25 years) 
        tab_all_concat = []

        # Prepare the csv file for each test
        fichier = open("processed_data/results_"+str(nb_years+1)+"_years_"+str(nb_bits)+"bits.csv", "w",newline='')
        writer = csv.writer(fichier)
        for j in range(1, 26 - nb_years) :
            tab_concat = []
            for i in range(0, len_data) :
                c = ""
                for k in range(0, nb_years+1):
                    c += str(data[i][j+k])
                tab_concat.append(c)

            counter = Counter(tab_concat)
            
            nb_of_identified_users = 0
            
            for key in counter:
                if(counter[key] == 1):
                    nb_of_identified_users += 1
            
            average += nb_of_identified_users 
            #print('y = '+ str(nb_years) + ' et unique = '+ str(nb_of_identified_users))
            
            #ecriture sur le fichier csv
            writer.writerow([str(j+1994)+' - '+str(j+1994+nb_years), nb_of_identified_users/162541*100])
        
        year_average = (average/(162541*(25-nb_years)))*100
        years_averages.append(year_average)
        print("moyenne d'utilisateur unique sur une periode de", nb_years+1, "ans :", year_average )
        print(counter['0x00x00x00x00x00x00x00x00x00x0'])

    # Prepare the global average csv file 
    fichier2 = open("results_averages_"+str(nb_bits)+"bits.csv", "w",newline='')
    writer2 = csv.writer(fichier2)
    for y in range(0, 25):
        writer2.writerow([y+1, years_averages[y]])
