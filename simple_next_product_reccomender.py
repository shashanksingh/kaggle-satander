import pandas as pd
import numpy as np
import datetime

# train_v2 = pd.read_csv("train_ver2.csv",header=0, nrows=1262000,dtype={"ncodpers": int})#limited

counter = 0
with open('reccomendation.csv', 'a') as f:
  f.write('ncodpers,added_products\n')
  for df in pd.read_csv('train_ver2.csv',header=0,  chunksize=10000):
    customer_with_product_array=df.loc[:,["ncodpers",
          "ind_ahor_fin_ult1","ind_aval_fin_ult1","ind_cco_fin_ult1",
          "ind_cder_fin_ult1","ind_cno_fin_ult1","ind_ctju_fin_ult1",
          "ind_ctma_fin_ult1","ind_ctop_fin_ult1","ind_ctpp_fin_ult1",#done
          "ind_deco_fin_ult1","ind_deme_fin_ult1","ind_dela_fin_ult1",
          "ind_ecue_fin_ult1","ind_fond_fin_ult1","ind_hip_fin_ult1",
          "ind_plan_fin_ult1","ind_pres_fin_ult1","ind_reca_fin_ult1",
          "ind_tjcr_fin_ult1","ind_valo_fin_ult1","ind_viv_fin_ult1",
          "ind_nomina_ult1","ind_nom_pens_ult1","ind_recibo_ult1"
          ]]

    # customer_with_product_array.
    # for single.

    dataframe_to_write = pd.DataFrame([])
    for row , column in customer_with_product_array.iterrows():
      # print column[0]
      series_to_write = pd.Series({ "ncodpers":column[0], "added_products":"ind_nomina_ult1"})
      # print series_to_write, dataframe_to_write
      # dataframe_to_write.add(series_to_write)
      # series_to_write.to_csv(f,header=False,sep=',',index=False)
      f.write(str(int(column[0]))+",ind_nomina_ult1\n")
    # print dataframe_to_write

    print "[SIMPLE_NEXT_PRODUCT_RECCOMENDER][CSV]",dataframe_to_write.to_csv(f,header=False)
    counter = counter + 1
    # df.to_csv(f, header=False)
    print "[SIMPLE_NEXT_PRODUCT_RECCOMENDER][", (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),"][",counter,"] Done with Batch" 

f.close()