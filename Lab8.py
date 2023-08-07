# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:59:11 2023

@author: Cooks
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("all_alpha_19.csv", header = 'infer')

df = df[df['Stnd'] == 'T3B125']
df = df.query('Fuel == "Diesel" or Fuel == "Gasoline"')

cols = ['Model', 'Displ', 'Fuel', 'City MPG', 'Hwy MPG', 'Cmb MPG', 'Greenhouse Gas Score']

new_df = df[cols].reset_index(drop=True)

new_df = new_df.astype({'City MPG':'float','Hwy MPG':'float', 'Cmb MPG':'float'})

def mpg_to_kml(mpg):
    return mpg*0.42514

new_df = new_df.assign(CityKML = lambda x: mpg_to_kml(x['City MPG']))
new_df = new_df.assign(HwyKML = lambda x: mpg_to_kml(x['Hwy MPG']))
new_df = new_df.assign(CmbKML = lambda x: mpg_to_kml(x['Cmb MPG']))

new_df.to_csv("car_data.csv")

df = pd.read_csv("car_data.csv", header='infer', index_col= 0)

df.plot(x = 'Displ', y = 'CityKML', kind ='scatter',color = 'r')
plt.show()

c = []
for x in df['Fuel']:
    if x =='Gasoline':
        c.append('r')
    else:
        c.append('g')
s = []
for x in df['Greenhouse Gas Score']:
    x = x*8
    s.append(x)
df.plot(x = 'Displ', y = 'CityKML', kind ='scatter',color = c, s = s, alpha = 0.5)
