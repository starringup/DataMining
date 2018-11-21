import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

all_countries_file_path = "E:/Git/repository/DataMining/countries of the world.csv"
developed_countries_file_path = "E:/Git/repository/DataMining/Developed Countries.csv"

#"Population","Area","NetMigration",
cov_features = ["PopDensity","Coastline","InfantMortality","NetMigration",
                "GDP","Literacy","Arable","Crops","Birthrate","Deathrate","Agriculture","Industry","Service"]
# cov_features = ["Agriculture","Industry","Service"]

#"Population":["United States","Japan"],"Area":["Canada","United States","Australia"],"NetMigration":["Singapore","Luxembourg"],
outlier = {
        "PopDensity":["Singapore"],"Coastline":["Italy","Denmark"],"NetMigration":["Singapore","Luxembourg"],
        "InfantMortality":["Israel","Korea.South"],"GDP":["Luxembourg","Norway","United States","Israel","Korea.South"],
        "Literacy":["Israel","Singapore"],"Arable":["Denmark"],"Crops":["Luxembourg","Norway","United States","Israel","Korea.South"],
        "Birthrate":["Israel"],"Deathrate":["Singapore"],"Agriculture":["Iceland"],"Industry":["Luxembourg","Ireland","Norway"],
        "Service":["Ireland","Luxembourg"]}
# outlier = {"Agriculture":["Iceland"],"Industry":["Luxembourg","Ireland","Norway"],
#         "Service":["Ireland","Luxembourg"]}

def calculateCov(dataset,flt = {}):
    cov = dict()
    for feature in dataset.columns:
        print("process %s:" % feature)
        tmp = dataset.loc[:,[feature]]    #筛选列
        countries = list(tmp.index)
        if len(flt) != 0:
            countries = list(set(tmp.index).difference(set(flt[feature])))
            if len(countries) != len(dataset) - len(flt[feature]):
                print("Error:the outliers' cnt is wrong!")
                print("%d - %d != %d" % (len(dataset),len(flt[feature]),len(countries)))

        d = tmp.loc[countries]      #筛选行
        arr = np.asarray(list(d[feature]))
        m_sum = sum(arr)
        nor = []
        # print("     normalize:")
        for x in arr:
            x = x / m_sum
            # x = float(x - np.min(arr)) / (np.max(arr) - np.min(arr))
            # print(x)
            nor.append(x)
        cov[feature] = np.asanyarray(nor).std()
        # cov[feature] = arr.std()
        print("标准差:%f" % cov[feature])
    return cov

def dictToDF(m_cov):
    tmp = {"feature":[],"cov":[]}
    for key in m_cov.keys():
        tmp["feature"].append(key)
        tmp["cov"].append(m_cov[key])
    return pd.DataFrame(tmp)

#计算发达国家相关属性的标准差
developed_countries_data = pd.read_csv(developed_countries_file_path,index_col = "Country")
print("计算发达国家相关属性的标准差:")
my_dc_dataset = developed_countries_data.loc[:,cov_features]
dev_cov = calculateCov(my_dc_dataset,flt = outlier)
dev_cov_df = dictToDF(dev_cov)
print("############################发达国家标准差#########################")

# 计算所有国家相关属性的标准差
# all_countries_data = pd.read_csv(all_countries_file_path,index_col = "Country")
# print("计算所有国家相关属性的标准差:")
# my_ac_dataset = all_countries_data.loc[:,cov_features]
# all_cov = calculateCov(my_ac_dataset)
# all_cov_df = dictToDF(all_cov)
# print("############################所有国家标准差#########################")


f,ax1 = plt.subplots(figsize = (20,10))
sns.pointplot(x = "feature",y = "cov",data = dev_cov_df,color = "lime",alpha = 0.8)
# sns.pointplot(x = "feature",y = "cov",data = all_cov_df,color = "red",alpha = 0.8)
plt.text(40,0.6,"developed countries' cov of every feature",color = "red",fontsize = 17,style = "italic")
# plt.text(40,0.55,"all countries' cov of every feature",color = "lime",fontsize = 18,style = "italic")
plt.xlabel("features",fontsize = 18,color = "blue")
plt.ylabel("cov",fontsize = 18,color = "blue")
plt.title("COV OF EVERY FEATURE",fontsize = 20,color = "blue")
plt.grid()
plt.show()

# for feature in my_dc_dataset.columns:
#     print("process %s:" % feature)
#     tmp = my_dc_dataset.loc[:,[feature]]    #筛选列
#     countries = list(set(tmp.index).difference(set(outlier[feature])))

#     if len(countries) != len(my_dc_dataset) - len(outlier[feature]):
#         print("Error:the outliers' cnt is wrong!")
#         print("%d - %d != %d" % (len(my_dc_dataset),len(outlier[feature]),len(countries)))

#     d = tmp.loc[countries]      #筛选行
#     arr = np.asarray(list(d[feature]))
#     nor = []
#     print("     normalize:")
#     for x in arr:
#         x = float(x - np.min(arr)) / (np.max(arr) - np.min(arr))
#         print(x)
#         nor.append(x)
#     developed_cov[feature] = np.asanyarray(nor).std()
#     print("标准差:%f" % developed_cov[feature])
