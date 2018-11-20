import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.metrics import accuracy_score
from subprocess import check_call
from IPython.display import Image as PImage
from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt
import graphviz
import os

def createMyDataFrame(source_data,keys_list):
    tmp = dict()
    for key in keys_list:
        tmp[key] = list(source_data[key])
    return pd.DataFrame(tmp)

train_dataset_path = "E:/Git/repository/DataMining/countries of the world.csv"
keys_list = ["InfantMortality","GDP","Literacy","Birthrate","Deathrate","Industry","Service","Developed"]
condidate_country = ["Malta","Czech Republic","Andorra","Slovenia","Bermuda","Cayman Islands","San Marino","Aruba","Liechtenstein",
                    "Estonia","Niger","Mali","Uganda","Afghanistan","N. Mariana Islands","Kuwait","Saudi Arabia","Jordan","Equatorial Guinea",
                    "Qatar","Iraq","Angola","Jersey","British Virgin Is.","Bahamas. The","Macau China","Japan","United States"]
train_dataset = pd.read_csv(train_dataset_path,index_col="Country")
#剔除原数据集中无用的属性
predict_df = train_dataset.loc[condidate_country]
train_countries = list(set(train_dataset.index).difference(set(condidate_country)))
train_df = train_dataset.loc[train_countries]

train_df = createMyDataFrame(train_df,keys_list)
predict_df = createMyDataFrame(predict_df,keys_list)

# #将Developed属性作为输出，其他属性作为输入
x,y = train_df.loc[:,train_df.columns != "Developed"],train_df.loc[:,"Developed"]
predict_condidate = predict_df.loc[:,predict_df.columns != "Developed"]

# #将数据集分为训练集和测试集
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.33,random_state = 42)

# #训练决策树分类器
max_depth = 6
clf = tree.DecisionTreeClassifier(max_depth=max_depth)
clf = clf.fit(x,y.astype("int"))
print(clf.predict(predict_condidate))

#检验预测准确率
# print(accuracy_score(y_test.astype("int"),clf.predict(x_test)))

#交叉检验
# cv_avg = []
# n = 10
# k_range = range(3,10)
# for k in k_range:
#     clf = tree.DecisionTreeClassifier(max_depth=)
#     cv_result = cross_val_score(clf,x,y,cv = n)
#     print("cv scores:",cv_result)
#     avg = np.sum(cv_result) / n
#     print("cv scores average",avg)
#     cv_avg.append(avg)
# plt.plot(k_range,cv_avg)
# plt.xlabel("depth of the decision tree")
# plt.ylabel("accuracy")
# plt.show()

# clf = tree.DecisionTreeClassifier(max_depth=max_depth)
# cv_result = cross_val_score(clf,x,y,cv = 10)

os.environ["PATH"] += os.pathsep + "E:/Graphviz/Graphviz2.38/bin/"
dot_data = tree.export_graphviz(clf,
                                out_file=None,
                                feature_names=list(x),
                                class_names=["developing","developed"],
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("./Decision Tree",view=True)

