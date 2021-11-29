# -*- coding: UTF-8 -*-
"""
@author: Mirco Ceccarelli (mirco.ceccarelli@stud.unifi.it)
@author: Francesco Argentieri (francesco.argentieri@stud.unifi.it)
Università degli Studi di Firenze 2021
"""
from multiprocessing import cpu_count, Pool
import numpy as np
from PIL import Image

import create_plots
import extract_path
import prnu
import utility_functions as uf
from tabulate import tabulate


def main():
    """
    Main example script. Load a subset of flatfield and natural images from a dataset.
    For each device compute the fingerprint from all the flatfield images.
    For each natural image compute the noise residual.
    Check the detection performance obtained with cross-correlation and PCE
    :return:
    """

    # To use the Polimi dataset.
    #ff_dirlist, ff_device, nat_dirlist, nat_device, nat_image_name, fingerprint_device = extract_path.extract_path_polimi()

    # To use the reVISION dataset.
    ff_dirlist, ff_device, nat_dirlist, nat_device, nat_image_name, fingerprint_device = extract_path.extract_path_revision()

    k = []
    for device in fingerprint_device:
        imgs = []
        for img_path in ff_dirlist[ff_device == device]:
            im = Image.open(img_path)
            im_arr = np.asarray(im)
            if im_arr.dtype != np.uint8:
                print('Error while reading image: {}'.format(img_path))
                continue
            if im_arr.ndim != 3:
                print('Image is not RGB: {}'.format(img_path))
                continue
            im_cut = prnu.cut_ctr(im_arr, (512, 512, 3))
            imgs += [im_cut]
        # First noise extraction to compute the fingerprint from all flat-field images.
        k += [prnu.extract_multiple_aligned(imgs, processes=cpu_count())]

    k = np.stack(k, 0)

    print("*"*100)
    print('Computing residuals')

    imgs = []
    for img_path in nat_dirlist:
        print("img_path: ", img_path)
        imgs += [prnu.cut_ctr(np.asarray(Image.open(img_path)), (512, 512, 3))]

    pool = Pool(cpu_count())
    # Second noise extraction to compute the residual noise for each natural images.
    w = pool.map(prnu.extract_single, imgs)
    pool.close()

    w = np.stack(w, 0)

    # Computing Ground Truth
    gt = prnu.gt(fingerprint_device, nat_device)
    print("*" * 100)

    print('Computing cross correlation')
    cc_aligned_rot = prnu.aligned_cc(k, w)['cc']

    print('Computing statistics cross correlation')
    stats_cc = prnu.stats(cc_aligned_rot, gt)

    print('Computing PCE')
    pce_rot = np.zeros((len(fingerprint_device), len(nat_device)))

    for fingerprint_idx, fingerprint_k in enumerate(k):
        for natural_idx, natural_w in enumerate(w):
            cc2d = prnu.crosscorr_2d(fingerprint_k, natural_w)
            pce_rot[fingerprint_idx, natural_idx] = prnu.pce(cc2d)['pce']

    print("pce_rot: ", pce_rot)
    print(len(pce_rot))

    print('Computing statistics on PCE')
    stats_pce = prnu.stats(pce_rot, gt)

    print('AUC on CC {:.2f}, expected {:.2f}'.format(stats_cc['auc'], 0.98))
    print('AUC on PCE {:.2f}, expected {:.2f}'.format(stats_pce['auc'], 0.81))

    # True Positive Rate (TPR) PCE
    print("True Positive Rate (PCE): {}".format(stats_pce["tpr"]))
    # False Positive Rate (FPR) PCE
    print("False Positive Rate (PCE): {}".format(stats_pce["fpr"]))
    # Threshold (PCE)
    print("Threshold (PCE): {}".format(stats_pce["th"]))

    # Plots a single ROC curve per device.
    for idx, value in enumerate(pce_rot):
        stats_pce_single_device = prnu.stats(value, gt[idx])
        auc_per_single_device = round(stats_pce_single_device["auc"], 2)
        plot_title = "PCE (AUC: " + str(auc_per_single_device) + ")"
        create_plots.create_roc_per_single_device(stats_pce_single_device["tpr"], stats_pce_single_device["fpr"], plot_title, fingerprint_device[idx])

    # Write tpr/fpr results in csv file.
    uf.write_into_csv(stats_pce["tpr"], stats_pce["fpr"], "Plots/reVISIONDataset/DRUNet100/DRUNet100Rate.csv")

    # Plots PCE Histograms for each device (Use it only for Polimi dataset, because there are fewer images)
    """
    print('Computing Histograms')
    pce_values = pce_rot.tolist()
    nat_image_name = nat_image_name.tolist()
    for idx, value in enumerate(fingerprint_device):
        create_histograms.create_histogram_plot(pce_values[idx], nat_image_name, value)
    """

    # Plots general ROC curve.
    create_plots.create_roc(stats_pce["tpr"], stats_pce["fpr"], "PCE")

    arr_tot = []
    for idx, device in enumerate(fingerprint_device):
        for index in range(len(pce_rot[0])):
            tripletta = [nat_image_name[index], device, pce_rot[idx][index]]
            arr_tot.append(tripletta)

    # Calculates statistics: True Positive, False Positive, True Negative and False Negative and their respective rates.
    # Next all these data are inserted in a table.
    statistics_table = []
    TP, FP, TN, FN, TPR, FPR = create_plots.create_value_table(fingerprint_device, nat_image_name, arr_tot)
    for i in range(len(fingerprint_device)):
        six_tuple = [fingerprint_device[i], TP[i], FP[i], TN[i], FN[i], TPR[i], FPR[i]]
        statistics_table.append(six_tuple)
    table = tabulate(statistics_table, headers=["Device", "TP", "FP", "TN", "FN", "TPR", "FPR"], tablefmt='fancy_grid')
    uf.write_into_table_txt(table, "Plots/reVISIONDataset/DRUNet100/DRUNet100Table.txt")
    print(table)

    # Given the quantity of devices, plots are divided into multiple graphics.
    num_plot = 4
    num_dev_per_plot = int(len(fingerprint_device)/num_plot)

    for i in range(num_plot):
        # Divides fingerprint device array.
        stop = (i+1) * num_dev_per_plot
        start = stop - num_dev_per_plot
        fing_device_slice_arr = fingerprint_device[start:stop]

        # Divide array tot (triplette)
        stop = (i+1) * num_dev_per_plot * len(pce_rot[0])
        start = stop - (num_dev_per_plot * len(pce_rot[0]))
        slice_arr = arr_tot[start:stop]

        create_plots.create_boxplot(fing_device_slice_arr, slice_arr, pce_rot, i)


if __name__ == '__main__':
    main()
