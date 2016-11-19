# pip install --upgrade pip
python -m pip install --upgrade pip
virtualenv  .
source bin/activate
pip install  numpy scipy matplotlib ipython jupyter pandas sympy nose
pip install -U scikit-learn
pip install pandas
sudo apt-get install unzip
wget https://www.kaggle.com/c/santander-product-recommendation/download/train_ver2.csv.zip
unzip train_ver2.csv.zip