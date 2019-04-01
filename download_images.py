# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:56:21 2019

@author: 1024994
"""

import requests
import pandas as pd
import numpy as np
import urllib

data = pd.read_csv("C:\\Users\\1024994\\Desktop\\myntra\\tshirt_image_urls.csv")
data = np.array(data)



for i in range(4000):
    urllib.request.urlretrieve("{}".format(data[i][0])
, "C:\\Users\\1024994\\Desktop\\myntra\\myntra_tshirt_{}.jpg".format(i))

