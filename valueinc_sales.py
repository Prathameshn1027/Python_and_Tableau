# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:23:21 2023

@author: pnalavde
"""

import pandas as pd

#file_name = pd.read_csv('file.csv') <---------FORMAT
data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

data.info()

#working with calculations
#defining variables

CostPerItem = 11.73
SellingPricePerItem = 22.11
NumberOfItemsPurchased = 6

#Mathematical operations on Tableau

ProfitPerItem = 21.11 - 11.73

ProfitPerTransaction = ProfitPerItem * NumberOfItemsPurchased

CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column Calculation

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased 
#Variable = dataframe['Column_name']
CostPerItem = data['CostPerItem'] 
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased 

#Adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction


#sales per transaction column
SalesPerTransaction = SellingPricePerItem * NumberOfItemsPurchased
data['SalesPerTransaction'] = SalesPerTransaction

#calculate profit
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#calculate markup

MarkupPerTransaction = (SalesPerTransaction - CostPerTransaction)/CostPerTransaction
data['MarkupPerTransaction'] = (data['SalesPerTransaction'] - data['CostPerTransaction'])/ data['CostPerTransaction']

#----------------------------OR--------------------- ( any way is fine!)
data['MarkupPerTransaction']  = data['ProfitPerTransaction'] / data['CostPerTransaction']


#round markup ( we just need 2 numbers after the decimal)

roundmarkup = round(data['MarkupPerTransaction'], 2)

#put this new column in the dataframe

data['roundmarkup'] = round (data['MarkupPerTransaction'], 2)

#Combining data fields ( multiple columns )
# Here we are combining day, month and year column together

my_date = 'Day'+'-'+'Month'+'-'+'Year'

#since the data type is not same for all, we change the data type to object

day = data['Day'].astype(str)
print(day.dtype) 

my_date = day + '-' + data['Month']

year = data['Year'].astype(str)
print(year.dtype)

my_date = day + '-' + data['Month'] + '-' + year

#now add this column in the data frame 
data['my_date'] = my_date

# if you want to view a particular row or column; use "iloc"

data.iloc[0] #this will view row with index 0
data.iloc[0:3]  #first 3 rows
data.iloc[-5:]  #last 5 rows

data.head(5)

data.iloc[4,2] #we want 4th row and 2nd column value

#Using split 
#new_var = column.str.split('sep' , expand = True)  <----Format to split a column

split_col = data['ClientKeywords'].str.split(',' , expand = True)

#Creating a new column for each of the splits from above "Client key words"

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using replace function 
data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']' , '')

#changing item to lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

#How to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv' , sep=';')

#merging files : merge_df = pd.merge(df_old , df_new, on = 'key') <-------Format

data = pd.merge(data, seasons, on = 'Month')

#Dropping columns 
#df = df.drop('columnname' , axis = 1) <------------Format

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop(['Year','Month','Day'], axis = 1) 

#Export into CSV
data.to_csv('ValueInc_Cleaned.csv' , index = False)







































