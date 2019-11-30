#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 09:57:56 2019

@author: owner

import pandas as pd
data = [100, 120, 140, 180, 200, 210,
214]
s = pd.Series(data)
print(s)

s.index = ["a", "b", "c", "d",
"e","f","g"]
print(s) 


print( s.agg(['sum','max']))
s.plot()





import pandas as pd
s1 = pd.Series([10, 20, 30, 40, 50, 60], index=pd.date_range('20130102', periods=6))
#print(s1)
print (s1[1])
print (s1[1:3])
print (s1>20)




import pandas as pd
df1 = pd.DataFrame({
"Int_Rate":[2,1,2,3],
"IND_GDP":[50,45,45,67]},
index=[2001, 2002,2003,2004])

print(df1)
df2 = pd.DataFrame({"Low_Tier_HPI":[50,45,67,34],
"Unemployment":[1,3,5,6]},
index=[2001, 2003,2004,2004])

print(df2)
print(df1.join(df2))



import numpy as np
import pandas as pd
dates = pd.date_range('20190101', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('PQRS'))
print(df.head())
print(df[0:1])
print(df['20190102':'20190104'])
print(df[['P','Q']])

"""


import pandas as pd
d = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(d, columns = ['Number'])

df.to_excel('PandaTest.xlsx', sheet_name =
'testing', index = True)
df.to_csv('myDataFrame.csv', sep='\t')