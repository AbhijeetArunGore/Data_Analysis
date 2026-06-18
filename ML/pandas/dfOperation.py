import pandas as pd
s=pd.Series([1,2,3,4])
df=pd.DataFrame(s)
print(df)
df.columns=['list1']
print(df)
df['list2']=20
print(df)
df['list3']=df['list1']+df['list2']
print(df)
del df['list3']
print(df)