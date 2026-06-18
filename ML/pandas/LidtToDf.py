import pandas as pd
l=[{'name':"sne",'score':"13",},
   {"name":'abi','score':'23'},
   {'name':'ded','score':'33'
   }]
df=pd.DataFrame(l)
print(df)
for (row_index,row_value) in df.iterrows():
    print("\n row index is :",row_index)
    print("\n row value is :",row_value)


for(col_index,col_valu) in df.ite():
    print("\n column index is :",col_index)
    print("\n column value is :",col_valu)
