import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt

#col_list=["File_Name","Used"]

df = pd.read_csv("Dataset - Sheet1.csv")
print(df['Origin'].unique())
Cost_ref=df[(df.Origin== 'referral')].Sales.sum()
Cost_dis=df[(df.Origin== 'display')].Sales.sum()
Cost_soc=df[(df.Origin== 'social')].Sales.sum()
Cost_oth=df[(df.Origin== 'other')].Sales.sum()
Cost_pai=df[(df.Origin== 'paid_search')].Sales.sum()
Cost_unk=df[(df.Origin== 'unknown')].Sales.sum()
Cost_ema=df[(df.Origin== 'email')].Sales.sum()
Cost_dir=df[(df.Origin== 'direct_traffic')].Sales.sum()
Cost_org=df[(df.Origin== 'organic_search')].Sales.sum()



print(Cost_ref)
print(Cost_dis)
print(Cost_soc)
print(Cost_oth)
print(Cost_pai)
print(Cost_unk)
print(Cost_ema)
print(Cost_dir)
print(Cost_org)
data = {'Origin': df['Origin'].unique(),
        'Revenue': [Cost_ref,Cost_dis,Cost_soc,Cost_oth,Cost_pai,Cost_unk,Cost_ema,Cost_dir,Cost_org]
       }
  
df = pd.DataFrame(data,columns=['Origin','Revenue'])
df.plot(x ='Origin', y='Revenue', kind = 'bar')
df.to_csv('file5.csv')
plt.title("Revenue Gernerated From each Origin")
plt.show()
