import numpy as np
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

countries_of_the_world = pd.read_csv('C:/Users/Gilbert_Lee/Desktop/DataMining/countries of the world.csv', encoding="windows-1252")
countries_of_the_world['Country'].unique()
countries_of_the_world.Service.replace(['-'],0.0,inplace = True)
countries_of_the_world.Service = countries_of_the_world.Service.astype(float)
area_list = list(countries_of_the_world['Country'].unique())
area_poverty_ratio = []
for i in area_list:
    x = countries_of_the_world[countries_of_the_world['Country']==i]
    area_poverty_rate = sum(x.Service)/len(x)
    area_poverty_ratio.append(area_poverty_rate)
data = pd.DataFrame({'area_list': area_list,'area_poverty_ratio':area_poverty_ratio})
new_index = (data['area_poverty_ratio'].sort_values(ascending=False)).index.values
sorted_data = data.reindex(new_index)

# visualization
plt.figure(figsize=(150,10))
sns.barplot(x=sorted_data['area_list'], y=sorted_data['area_poverty_ratio'])
plt.xticks(rotation= 45)
plt.xlabel('Countries')
plt.ylabel('Service')
plt.title('Service of Countries')