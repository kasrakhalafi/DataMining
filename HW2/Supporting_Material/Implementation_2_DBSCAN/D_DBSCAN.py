# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

from sklearn.cluster import DBSCAN
import pandas as pd
import folium
import numpy as np

loc = pd.read_csv('covid.csv',header=0)
loc = loc.values
r, _ = loc.shape

Eps = 0.55
MinPts = 150
db = DBSCAN(eps=Eps, min_samples=MinPts).fit(loc)
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Eps is chosen {} and MinPts is {} '.format(Eps, MinPts))
print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)

m = folium.Map(location=[32.427910, 53.688046], zoom_start = 5)

colours = ['green', 'blue', 'red', 'purple', 'crimson', 
           'white', 'pink', 'grey', 'orange', 'yellow',
           'brown', 'deeppink', 'magenta', 'black']

for i in range(r):
  folium.Circle(
    radius = 1,
    location = loc[i],
    popup = 'Covid-19 in this area',
    color = colours[labels[i]],
    fill = False,
    ).add_to(m)

m

