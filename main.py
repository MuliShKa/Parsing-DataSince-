import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("temu-2025-10-03 (1).csv")

df['price-2Xz_3'] = df['price-2Xz_3'].astype(str)


df_filled = df.fillna('N/A')

df_no_na = df.dropna()

duplicates = df.duplicated()

df_no_duplicates = df.drop_duplicates()

df['price-2Xz_3_split'] = df['price-2Xz_3'].str.split('-')






print(df_no_duplicates)

