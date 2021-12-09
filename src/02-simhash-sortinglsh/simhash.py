from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from floc_simhash import SimHashTransformer
from random import gauss

import numpy as np
import pandas as pd
import csv
import sys

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
nb_users = int(sys.argv[2])
nb_bits = int(sys.argv[3])


print(filename)
ratings = pd.read_csv(filename, header = 0)

size = len(ratings)
# user/movie array
arr_vecs = np.zeros((size,22))

# user array (meaned)
arr_users = np.zeros((nb_users+1,23))



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

    # print(arr_vecs[index])

# for each user: average his vectors
   
for arr_vec in arr_vecs:
    index = int(arr_vec[0])

    arr_users[index][3] += arr_vec[3]
    arr_users[index][4] += arr_vec[4]
    arr_users[index][5] += arr_vec[5]
    arr_users[index][6] += arr_vec[6]
    arr_users[index][7] += arr_vec[7]
    arr_users[index][8] += arr_vec[8]
    arr_users[index][9] += arr_vec[9]
    arr_users[index][10] += arr_vec[10]
    arr_users[index][11] += arr_vec[11]
    arr_users[index][12] += arr_vec[12]
    arr_users[index][13] += arr_vec[13]
    arr_users[index][14] += arr_vec[14]
    arr_users[index][15] += arr_vec[15]
    arr_users[index][16] += arr_vec[16]
    arr_users[index][17] += arr_vec[17]
    arr_users[index][18] += arr_vec[18]
    arr_users[index][19] += arr_vec[19]
    arr_users[index][20] += arr_vec[20]
    arr_users[index][21] += arr_vec[21]

    arr_users[index][22] += 1

# enlevage de la premiere colonne (juste les titres)
arr_users = arr_users[1:, :]

# average of user interests
for user in arr_users:
    if user[22] != 0:
        user[3:21] /= user[22]

# creation of p-bit vectors (p vectors of size 19)
# first: white paper proposes 8 bits
pbit_vec = np.zeros((nb_bits, 19)) 

for i in range(nb_bits):
    pbit_vec[i] = make_rand_vector(19) 

# x is the d-dimensional simhash takes as input
x = arr_users[:, 3:22]

# compute simhash according to google's white paper
h = ["" for i in range(nb_users)]

for i in range(nb_users):
    for j in range(nb_bits):
        h[i] += "0" if np.dot(x[i], pbit_vec[j]) <= 0 else "1"

# printing
# for i in range(nb_users):
#     print(h[i])

year = filename[-8:-4]
print(year)
yearCohorts = []
yearCohorts.append(['id',year])
for i in range(nb_users):
    #print(hex(int(h[i], 2)))
    yearCohorts.append([i+1,int(h[i], 2)])

writer = csv.writer(open('processed_data/simhash_'+str(nb_bits)+'_'+year+'.csv', 'w',newline=''))
writer.writerows(yearCohorts)


# SortingLSH
print("Applying SortingLSH...")

def anonymityCheck(cohorts, k):
    """ Check if each cohort appears at least k times """
    hashes = dict()
    for i in range(len(cohorts)):
        if cohorts[i] in hashes.keys():
            hashes[cohorts[i]] += 1
        else:
            hashes[cohorts[i]] = 1
    minimum = len(cohorts) + 1
    for i in hashes:
        if minimum >= hashes[i]:
            minimum = hashes[i]
    return minimum >= k

while (not anonymityCheck(h, 2)) and (len(h) > 1):
    for i in range(len(h)):
        h[i] = h[i][0:-1]

print("Cohorts are now encoded on", len(h[0]), "bits")


yearCohorts = []
yearCohorts.append(['id',year])
for i in range(nb_users):
    #print(hex(int(h[i], 2)))
    yearCohorts.append([i+1,int(h[i], 2)])

writer = csv.writer(open('processed_data/sortinglsh_'+str(nb_bits)+'_'+year+'.csv', 'w',newline=''))
writer.writerows(yearCohorts)
