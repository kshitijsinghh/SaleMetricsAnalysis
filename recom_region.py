import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt

#col_list=["File_Name","Used"]

df = pd.read_csv("Dataset - Sheet1.csv")
#print(df.head())
print(df['Region'].unique())
import csv
import pandas as pd
import numpy


#col_list=["File_Name","Used"]

df = pd.read_csv("Dataset - Sheet1.csv")
#print(df.head())
#print(df['Region'].unique())
newdf = df[(df.Region == 'South')]
#print(newdf.head())
print("Number of customer acquired from South"+"="+" "+ str(len(newdf)))
newdf2 = df[(df.Region == 'East')]
#print(len(newdf2))
print("Number of customer acquired from East"+"="+" "+ str(len(newdf2)))
newdf3 = df[(df.Region == 'West')]
newdf4 = df[(df.Region == 'North')]
newdf5 = df[(df.Region == 'Central')]

print("Number of customer acquired from West"+"="+" "+ str(len(newdf3)))
print("Number of customer acquired from North"+"="+" "+ str(len(newdf4)))
print("Number of customer acquired from Central"+"="+" "+ str(len(newdf5)))

plot_df= data = {'Region': df['Region'].unique(),'NumberOfCustomers': [len(newdf),len(newdf2),len(newdf3),len(newdf4),len(newdf5)] }
df = pd.DataFrame(plot_df,columns=['Region','NumberOfCustomers'])
df.to_csv('file3.csv')

df.plot(x ='Region', y='NumberOfCustomers', kind = 'line')
plt.title("Number of Customer in each Region")
plt.show()
#East

