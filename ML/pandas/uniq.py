import pandas as pd
s1=pd.Series([1,2,2,3,4,3,5])
print("the unique elements in series are :",s1.unique())
#how many unique elements are there
print(s1.nunique(),"elements are unique")
#all values like mean max
print("description of s1:",s1.describe())