import csv 
import matplotlib.pyplot as plt
#%matplotlib inline 
import numpy as np 
import pandas as pd 
         
#%reload_ext autoreload 
#%autoreload 2 
########################
with open("Open_Checkbook_FY2021_Dataset.csv",'r') as budget_file:
  #reader = csv.reader(budget_file)
  df = pd.read_csv(budget_file)


#print('hi')
#print(df)
print(df.index)
print(df.columns)


#main = 'Agency'
#sub = 'Service'
#main = 'Agency'
#sub = 'Vendor_Name'
#main = 'Vendor_Name'
#sub = 'Agency'
main = 'Fund'
sub = 'Spending_Description'
#main = 'Vendor_Name'
#sub = 'Amount'


service_hash = {}
for x in df.index:
  thismain = df[main][x]
  thissub = df[sub][x]
  thismainset = service_hash.get(thismain,set())
  thismainset.add(thissub)
  service_hash[thismain] = thismainset

for thiskey in service_hash.keys():
  print(thiskey)
  for thisval in service_hash[thiskey]:
    print('***' + str(thisval))
