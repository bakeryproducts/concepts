import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv('/root/Documents/git/concepts/datasci/datasets/BP-COAL_CONSUM_O_RUS.csv')

df.set_index('Date',inplace=True)       # set date for index in df
df.to_csv('new.csv')
#df['Value'].to_csv('new.csv')

df = pd.read_csv('new.csv',index_col=0) # set index as column number

df.columns=['col_name']                 # new names for columns
print(df.head())
df.to_csv('new_wo_h.csv',header=False)  # wo header

df = pd.read_csv('new_wo_h.csv',names=['ind','col1'],index_col=0)   # open with header and index
print(df.head())

df.rename(columns={'col1':'NEWcol'},inplace=True)   # renames 1 column
print(df.head())
