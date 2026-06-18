import pandas as pd
dic={'name':['sachine','kohli','kohli'],'age':[10,32,33]}
df=pd.DataFrame(dic)
df=pd.DataFrame(dic,index=[True,False,False])
print(df)
print(df.loc[False])