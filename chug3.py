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


boring = set()
boring.add('OBJECTID_1')
boring.add('OBJECTID')
boring.add('Date_Accuracy')
boring.add('GlobalID')
boring.add('name')
boring.add('Amount')

print(boring)

nonboring = set(df.columns).difference(boring)

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

# okay, here's the thing...
# we have two columns, a main column and a sub column
# we are assuming that these columns have some sort of
# controlled vocabulary, or at least very commonly 
# recurring values that act as such
# we are ultimately looking for rules of the form
# IF COLUMN A HAS VALUE X THEN COLUMN B ALWAYS HAS VALUE Y
# e.g.
# IF CITY HAS VALUE BALTIMORE THEN STATE ALWAYS HAS VALUE MARYLAND
# or slight generalizations of this
# in terms of below we have
# IF COLUMN MAIN HAS VALUE X THEN COLUMN SUB ALWAYS HAS VALUE Y
# which happens when the sets in set_hash have cardinality 1
# (better variable names may suggest themselves after batting this around)
# the code below will crudely achieve this, marching through indices
# for main and sub
# for every value in the main column we create a set corresponding to that value
# that has the corresponding value in the sub column
# and then we go back through and for every keyword from main
# we list the values we have encountered for sub
# e.g. if main is vendor_name and sub is fund
# then for each vendor we are reporting
# the vendor and the set of funds that vendor is paid out of
# not bad documentation for a file stupidly named chug3.py huh?
# it's a pretty low bar

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

def print_crap(df,main,sub):
  set_hash = {}
  for x in df.index:
    thismain = df[main][x]
    thissub = df[sub][x]
    thismainset = set_hash.get(thismain,set())
    thismainset.add(thissub)
    set_hash[thismain] = thismainset

  for thiskey in set_hash.keys():
    myset = set_hash[thiskey]
    if len(myset) == 1:
      for thisval in myset:
#        print(myset)
#        print('Main: ' + main)
#        print('Sub: ' + sub)
#        print(thiskey)
#        print('***' + str(thisval))
        print('If the ' + str(main) + ' is ' + str(thiskey) + ' then the ' + str(sub) + ' is ' + str(thisval))
        print('--------------------')

for main in nonboring:
  for sub in nonboring:
    if not main == sub:
      print_crap(df,main,sub)
