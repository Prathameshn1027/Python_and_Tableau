# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:30:09 2023

@author: pnalavde
"""

import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

#method 1 to open json file
json_file = open('loan_data_json.json')
data = json.load(json_file)

#Transform to dataframe
loandata = pd.DataFrame(data)

#to find unique values
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe the data for a particular column
loandata['int.rate'].describe()

loandata['fico'].describe()

loandata['dti'].describe()

#using EXP() to get the annual income from log.annual.inc
income = np.exp(loandata['log.annual.inc'])
#now add this income to the loandata
loandata['annualincome']= income

#working with arrays 
arr = np.array([1,2,3,4])   #this is a 1D array

#0D array
arr = np.array(10)

#2D array
arr = np.array([[1,2,3],[4,5,6]])

#3D array
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

#working with IF statements
a = 13
b = 20
if b>a:
    print('b is greater than a')
    
#with more conditions
a = 15
b = 20
c = 25
if b>a and b<c:
    print('b is greater than a but smaller than c')
    
#what if the condition is not met?

a = 30
b = 100
c = 20
if b>a and b<c:
    print('b is greater than a but smaller than c')
else:
    print('NO condition met')

#another condition with different matrics

a = 10
b = 20
c = 15
if b>a and b<c:
    print('b is greater than a but smaller than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('No condition')

#using or

a = 10
b = 20
c = 15
if b>a or b<c:
    print('b is greater than a or smaller than c')
else:
    print('No condition')

# FICO score
fico = 100 # this is just for 1 value
if fico >= 300 and fico < 400:
    ficocat = 'very poor'
elif fico >= 400 and fico < 600:
    ficocat = 'poor'
elif fico >= 601 and fico < 660:
    ficocat = 'fair'
elif fico >= 660 and fico < 700:
    ficocat = 'good'
elif fico >= 700:
    ficocat = 'excellent'
else:
    ficocat = 'unknown'
print(ficocat)

# FOR loops
# applying for loop to loandata 

#to find the length of the data
length = len(loandata)
#now applying for loop

ficocat = []
for x in range(0,length):
    catagory = loandata['fico'][x]
    
    try:
        
        if catagory >= 300 and catagory < 400:
            cat = 'very poor'
        elif catagory >= 400 and catagory < 600:
            cat = 'poor'
        elif catagory >= 601 and catagory < 660:
            cat = 'fair'
        elif catagory >= 660 and catagory < 700:
            cat = 'good'
        elif catagory >= 700:
            cat = 'excellent'
        else: 
            cat = 'unknown'
    except: 
        cat = 'unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
#create a nuew column on loandata

loandata['fico.catagory'] = ficocat








#df.loc as conditional statements
#df.loc[df[columnname] condition, newcolumn] = 'value if the condition is met'
#for interest rate, a new column is wanted. if rate>0.12, it is high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] < 0.12, 'int.rate.type'] = 'low'


#no of rows/columns by fico catagory
catplot = loandata.groupby(['fico.catagory']).size()
catplot.plot.bar(color = 'red', width = 0.8)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'blue')
plt.show()

#scatterplot of annual income vs dti
ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = 'red')
plt.show()

#writing to CSV
loandata.to_csv('loan_cleaned.csv' , index = True)










































