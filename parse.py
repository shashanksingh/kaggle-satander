#simple collbrative filtering
# step 1 : Find out unique customers
# step 2 : How many times have they bough a certain product
# step 3 : find out similar customers ( clustering -> age and other features )
# stesp 4 : find top hits in a cluster and recommend everyone the same

#header : "fecha_dato","ncodpers","ind_empleado","pais_residencia","sexo","age",
#header : "fecha_alta","ind_nuevo","antiguedad","indrel","ult_fec_cli_1t",
#header : "indrel_1mes","tiprel_1mes","indresi","indext","conyuemp","canal_entrada",
#header : "indfall","tipodom","cod_prov","nomprov","ind_actividad_cliente","renta",
#header : "segmento","ind_ahor_fin_ult1","ind_aval_fin_ult1","ind_cco_fin_ult1",
#header : "ind_cder_fin_ult1","ind_cno_fin_ult1","ind_ctju_fin_ult1",
#header : "ind_ctma_fin_ult1","ind_ctop_fin_ult1","ind_ctpp_fin_ult1",
#header : "ind_deco_fin_ult1","ind_deme_fin_ult1","ind_dela_fin_ult1",
#header : "ind_ecue_fin_ult1","ind_fond_fin_ult1","ind_hip_fin_ult1",
#header : "ind_plan_fin_ult1","ind_pres_fin_ult1","ind_reca_fin_ult1",
#header : "ind_tjcr_fin_ult1","ind_valo_fin_ult1","ind_viv_fin_ult1",
#header : "ind_nomina_ult1","ind_nom_pens_ult1","ind_recibo_ult1"

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split

print "[Parse][Step 1] Find out unique customers"
print "[Parse] Load CSV"
train_v2 = pd.read_csv("train_ver2.csv",header=0, nrows=1262000,dtype={"ncodpers": int})#limited
customer_codes = train_v2.loc[:,["ncodpers"]]
unique_customer_codes = customer_codes.drop_duplicates()
# print "[Parse] Customer Code ", unique_customer_codes
print "[Parse] Unique customer count", unique_customer_codes.count()

print "[Parse][Step 2] How many times have they bough a certain product"
customer_with_product_array=train_v2.loc[:,["ncodpers",
          "ind_ahor_fin_ult1","ind_aval_fin_ult1","ind_cco_fin_ult1",
          "ind_cder_fin_ult1","ind_cno_fin_ult1","ind_ctju_fin_ult1",
          "ind_ctma_fin_ult1","ind_ctop_fin_ult1","ind_ctpp_fin_ult1",#done
          "ind_deco_fin_ult1","ind_deme_fin_ult1","ind_dela_fin_ult1",
          "ind_ecue_fin_ult1","ind_fond_fin_ult1","ind_hip_fin_ult1",
          "ind_plan_fin_ult1","ind_pres_fin_ult1","ind_reca_fin_ult1",
          "ind_tjcr_fin_ult1","ind_valo_fin_ult1","ind_viv_fin_ult1",
          "ind_nomina_ult1","ind_nom_pens_ult1","ind_recibo_ult1"
          ]]
print "[Parse] Groupby customer code"
customer_with_product_array_grouped_by_customer = customer_with_product_array.groupby(["ncodpers"])
print "[Parse] Stats - Groupby customer code"
print customer_with_product_array_grouped_by_customer.aggregate(np.sum)
# customer_with_product_array.duplicated()

print "[Parse][Step 3] Find out similar customers ( clustering -> age and other features )"
# cluster = KMeans(n_clusters=10, random_state=20)
# # result = cluster.fit_predict(unique_customer_code)
# print "Cluster Centers"
# print cluster.cluster_centers_
# # result = cluster.predict(sample_df_test)
# print "Prediction"
# print result
