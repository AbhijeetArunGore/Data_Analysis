import pandas as pd

s=pd.Series([1,2,3,4,5])
df=pd.DataFrame(s)
print(df)

names=pd.Series(['rohit','dhoni'])
team=pd.Series(["kal","mal"])
dic={'names':names,"team":team,"score":s}
df=pd.DataFrame(dic)
print(df)