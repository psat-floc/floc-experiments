import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import csv
sns.set()
from sklearn.cluster import KMeans

nb_bits = sys.argv[1]
filename_nb_cohorts = "processed_data_knn/nb_cohorts_simhash_" + str(nb_bits) + ".csv"
data_nb_cohorts = pd.read_csv(filename_nb_cohorts, header=None).to_numpy()

for year in range(1995, 2020):
    print(year)
    filename = "processed_data_knn/intermediary_data_" + str(year) + ".csv"
    data = pd.read_csv(filename, header=None).to_numpy()
    len_data = len(data)
    non_empty_data = []
    non_empty_data_with_id = []
    for i in range(len_data) :
        empty = True
        for j in range(len(data[i])) :
            if(data[i][j] != 0) :
                empty = False
        if(not empty) :
            non_empty_data.append(data[i])
            non_empty_data_with_id.append(np.insert(data[i], 0, i))

    filename_output = "processed_data_knn/cohorts_knn_" + str(nb_bits) + "_" + str(year) + ".csv"
    file_output = open(filename_output, "w", newline='')
    output_writer = csv.writer(file_output)
    output_writer.writerow(['user_id', 'cluster'])
    # On demande le même nombre de clusters que ce que simhash nous avait donné
    nb_clusters = data_nb_cohorts[year - 1995][1]
    kmeans = KMeans(nb_clusters)
    kmeans.fit(non_empty_data)
    identified_clusters = kmeans.fit_predict(non_empty_data)
    for i in range(len(non_empty_data_with_id)):
        non_empty_data_with_id[i] = np.append(non_empty_data_with_id[i], identified_clusters[i])
        output_writer.writerow([int(non_empty_data_with_id[i][0]), int(non_empty_data_with_id[i][-1])])
