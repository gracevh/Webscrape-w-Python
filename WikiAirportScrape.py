#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:48:57 2020

@author: burlios
"""


from bs4 import BeautifulSoup
from urllib.request import urlopen # urllib2 split to urllib.request and urllib.error in Py3

url = "https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States"
html = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html)
soup2 = BeautifulSoup(html, 'lxml') # a faster parser than the default if desired

# First get the table headings as a list
headings = []
for th in ap_table_data[0].find_all("th"):
    # remove any newlines and extra spaces from left and right
    headings.append(th.text.replace('\n', ' ').strip())
headings

import re
x = "2019[2] 21(5)"

re.sub("[\(\[].*?[\)\]]", "", x) # use regex function to remove brackets and parentheses from a string
re.sub("[\[].*?[\]]", "", x) # use regex function to remove bracketed info from a string


        
        
# get first table with find using tag "table"
ap_table = soup.find("table", attrs={"class": "wikitable"})
ap_table_data = ap_table.tbody.find_all("tr")  # contains 2 rows
len(ap_table_data) # find the length for the loop

import pandas as pd
# put the data into a list to become a dataframe
info = []
df = []
for i in range(1,31): # ignore the headers for now
    info.append(ap_table_data[i].text.replace('\n', '_').strip()) # insert _ to separate pieces of info
    temp = pd.Series(info[i]) # turn into series to split-expand
    df.append(temp.str.split('_',expand=True)) # split into columns with expand based on _ and bc its series 
    
type(df)  # its a list
type(df[0]) # list of dataframes 
df = pd.concat(df) # concatenate the list of dataframes to one dataframe 

import numpy as np

copy = df.copy() # make a copy of the data for safety
copy = copy.replace('', np.nan) # turn empty strings into NaN

non_null_columns = [col for col in copy.columns if copy.loc[:, col].notna().any()] # find the columns that are not null
copy = copy[non_null_columns] # isolate non null columns
copy.columns = [headings] # add the headings 
first_30 = copy # remove the nearly empty column

# Repeat, but use find all to get the second table, set the limit to reduce amount of tables
all_ap_tables = soup.find_all("table", attrs={"class":"wikitable"}, limit=2)
ap_table2 = all_ap_tables[1] # extract the second table
ap_table_data2 = ap_table2.tbody.findAll('tr') # turn the table into data by defining each table row (tr)

len(ap_table_data2) # check the length
ap_table_data2[0] # check the headings 

# get the headings for second table
headings2 = []
for th in ap_table_data2[0].find_all("th"):
    # remove any newlines and extra spaces from left and right
    headings2.append(th.text.replace('\n', ' ').strip())
headings2

# get the data 
info = []
df2 = []
for i in range(1,32): # ignore the headings
    info.append(ap_table_data2[i].text.replace('\n', '_').strip()) # insert _ to separate pieces of info
    temp = pd.Series(info[i]) # turn into series to split-expand
    df2.append(temp.str.split('_',expand=True)) # split into columns with expand based on _ and bc its series 
            
# get another list of dataframes
df2 = pd.concat(df2)

copy2 = df2.copy() # make a copy of the data for safety
copy2 = copy2.replace('', np.nan) # turn empty strings into NaN

non_null_columns = [col for col in copy2.columns if copy2.loc[:, col].notna().any()] # find the columns that are not null
copy2 = copy2[non_null_columns] # isolate non null columns
copy2.columns = [headings2] # add the headings 
# other data table has values in 
last_31 = copy2.drop("2019",axis=1) # remove the nearly empty column



## Additional useful call techniques for personal reference
tables = soup.findChildren('table', limit=2) # finds all of the <table>content</table> children that belong to tag html, but limit the number of tables to 2 
len(tables) # how many tables 
tables[1] # gives the first table
type(tables)
soup.table.contents[1] # can call the contents of a tag such as table
soup.children
# only need the first and second table for the 1-61
tblrows = soup.table.findChildren('tr')

len(tblrows)
tblrows[0]

tbl = soup.table
tbl.contents
soup.table.find_all(["td","a"]) # this will find all things in the first table with tags td and a

for tag in soup.find_all(True): # use this to find all the different types of tags in the soup
    print(tag.name)
    
soup.table.findAll("a", id=False) # finds all of the links for the first table
table = soup.findAll("table", limit=2)

[text for text in tbl.stripped_strings] #strips the html into readable text 
tbl.text


