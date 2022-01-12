from random import gauss

import numpy as np
import pandas as pd
import csv
import sys
from os.path import exists

# Action, Adventure, Animation, Children's, Comedy, Crime, Documentary,
# Drama, Fantasy, Film-Noir, Horror, Musical, Mystery, Romance, Sci-Fi,
# Thriller, War, Western, No genres listed
# => 19 dimensions


# random vector creation
# https://stackoverflow.com/a/8453514
def make_rand_vector(dims):
    vec = [gauss(0, 1) for i in range(dims)]
    mag = sum(x**2 for x in vec) ** .5
    return [x/mag for x in vec]

# Parametres d'entrée : filename(years.csv(exp:1999.csv), nb_users, nb_bits)
filename = sys.argv[1]
nb_users = int(sys.argv[2]) + 1
nb_bits = int(sys.argv[3])

def load_ratings(filename, nb_users):

    print(filename)
    ratings = pd.read_csv(filename, header = 0)

    size = len(ratings)
    # user/movie array
    arr_vecs = np.zeros((size,22))

    # user array
    arr_users = np.zeros((nb_users,20))

    # ajout du genre de chaque film au dataframe movies
    for index, row in ratings.iterrows():
        arr_vecs[index][0] = row['userId']
        arr_vecs[index][1] = row['movieId']
        arr_vecs[index][2] = row['timestamp']

        genres = row['genres'].split("|")
        rating = row['rating']

        for genre in genres:
            if genre == 'Action':
                arr_vecs[index][3] = rating
            if genre == 'Adventure':
                arr_vecs[index][4] = rating
            if genre == 'Animation':
                arr_vecs[index][5] = rating
            if genre == 'Children\'s':
                arr_vecs[index][6] = rating
            if genre == 'Comedy':
                arr_vecs[index][7] = rating
            if genre == 'Crime':
                arr_vecs[index][8] = rating
            if genre == 'Documentary':
                arr_vecs[index][9] = rating
            if genre == 'Drama':
                arr_vecs[index][10] = rating
            if genre == 'Fantasy':
                arr_vecs[index][11] = rating
            if genre == 'Film-Noir':
                arr_vecs[index][12] = rating
            if genre == 'Horror':
                arr_vecs[index][13] = rating
            if genre == 'Musical':
                arr_vecs[index][14] = rating
            if genre == 'Mystery':
                arr_vecs[index][15] = rating
            if genre == 'Romance':
                arr_vecs[index][16] = rating
            if genre == 'Sci-Fi':
                arr_vecs[index][17] = rating
            if genre == 'Thriller':
                arr_vecs[index][18] = rating
            if genre == 'War':
                arr_vecs[index][19] = rating
            if genre == 'Western':
                arr_vecs[index][20] = rating
            if genre == '(no':
                arr_vecs[index][21] = rating

    # for each user: average his vectors
    for arr_vec in arr_vecs:
        index = int(arr_vec[0])

        arr_users[index][0] += arr_vec[3]
        arr_users[index][1] += arr_vec[4]
        arr_users[index][2] += arr_vec[5]
        arr_users[index][3] += arr_vec[6]
        arr_users[index][4] += arr_vec[7]
        arr_users[index][5] += arr_vec[8]
        arr_users[index][6] += arr_vec[9]
        arr_users[index][7] += arr_vec[10]
        arr_users[index][8] += arr_vec[11]
        arr_users[index][9] += arr_vec[12]
        arr_users[index][10] += arr_vec[13]
        arr_users[index][11] += arr_vec[14]
        arr_users[index][12] += arr_vec[15]
        arr_users[index][13] += arr_vec[16]
        arr_users[index][14] += arr_vec[17]
        arr_users[index][15] += arr_vec[18]
        arr_users[index][16] += arr_vec[19]
        arr_users[index][17] += arr_vec[20]
        arr_users[index][18] += arr_vec[21]

        arr_users[index][19] += 1

    # enlevage de la premiere colonne (juste les titres)
    # arr_users = arr_users[1:, :]

    year = filename[-8:-4]

    # average of user interests
    intermediaryName = "processed_data/intermediary_data_" + str(year) + ".csv"
    intermediary_file = open(intermediaryName, "w",newline='')
    intermediary_writer = csv.writer(intermediary_file)
    
    for user in arr_users:
        if user[19] != 0:
            user[0:18] /= user[19]
            user[0:18] -= user[0:18].mean()

        intermediary_writer.writerow(user)

    return arr_users


year = filename[-8:-4]
interFile = "processed_data/intermediary_data_" + str(year) + ".csv"
arr_users = []

if exists(interFile):
    arr_users = pd.read_csv(interFile, header = None).to_numpy()
else:
    arr_users = load_ratings(filename, nb_users)


# creation of p-bit vectors (p vectors of size 19)
# first: white paper proposes 8 bits
pbit_vec = np.zeros((nb_bits, 19)) 

for i in range(nb_bits):
    pbit_vec[i] = make_rand_vector(19) 

# x is the d-dimensional simhash takes as input
x = arr_users[:, 0:19]

# compute simhash according to google's white paper
h = ["" for i in range(nb_users)]

for i in range(nb_users):
    for j in range(nb_bits):
        h[i] += "0" if np.dot(x[i], pbit_vec[j]) <= 0 else "1"

# printing
# for i in range(nb_users):
#     print(h[i])

yearCohorts = []
yearCohorts.append(['id',year])
for i in range(nb_users):
    # print(hex(int(h[i], 2)))
    # yearCohorts.append([i+1,int(h[i], 2)])
    yearCohorts.append([i+1,(hex(int(h[i], 2)))])

writer = csv.writer(open('processed_data/simhash_'+str(nb_bits)+'_'+year+'.csv', 'w',newline=''))
writer.writerows(yearCohorts)

# SortingLSH

cohorts = [[i, h[i]] for i in range(nb_users)]

# sort hashes

sorted_cohorts = sorted(cohorts, key=lambda x: x[1])

# this value sets the minimal amount of users per cohort
k = 5

cohort_int = 1
nb_users_in_cohort = 0

for i in range(nb_users):
    # cas de la fin du tableau, les derniers k - 1 elements doivent appartenir
    # a la meme cohorte pour ne pas se retrouver avec une cohorte < k
    if i >= nb_users - k + 1:
        sorted_cohorts[i].append(cohort_int)

    else:
        if nb_users_in_cohort < k:
            sorted_cohorts[i].append(cohort_int)
            nb_users_in_cohort += 1

        else:
            # si l'utilisateur précédent a le mm hash
            if sorted_cohorts[i][1] == sorted_cohorts[i-1][1]:
                sorted_cohorts[i].append(cohort_int)
            # sinon
            else:
                cohort_int += 1
                nb_users_in_cohort = 1
                sorted_cohorts[i].append(cohort_int)

yearCohorts = []
yearCohorts.append(['id',year])

sorted_cohorts = sorted(cohorts, key=lambda x: x[0])

for i in range(nb_users):
    yearCohorts.append([sorted_cohorts[i][0] + 1,hex(sorted_cohorts[i][2])])

writer = csv.writer(open('processed_data/sortinglsh_'+str(nb_bits)+'_'+year+'.csv', 'w',newline=''))
writer.writerows(yearCohorts)

