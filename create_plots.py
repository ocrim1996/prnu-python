"""
@author: Mirco Ceccarelli (mirco.ceccarelli@stud.unifi.it)
@author: Francesco Argentieri (francesco.argentieri@stud.unifi.it)
Università degli Studi di Firenze 2021
"""

import numpy as np
from matplotlib import pyplot as plt


# Plots histograms with PCE values for each image
def create_histogram_plot(y_value, labels_value, device_name):
    x = [i for i in range(20)]
    labels = labels_value
    y = y_value

    plt.bar(x, height=y)
    plt.xticks(x, labels, rotation='vertical')

    # Pad margins so that markers don't get
    # clipped by the axes
    plt.margins(0.1)

    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.5)

    plt.xlabel("Image tested", labelpad=7)
    plt.ylabel("PCE", labelpad=7)
    plt.axhline(y=60, color='b', linestyle='--', label="Threshold")

    plt.title("PCE of " + str(device_name) + " with NoiseExtract")
    outpath = "/data/lesc/users/elaborato2/PRNULab/Plots/PolimiDataset/Histograms_with_NoiseExtract/"
    plot_name = outpath + "PCE_of_" + str(device_name)+".png"

    plt.savefig(plot_name)
    plt.show()


# Taken in input the true positive rate (tpr) and the false positive rate (fpr) prints the ROC curve.
def create_roc(tpr, fpr, title):
    plt.title('ROC Curve of ' + title + ' with DRUNet100')
    plt.plot(fpr, tpr, '-bo', mfc='none', label='20 nat images')
    plt.legend(loc='lower right')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate (TPR)')
    plt.xlabel('False Positive Rate (FPR)')
    plt.grid()
    outpath = "/data/lesc/users/elaborato2/PRNULab/Plots/reVISIONDataset/DRUNet100/"
    plot_name = outpath + "ROC Curve with DRUNet100.png"
    plt.savefig(plot_name)
    plt.show()


# Taken in input the true positive rate (tpr) and the false positive rate (fpr) prints the ROC curve for each device.
def create_roc_per_single_device(tpr, fpr, title, device):
    plt.title('ROC Curve of ' + title + ' with DRUNet100 of ' + device)
    plt.plot(fpr, tpr, '-bo', mfc='none', label='20 nat images')
    plt.legend(loc='lower right')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate (TPR)')
    plt.xlabel('False Positive Rate (FPR)')
    plt.grid()
    outpath = "/data/lesc/users/elaborato2/PRNULab/Plots/reVISIONDataset/DRUNet100/"
    plot_name = outpath + "ROC Curve with DRUNet100 of " + device + ".png"
    plt.savefig(plot_name)
    plt.show()


# 3 ROC Curves in a single plot.
def create_3_multiple_roc(tpr_list, fpr_list, title):
    plt.title('ROC Curve of ' + title + ' Comparison')
    line_style = ['-bo', '-ro', '-go']
    label_name = ['20 nat images (NoiseExtract)', '20 nat images (DRUNet15)', '20 nat images (DRUNet50)']
    for i in range(len(tpr_list)):
        plt.plot(fpr_list[i], tpr_list[i], line_style[i], mfc='none', label=label_name[i])
    plt.legend(loc='lower right')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate (TPR)')
    plt.xlabel('False Positive Rate (FPR)')
    plt.grid()
    outpath = "/data/lesc/users/elaborato2/PRNULab/Plots/reVISIONDataset/ROCMultiplePlots/"
    plot_name = outpath + "ROC Curve Comparison.png"
    plt.savefig(plot_name)
    plt.show()


