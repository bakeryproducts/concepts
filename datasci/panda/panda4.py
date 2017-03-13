# merging and joining dataframes ls6

import pandas as pd

df1 = pd.DataFrame({'year':[2001,2002,2003,2004],'rate1':[1,2,3,4]})

df2 = pd.DataFrame({'year':[2001,2002,2004,2005],'rate2':[1,2,4,10]})


# merge df1 with df2, left : df1 ; right :df2
# outer : union - all + nans; inner: intersection
# on = [columns that owned by df1 and df2]
merged = pd.merge(df1,df2,on = 'year', how = 'inner')       # how = left \ right\ outer\inner

merged.set_index('year',inplace=True)

print(merged)

df1['rate1']=[5,6,7,8]
print(df1)
print(merged)

# join with same indexes:
df1.set_index('year',inplace=True)
df2.set_index('year',inplace=True)
joined = df1.join(df2)
print(joined)
