import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt

#col_list=["File_Name","Used"]

df = pd.read_csv("Dataset - Sheet1.csv")
print(df['Product'].unique())
Cost_A=df[(df.Product== 'A')].Sales.sum()
Cost_B=df[(df.Product== 'B')].Sales.sum()
Cost_C=df[(df.Product== 'C')].Sales.sum()
Cost_D=df[(df.Product== 'D')].Sales.sum()
Cost_E=df[(df.Product== 'E')].Sales.sum()
Cost_F=df[(df.Product== 'F')].Sales.sum()
Cost_G=df[(df.Product== 'G')].Sales.sum()
print(Cost_B)
print(Cost_G)


data = {'Product': df['Product'].unique(),
        'Revenue': [Cost_A,Cost_B,Cost_G,Cost_F,Cost_D,Cost_E,Cost_C]
       }
  
df = pd.DataFrame(data,columns=['Product','Revenue'])
df.plot(x ='Product', y='Revenue', kind = 'bar')
df.to_csv('file6.csv')
plt.title("Revenue Generated From each Product")
plt.show()



