"""
@author: Mirco Ceccarelli (mirco.ceccarelli@stud.unifi.it)
@author: Francesco Argentieri (francesco.argentieri@stud.unifi.it)
Università degli Studi di Firenze 2021
"""

import numpy as np
import csv


# Write into csv file.
def write_into_csv(tpr, fpr, file_name):
    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(tpr)
        csv_writer.writerow(fpr)


# Read from csv file.
def read_from_csv(file_name):
    tpr = []
    fpr = []
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                for i in row:
                    tpr.append(float(i))
            elif idx == 1:
                for i in row:
                    fpr.append(float(i))
    tpr = np.asarray(tpr)
    fpr = np.asarray(fpr)
    return tpr, fpr


# Write into txt file.
def write_into_table_txt(table, file_name):
    with open(file_name, 'w') as f:
        f.write(table)
