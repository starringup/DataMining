import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

feature = "Literacy"

gdp = pd.read_csv("E:/Git/repository/DataMining/countries of the world.csv")

new_index = (gdp[feature].sort_values(ascending = False)).index.values
sorted_gdp = gdp.reindex(new_index)

plt.figure(figsize=(50,10))
sns.barplot(x = sorted_gdp["Country"],y = sorted_gdp[feature])
plt.xticks(rotation = -90)
plt.title(feature + "of countries in the world",color = "blue",fontsize = 15)
plt.show()