import pandas as pd
dict1={'id':[10,30,40],
       'name':['sachine','kohli','dhoni']}
df1=pd.DataFrame(dict1)
print("df1 is:",df1)
dict2={'id':[24,34],
       'name':['rohit','gred']}
df2=pd.DataFrame(dict2)
print("data frame2 iss :",df2)
df3=df1,df2
print("df3 is :",df3)