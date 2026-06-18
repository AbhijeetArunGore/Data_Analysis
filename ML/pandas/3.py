import numpy as np
import pandas as pd
arr2=np.array(['a','b','c','d','e'])
arr=np.array([10,20,30,40,50])
s1=pd.Series(arr,index=arr2)
print(s1)
t=np.sqrt(s1)
print(t)