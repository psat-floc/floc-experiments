import pandas as pd
import csv
from collections import Counter

#0 = id
#1 = 1996
#2 = 1997
#3 = 1998
#4 = 1999
#5 = 2000
#6 = 2001
#7 = 2002
#8 = 2003
#9 = 2004
#10 = 2005
#11 = 2006
#12 = 2007
#13 = 2008
#14 = 2009
#15 = 2010
#16 = 2011
#17 = 2012
#18 = 2013
#19 = 2014
#20 = 2015
#21 = 2016
#22 = 2017
#23 = 2018
#24 = Navigateur

data = pd.read_csv('processed_data/all_cohorts_8.csv', header=0).to_numpy()
len_data = len(data)

years_averages = []
for y in range(0, 23):
    average = 0
    nb_years = y # min = 0 (for 1 year), max = 22 (for 23 years) 
    tab_all_concat = []

    # Prepare the csv file for each test
    for j in range(2, 25 - nb_years) :
        tab_concat = []
        for i in range(0, len_data) :
            c = ""
            c += str(data[i][1])
            for k in range(0, nb_years+1):
                c += str(data[i][j+k])
            tab_concat.append(c)
        counter = Counter(tab_concat)

        nb_of_identified_users = 0
        
        for key in counter:
            if(counter[key] == 1):
                nb_of_identified_users += 1
        
        average += nb_of_identified_users 
        #print(j+1995, ' - ', j+1995+nb_years, ': ', nb_of_identified_users/138493*100, '%')
        #ecriture sur le fichier csv

    year_average = average/(138493*(23-nb_years))*100
    years_averages.append(year_average)
    #print("moyenne d'utilisateur unique sur une periode de", nb_years+1, "ans :", year_average )

# Prepare the global average csv file 
fichier2 = open("processed_data/results_averages_8bits_fingerprint.csv", "w",newline='')
writer2 = csv.writer(fichier2)
for y in range(0, 23):
    writer2.writerow([y+1, years_averages[y]])
