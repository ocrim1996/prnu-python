

# PRNU extraction via denoiser based on convolutional neural network (DRUNet)

[![Python](https://img.shields.io/badge/Python-3.8.10-green?style=plastic)](https://www.python.org/downloads/release/python-3810/)
[![Numpy](https://img.shields.io/badge/Numpy-1.21.1-orange?style=plastic)](https://pypi.org/project/numpy/)
[![Pillow](https://img.shields.io/badge/Pillow-7.0-red?style=plastic)](https://pypi.org/project/Pillow/)
[![SciPy](https://img.shields.io/badge/Scipy-1.7.1-9cf?style=plastic)](https://pypi.org/project/scipy/)
[![ScikitLearn](https://img.shields.io/badge/ScikitLearn-1.0.1-9cf?style=plastic)](https://pypi.org/project/scikit-learn/)
[![Opencv-Python](https://img.shields.io/badge/Opencv-4.5.3.56-success?style=plastic)](https://pypi.org/project/opencv-python/)
[![Torch](https://img.shields.io/badge/Torch-1.9.1-success?style=plastic)](https://pypi.org/project/torch/)
[![MIT License](https://img.shields.io/badge/License-MIT-blueviolet?style=plastic)](https://opensource.org/licenses/mit-license.php)


# Image Processing and Security
<p align="center">
    <img src="https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/50B32844-863A-4BD6-BEF0-752499782CF9/AEC4710F-EA46-427A-AD8C-8ADECECC3A92_2/LogoUnifi.png" alt="drawing" width="100"/>
</p>

## Authors
- **Mirco Ceccarelli**
- **Francesco Argentieri**

## Relators
- **Prof. Alessandro Piva**
- **Dott. Dasara Shullani**
- **Dott. Daniele Baracchi**

## Introduction
In this project we have dealt with a branch of the **Multimedia Forensics**: ***Device Identification*** (know what device has taken a photo).

![DeviceIdentification](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/50B32844-863A-4BD6-BEF0-752499782CF9/587EC1A1-FBAD-42F4-ADF0-AD8EF305C34E_2/DeviceIdentifcation.png)

In order to do this, a noise that is introduced by the sensors of each digital camera, is exploited: the **PRNU** (Photo Response Non Uniformity), which is different for each individual device.

Here below a brief scheme of the *Device Identification* process via **PRNU**:
![DeviceIdentification](https://res.craft.do/user/full/63cec524-c1b6-57b4-8157-df0476f848cb/doc/50B32844-863A-4BD6-BEF0-752499782CF9/9A27C2CD-8046-4155-898A-F7CD270603D4_2/Fasi%20dellestrazione%20del%20PRNU.png)

## Settings
Before running the code, set up the project correctly.
Click here: [model_zoo](model_zoo)

In the `prnu/functions.py` file is used the Noise Extract method of DRUNet, if you want to use the Polimi Noise Extract method you need to comment some lines of code.

## To Run
```angular2html
python3 example.py
```


