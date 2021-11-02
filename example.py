# -*- coding: UTF-8 -*-
"""
@author: Luca Bondi (luca.bondi@polimi.it)
@author: Paolo Bestagini (paolo.bestagini@polimi.it)
@author: Nicolò Bonettini (nicolo.bonettini@polimi.it)
Politecnico di Milano 2018
"""

import os
from glob import glob
from multiprocessing import cpu_count, Pool

import numpy as np
from PIL import Image
import create_histograms

import prnu


def main():
    """
    Main example script. Load a subset of flatfield and natural images from Dresden.
    For each device compute the fingerprint from all the flatfield images.
    For each natural image compute the noise residual.
    Check the detection performance obtained with cross-correlation and PCE
    :return:
    """
    ff_dirlist = np.array(sorted(glob('test/data/ff-jpg/*.JPG')))
    ff_device = np.array([os.path.split(i)[1].rsplit('_', 1)[0] for i in ff_dirlist])

    nat_dirlist = np.array(sorted(glob('test/data/nat-jpg/*.JPG')))
    print("NAT dir-list: ", nat_dirlist)
    nat_device = np.array([os.path.split(i)[1].rsplit('_', 1)[0] for i in nat_dirlist])

    nat_image_name = np.array([os.path.split(i)[1] for i in nat_dirlist])
    print("NAT image name: ", nat_image_name)

    print('Computing fingerprints')
    fingerprint_device = sorted(np.unique(ff_device))
    print("NAT device without repetition: ", fingerprint_device)

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
        # 1° noise_extract
        k += [prnu.extract_multiple_aligned(imgs, processes=cpu_count())]

    k = np.stack(k, 0)

    print('Computing residuals')

    imgs = []
    for img_path in nat_dirlist:
        print("-"*50 + "COMPUTING RESIDUALS" + "-"*100)
        print("img_path: ", img_path)
        # Roba per il print
        prova = Image.open(img_path)
        prova2 = np.asarray(prova)
        #print("Questo è prova2: ", prova2)
        prova3 = prnu.cut_ctr(prova2, (512, 512, 3))
        #print("Questo è prova3: ", prova3)
        imgs += [prova3]

    pool = Pool(cpu_count())
    # 2° noise_extract
    print("*"*50 + "SECONDO NOISE EXTRACT" + "*"*100)
    w = pool.map(prnu.extract_single, imgs)
    pool.close()

    w = np.stack(w, 0)

    # Computing Ground Truth
    gt = prnu.gt(fingerprint_device, nat_device)

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

    print('Computing statistics on PCE')
    stats_pce = prnu.stats(pce_rot, gt)
    print('AUC on CC {:.2f}, expected {:.2f}'.format(stats_cc['auc'], 0.98))
    print('AUC on PCE {:.2f}, expected {:.2f}'.format(stats_pce['auc'], 0.81))

    """
    print('Computing Histograms')
    pce_values = pce_rot.tolist()
    nat_image_name = nat_image_name.tolist()
    for idx, value in enumerate(fingerprint_device):
        create_histograms.create_histogram_plot(pce_values[idx], nat_image_name, value)
    """


if __name__ == '__main__':
    main()
