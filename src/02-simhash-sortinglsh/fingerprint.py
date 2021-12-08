import numpy as np
import pandas as pd
import csv
from random import choices
import sys

data = pd.read_csv(sys.argv[1], header=0).to_numpy()
len_data = len(data)
fingerprints = ["Chrome", "Safari", "Edge", "Firefox", "Samsung Internet", "Opera", "Others"]
weights = [0.6467, 0.1906, 0.0410, 0.0366, 0.0281, 0.0236, 0.0334]
fichier = open(sys.argv[1][:-4] + "_fingerprint.csv", "w")
writer = csv.writer(fichier)
writer.writerow(['id','browser','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'])

for i in range(0, len_data) :
    browser = choices(fingerprints, weights)
    new_data = np.insert(data[i], 1, browser)
    writer.writerow(new_data)