# 4 ROC Curves in a single plot.
def create_4_multiple_roc(tpr_list, fpr_list, title):
    plt.title('4 ROC Curve of ' + title + ' Comparison')
    line_style = ['-b', '-r', '-g', '-y']
    label_name = ['20 nat images (NoiseExtract)', '20 nat images (DRUNet15)', '20 nat images (DRUNet50)',
                  '20 nat images (DRUNet100)']
    for i in range(len(tpr_list)):
        plt.plot(fpr_list[i], tpr_list[i], line_style[i], mfc='none', label=label_name[i])
    plt.legend(loc='lower right')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate (TPR)')
    plt.xlabel('False Positive Rate (FPR)')
    plt.grid()
    outpath = "/data/lesc/users/elaborato2/PRNULab/Plots/reVISIONDataset/ROCMultiplePlots/"
    plot_name = outpath + "4 ROC Curve Comparison 2.png"
    plt.savefig(plot_name)
    plt.show()


# Plots a graph with various statistics (TP, FP, TN, FN) for each device.
def create_boxplot(fingerprint_device, slice_arr, pce_rot, index_img):
    plt.title('BoxPlot with DRUNet100 ' + str(index_img))
    for i in range(len(fingerprint_device)):
        stop = (i+1) * len(pce_rot[0])
        start = stop - len(pce_rot[0])
        slice_arr_2 = slice_arr[start:stop]

        for elem in slice_arr_2:
            x = np.random.normal(i + 1, 0.1, size=1)
            if elem[1] in elem[0] and elem[2] >= 60:
                plt.plot(x, elem[2], 'g.')
            elif elem[1] in elem[0] and elem[2] < 60:
                plt.plot(x, elem[2], 'r.')
            elif elem[1] not in elem[0] and elem[2] >= 60:
                plt.plot(x, elem[2], 'r.')
            elif elem[1] not in elem[0] and elem[2] < 60:
                plt.plot(x, elem[2], 'g.')

    x_ticks = []
    x_labels = []

    for idx_dev, val_dev in enumerate(fingerprint_device):
        x_ticks.append(idx_dev+1)
        x_labels.append(val_dev)

    plt.axhline(y=60, color='b', linestyle='--', label="Threshold")
    plt.xticks(x_ticks, x_labels, rotation='vertical')
    plt.ylabel('PCE Value')
    plt.xlabel('Devices')
    plt.grid()
    outpath = "/data/lesc/users/elaborato2/PRNULab/Plots/reVISIONDataset/DRUNet100/"
    plot_name = outpath + "BoxPlot with DRUNet100 " + str(index_img) + ".png"
    plt.savefig(plot_name)
    plt.show()


# Creates arrays with the values of the statistics to then be used in the summary table.
def create_value_table(fingerprint_device, nat_image_name, arr_tot):
    TP = np.zeros((len(fingerprint_device),), dtype=int)
    FP = np.zeros((len(fingerprint_device),), dtype=int)
    TN = np.zeros((len(fingerprint_device),), dtype=int)
    FN = np.zeros((len(fingerprint_device),), dtype=int)
    TPR = np.zeros((len(fingerprint_device),), dtype=float)
    FPR = np.zeros((len(fingerprint_device),), dtype=float)

    for i in range(len(nat_image_name)):
        stop = (i+1) * len(nat_image_name)
        start = stop - len(nat_image_name)
        slice_arr_device = arr_tot[start:stop]
        for elem in slice_arr_device:
            if elem[1] in elem[0] and elem[2] >= 60:
                TP[i] = TP[i] + 1
            elif elem[1] in elem[0] and elem[2] < 60:
                FN[i] = FN[i] + 1
            elif elem[1] not in elem[0] and elem[2] >= 60:
                FP[i] = FP[i] + 1
            elif elem[1] not in elem[0] and elem[2] < 60:
                TN[i] = TN[i] + 1

    for i in range(len(fingerprint_device)):
        TPR[i] = float((TP[i])/(TP[i]+FN[i]))
        FPR[i] = float((FP[i])/(FP[i]+TN[i]))

    TPR = TPR.tolist()
    FPR = FPR.tolist()
    TP = TP.tolist()
    FP = FP.tolist()
    TN = TN.tolist()
    FN = FN.tolist()

    return TP, FP, TN, FN, TPR, FPR





