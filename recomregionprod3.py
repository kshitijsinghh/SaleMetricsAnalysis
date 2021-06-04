import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt

#col_list=["File_Name","Used"]

df = pd.read_csv("Dataset - Sheet1.csv")
#file = df["Product"]
#newdf = df[(df.Product == 'B')]
#file= newdf["File_Name"]
newdf1 = df[(df.Region == 'East')][(df.Product == 'A')]
print(len(newdf1))
newdf2 = df[(df.Region == 'East')][(df.Product == 'B')]
newdf3 = df[(df.Region == 'East')][(df.Product == 'C')]
newdf4 = df[(df.Region == 'East')][(df.Product == 'D')]
newdf5 = df[(df.Region == 'East')][(df.Product == 'E')]
newdf6 = df[(df.Region == 'East')][(df.Product == 'F')]
newdf7 = df[(df.Region == 'East')][(df.Product == 'G')]
print(len(newdf2))
print(len(newdf3))
print(len(newdf4))
print(len(newdf5))
print(len(newdf6))
print(len(newdf7))

data = {'Products': ['A','B','C','D','E','F','G'] ,
        'Number of Customer': [len(newdf1),len(newdf2),len(newdf3),len(newdf4),len(newdf5),len(newdf6),len(newdf7)]
       }
  
df = pd.DataFrame(data,columns=['Products','Number of Customer'])
df.plot(x ='Products', y='Number of Customer', kind = 'bar')
df.to_csv('file9.csv')
plt.title("Most Popular Product in East Region")
plt.show()





