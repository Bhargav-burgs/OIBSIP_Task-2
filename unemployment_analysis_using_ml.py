# -*- coding: utf-8 -*-
"""Unemployment analysis using ml.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W-bcViGwlcE1G6N9c8idi2G-nBmdLWXg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data=pd.read_csv('/content/Unemployment_Rate_upto_11_2020.csv')
data

data.shape

data.info()

data.describe()

data.isnull().sum()

data.corr()

sns.heatmap(data.corr())

x = data['Region']
x

y = data[' Estimated Unemployment Rate (%)']
y

df=data.iloc[:,3]

df

fg=px.bar(data,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemplyment Rate State Wise by bar graph')
fg.show()

fg=px.bar(data,x='Region.1',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemplyment Rate Region Wise by bar graph')
fg.show()

fg=px.box(data,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemplyment Rate State Wise by box plot')
fg.show()

fg=px.scatter(data,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemplyment Rate State Wise by bar graph')
fg.show()

fg=px.histogram(data,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',title='Unemplyment Rate State Wise by bar graph')
fg.show()

unemployment = data[['Region','Region.1',' Estimated Unemployment Rate (%)']]
fig = px.sunburst(unemployment,path=['Region.1','Region'], values=' Estimated Unemployment Rate (%)', width=700, height=700, title='Unemployment rate in BHARAT')
fig.show()