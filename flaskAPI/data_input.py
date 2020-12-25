import pandas as pd
import numpy as np 

df = pd.read_csv(r"C:\Users\hp\Documents\archive\booksENG_ref_train.csv")
X = df.drop('average_rating',axis =1)
data_in = list(X.iloc[5,:])