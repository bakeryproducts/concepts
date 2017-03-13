# quandl pickle pandas

import pandas as pd
import quandl
import pickle


main_df = pd.DataFrame()

api_key = open('api.txt','r').read()
quandl.ApiConfig.api_key=api_key
df1 = quandl.get('FMAC/HPI_KILTX')
df2 = quandl.get('FMAC/HPI_KANMO')
main_df = df1
#
# df_li =[df1,df2]
# for df in df_li
merged = df1.join(df2,lsuffix='_1',rsuffix='_2')

pickle_out = open('picklesaveDF','wb')
pickle.dump(merged,pickle_out)
pickle_out.close()

pickle_in = open('picklesaveDF','rb')
loaded_data = pickle.load(pickle_in)

print(merged.head(1))           # loaded right now
print(loaded_data.head())       # saved in pickle


merged.to_pickle('builtin_pandas')
merged_restored = pd.read_pickle('builtin_pandas')
print(merged_restored.head())          # same thing but nicer