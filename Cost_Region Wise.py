import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt

#col_list=["File_Name","Used"]

df = pd.read_csv("Dataset - Sheet1.csv")
print(df['Region'].unique())
Cost_c=df[(df.Region == 'Central')].Sales.sum()
Cost_E=df[(df.Region == 'East')].Sales.sum()
Cost_W=df[(df.Region == 'West')].Sales.sum()
Cost_N=df[(df.Region == 'North')].Sales.sum()
Cost_S=df[(df.Region == 'South')].Sales.sum()



print(Cost_c)
print(Cost_E)
print(Cost_W)
print(Cost_N)
print(Cost_S)
data = {'Region': df['Region'].unique(),
        'Revenue': [Cost_S,Cost_E,Cost_N,Cost_W,Cost_c]
       }
  
df = pd.DataFrame(data,columns=['Region','Revenue'])
df.plot(x ='Region', y='Revenue', kind = 'bar')
df.to_csv('file4.csv')
plt.title("Revenue Generated in each Region")
plt.show()
