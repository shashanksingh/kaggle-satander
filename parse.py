import pandas as pd
from sklearn.cluster import KMeans
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split

train_v2 = pd.read_csv("train_ver2.csv",header=0, nrows=261)
# print train_v2.pivot(index="ncodpers", columns="fecha_dato", values="age")
simple_df_to_cluster = train_v2.loc[:,["age"]]

print simple_df_to_cluster


cluster = KMeans(n_clusters=10, random_state=20)
result = cluster.fit_predict(simple_df_to_cluster)
print "Cluster Centers"
print cluster.cluster_centers_
# result = cluster.predict(sample_df_test)
print "Prediction"
print result 