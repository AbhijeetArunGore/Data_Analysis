import pandas as pd
s=pd.Series([23,24,56,32])
df=pd.DataFrame(s)
df.columns=['list1']
df['list2']=20
df['list3']=df['list1']+df['list2']
print(df)
df1=df.drop(index=[0,1],axis=0)
print(df1)