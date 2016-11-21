import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_graphviz

decision_tree = DecisionTreeClassifier()

print "[DecisonTree][Step 1] Find out unique customers"
print "[DecisonTree] Load CSV"
train_v2 = pd.read_csv("train_ver2.csv",header=0, nrows=1262000,dtype={"ncodpers": int})#limited
customer_codes = train_v2.loc[:,["ncodpers"]]
product_bought = train_v2.loc[:,["ind_ahor_fin_ult1"]]

clf = decision_tree.fit(customer_codes,product_bought)

export_graphviz(clf, out_file="tree.dot")