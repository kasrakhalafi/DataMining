# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import pandas
df = pandas.read_csv('data.csv',
                     index_col='id',
                     parse_dates=['confirmed_date'],
                     header=0)
print(df)