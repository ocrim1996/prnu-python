"""
@author: Mirco Ceccarelli (mirco.ceccarelli@stud.unifi.it)
@author: Francesco Argentieri (francesco.argentieri@stud.unifi.it)
Università degli Studi di Firenze 2021
"""

import utility_functions as uf
import numpy as np
import create_plots as ch

# Script to print 3 plots in a single graph.
"""
tpr_EN, fpr_EN = uf.read_from_csv("Plots/NoiseExtract/NoiseExtractRate.csv")
tpr_DRU15, fpr_DRU15 = uf.read_from_csv("Plots/DRUNet15/DRUNet15Rate.csv")
tpr_DRU50, fpr_DRU50 = uf.read_from_csv("Plots/DRUNet50/DRUNet50Rate.csv")

tpr_list = [tpr_EN.tolist(), tpr_DRU15.tolist(), tpr_DRU50.tolist()]
fpr_list = [fpr_EN.tolist(), fpr_DRU15.tolist(), fpr_DRU50.tolist()]

tpr_list = np.asarray(tpr_list, dtype=object)
fpr_list = np.asarray(fpr_list, dtype=object)

ch.create_multiple_roc(tpr_list, fpr_list, "PCE")
"""

# Script to print 4 plots in a single graph.
tpr_EN, fpr_EN = uf.read_from_csv("Plots/NoiseExtract/NoiseExtractRate.csv")
tpr_DRU15, fpr_DRU15 = uf.read_from_csv("Plots/DRUNet15/DRUNet15Rate.csv")
tpr_DRU50, fpr_DRU50 = uf.read_from_csv("Plots/DRUNet50/DRUNet50Rate.csv")
tpr_DRU100, fpr_DRU100 = uf.read_from_csv("Plots/DRUNet100DRUNet100/DRUNet100Rate.csv")


tpr_list = [tpr_EN.tolist(), tpr_DRU15.tolist(), tpr_DRU50.tolist(), tpr_DRU100.tolist()]
fpr_list = [fpr_EN.tolist(), fpr_DRU15.tolist(), fpr_DRU50.tolist(), fpr_DRU100.tolist()]

tpr_list = np.asarray(tpr_list, dtype=object)
fpr_list = np.asarray(fpr_list, dtype=object)

ch.create_4_multiple_roc(tpr_list, fpr_list, "PCE")

