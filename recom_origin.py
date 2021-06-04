import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt

#col_list=["File_Name","Used"]

df = pd.read_csv("Dataset - Sheet1.csv")
#print(df.head())
print(df['Origin'].unique())
newdf = df[(df.Origin == 'referral')]
#print(newdf.head())
print("Number of customer acquired from rederral"+"="+" "+ str(len(newdf)))
newdf2 = df[(df.Origin == 'display')]
#print(len(newdf2))
print("Number of customer acquired from display"+"="+" "+ str(len(newdf2)))
newdf5 = df[(df.Origin == 'paid_search')]
newdf3 = df[(df.Origin == 'social')]
newdf4 = df[(df.Origin == 'other')]
newdf7 = df[(df.Origin == 'email')]
newdf8 = df[(df.Origin == 'direct_traffic')]
newdf9 = df[(df.Origin == 'organic_search')]
newdf6 = df[(df.Origin == 'unknown')]
print("Number of customer acquired from paid_search"+"="+" "+ str(len(newdf3)))
print("Number of customer acquired from social"+"="+" "+ str(len(newdf4)))
print("Number of customer acquired from other"+"="+" "+ str(len(newdf5)))
print("Number of customer acquired from email"+"="+" "+ str(len(newdf6)))
print("Number of customer acquired from direct_traffic"+"="+" "+ str(len(newdf7)))
print("Number of customer acquired from organic_traffic"+"="+" "+ str(len(newdf8)))
plot_df= data = {'Origin': df['Origin'].unique(),'NumberOfCustomers': [len(newdf),len(newdf2),len(newdf3),len(newdf4),len(newdf5),len(newdf6),len(newdf7),len(newdf8),len(newdf9)] }
df = pd.DataFrame(plot_df,columns=['Origin','NumberOfCustomers'])
df.plot(x ='Origin', y='NumberOfCustomers', kind = 'line')
df.to_csv('file1.csv')
plt.title("Number of Customer Acquired from each Origin")
plt.show()
Number=  [len(newdf),len(newdf2),len(newdf3),len(newdf4),len(newdf5),len(newdf6),len(newdf7),len(newdf8),len(newdf9)]
print(max(Number)) #paid_search


