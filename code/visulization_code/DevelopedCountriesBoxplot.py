import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

feature = "Service"
file_path = "E:/Git/repository/DataMining/Developed Countries.csv"

data = pd.read_csv(file_path,index_col = "Country")
data = pd.DataFrame(data.loc[:,feature])
plt.figure()
p = data.boxplot(return_type = "dict")
x = p["fliers"][0].get_xdata()
y = p["fliers"][0].get_ydata()
y.sort()

for i in range(len(x)): 
  if i > 0:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
  else:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))
plt.show()