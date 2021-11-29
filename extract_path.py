"""
@author: Mirco Ceccarelli (mirco.ceccarelli@stud.unifi.it)
@author: Francesco Argentieri (francesco.argentieri@stud.unifi.it)
Università degli Studi di Firenze 2021
"""

import os
from glob import glob
import numpy as np


def extract_path_polimi():
    ff_dirlist = np.array(sorted(glob('test/data/ff-jpg/*.JPG')))
    ff_device = np.array([os.path.split(i)[1].rsplit('_', 1)[0] for i in ff_dirlist])

    nat_dirlist = np.array(sorted(glob('test/data/nat-jpg/*.JPG')))
    #print("NAT dir-list: ", nat_dirlist)
    nat_device = np.array([os.path.split(i)[1].rsplit('_', 1)[0] for i in nat_dirlist])

    nat_image_name = np.array([os.path.split(i)[1] for i in nat_dirlist])
    #print("NAT image name: ", nat_image_name)

    print("-" * 100)
    print('Computing fingerprints')
    fingerprint_device = sorted(np.unique(ff_device))
    #print("NAT device without repetition: ", fingerprint_device)

    return ff_dirlist, ff_device, nat_dirlist, nat_device, nat_image_name, fingerprint_device


def extract_path_revision():
    devices = ["D01_Samsung_GalaxyS3Mini", "D02_Apple_iPhone4s", "D05_Apple_iPhone5c", "D06_Apple_iPhone6",
               "D08_Samsung_GalaxyTab3", "D09_Apple_iPhone4", "D10_Apple_iPhone4s", "D11_Samsung_GalaxyS3",
               "D12_Sony_XperiaZ1Compact", "D13_Apple_iPad2", "D14_Apple_iPhone5c", "D15_Apple_iPhone6",
               "D16_Huawei_P9Lite", "D17_Microsoft_Lumia640LTE", "D18_Apple_iPhone5c", "D19_Apple_iPhone6Plus",
               "D20_Apple_iPadMini", "D21_Wiko_Ridge4G", "D22_Samsung_GalaxyTrendPlus", "D23_Asus_Zenfone2Laser",
               "D24_Xiaomi_RedmiNote3", "D25_OnePlus_A3000", "D26_Samsung_GalaxyS3Mini", "D27_Samsung_GalaxyS5",
               "D28_Huawei_P8", "D29_Apple_iPhone5", "D30_Huawei_Honor5c", "D31_Samsung_GalaxyS4Mini",
               "D32_OnePlus_A3003", "D33_Huawei_Ascend", "D34_Apple_iPhone5", "D35_Samsung_GalaxyTabA"]

    ff_dirlist = []
    nat_dirlist = []

    for device in devices:
        # Flat Images Dir
        flat_variable_path = "/images/images/forensic_datasets/VISION_dataset/reVISION_dataset_base/{}/images/flat/*.jpg".format(device)
        flat_image_dirlist = sorted(glob(flat_variable_path))
        flat_image_dirlist = flat_image_dirlist[:50]
        ff_dirlist.extend(flat_image_dirlist)

        # Nat Images Dir
        nat_variable_path = "/images/images/forensic_datasets/VISION_dataset/reVISION_dataset_base/{}/images/nat/*.jpg".format(device)
        nat_image_dirlist = sorted(glob(nat_variable_path))
        nat_image_dirlist = nat_image_dirlist[:20]
        nat_dirlist.extend(nat_image_dirlist)

    ff_dirlist = np.array(ff_dirlist)
    #print("FF Dirlist: ", ff_dirlist)
    nat_dirlist = np.array(nat_dirlist)
    #print("Nat Dirlist: ", nat_dirlist)

    # Flat Images Device
    ff_device = np.array([os.path.split(i)[1].rsplit('_', 3)[0] for i in ff_dirlist])
    #print("Flat Images Device: ", ff_device)

    # Nat Images Device
    nat_device = np.array([os.path.split(i)[1].rsplit('_', 3)[0] for i in nat_dirlist])
    #print("Nat Images Device: ", nat_device)

    # Nat Image Name
    nat_image_name = np.array([os.path.split(i)[1] for i in nat_dirlist])
    #print("NAT image name: ", nat_image_name)

    print("*"*100)
    print('Computing fingerprints')
    fingerprint_device = sorted(np.unique(ff_device))
    #print("Flat Device without repetition: ", fingerprint_device)

    return ff_dirlist, ff_device, nat_dirlist, nat_device, nat_image_name, fingerprint_device

