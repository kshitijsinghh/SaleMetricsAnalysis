import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt

#col_list=["File_Name","Used"]

df = pd.read_csv("Dataset - Sheet1.csv")
#print(df.head())
print(df['Product'].unique())

newdf = df[(df.Product == 'A')]
#print(newdf.head())
print("Number of customer acquired from South"+"="+" "+ str(len(newdf)))
newdf2 = df[(df.Product == 'B')]
#print(len(newdf2))
print("Number of customer acquired from East"+"="+" "+ str(len(newdf2)))
newdf3 = df[(df.Product == 'G')]
newdf4 = df[(df.Product == 'F')]
newdf5 = df[(df.Product == 'D')]
newdf6 = df[(df.Product == 'E')]
newdf7 = df[(df.Product == 'C')]


print("Number of customer acquired from West"+"="+" "+ str(len(newdf3)))
print("Number of customer acquired from North"+"="+" "+ str(len(newdf4)))
print("Number of customer acquired from Central"+"="+" "+ str(len(newdf5)))
print("Number of customer acquired from Central"+"="+" "+ str(len(newdf6)))
print("Number of customer acquired from Central"+"="+" "+ str(len(newdf7)))

plot_df= data = {'Product': df['Product'].unique(),'NumberOfCustomers': [len(newdf),len(newdf2),len(newdf3),len(newdf4),len(newdf5),len(newdf6),len(newdf7)] }
df = pd.DataFrame(plot_df,columns=['Product','NumberOfCustomers'])
df.plot(x ='Product', y='NumberOfCustomers', kind = 'line')
df.to_csv('file2.csv')
plt.title("Demmand of Product among Customers")
plt.show()

Number= [len(newdf),len(newdf2),len(newdf3),len(newdf4),len(newdf5),len(newdf6),len(newdf7)]
print(max(Number)) #B