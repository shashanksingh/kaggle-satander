#simple collbrative filtering, 
# step 1 : Find out unique customers
# step 2 : How many times have they bough a certain product
# step 3 : find out similar customers ( clustering -> age and other features )
# stesp 4 : find top hits in a cluster and recommend everyone the same


import pandas as pd
from sklearn.cluster import KMeans
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split

print "[Parse] Load CSV"
train_v2 = pd.read_csv("train_ver2.csv",header=0, nrows=262)
# print train_v2.pivot(index="ncodpers", columns="fecha_dato", values="age")
simple_df_to_cluster = train_v2.loc[:,["age"]]
print "[Parse] GET "

print simple_df_to_cluster


cluster = KMeans(n_clusters=10, random_state=20)
result = cluster.fit_predict(simple_df_to_cluster)
print "Cluster Centers"
print cluster.cluster_centers_
# result = cluster.predict(sample_df_test)
print "Prediction"
print result 
