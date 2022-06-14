# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 01:04:22 2021

@author: hp
"""

#cleaning the data
import pandas as pd 
import numpy as np 
import re
#importing the dataset
df = pd.read_csv('voyalla.csv')
url = []
url2=[]
for i in df['LINK']:
    imageurl = re.findall(r'(?:http\:|https\:)?\/\/.*?\.(?:png|jpg)', i)
    url.append(imageurl)
for i in url:
    url2.append(i[1])
df['LINK'] = url2
df.to_csv('finally.csv' , index = False)