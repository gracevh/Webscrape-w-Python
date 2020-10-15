#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:51:37 2020

@author: burlios
"""


import numpy as np
import pandas as pd
import re

a = np.array([np.arange(1,21)])
a = a.reshape(-1,1)
c = pd.DataFrame(c)
c.columns = ["A"]

c = np.where(c%2 != 0, "   ", "333 Everest")
c[str.contains('[A-Za-z]')]
c.filter(regex=r'^.*[a-zA-Z].*$')
m = c[0].filter(regex=r'\D')

c.loc[c["0"].replace('[A-Za-z]',np.nan,regex=True)]
for i in c:
    if i == isalnum():
        print(i)

getVals = list([val for val in c
               if val.isalpha() or val.isnumeric()]) 
 
result = "".join(getVals) 
  
c.A.str.replace('^.*[a-zA-Z].*$', 'NaN')

for i in c:
    if i != '^.*[a-zA-Z].*$':
        
       
np.where(c != '^.*[a-zA-Z].*$', "NaN", /)        
c.loc[c["A"] != '^.*[a-zA-Z]']
c.loc[c["A"].isdigit()]

first_digit = re.search('\d', c["A"])
if first_digit is not None:
    print(first_digit.start())
    
################################################################################    
rei = pd.read_csv("rei.csv")
rei = rei.T
rei.columns = ["A"]

fuck = []
for i in range(len(rei)):
    stripped = rei.A[i].strip()
    fuck.append(stripped)

# =============================================================================
# skip empty string
# not empty make a string append stop at first empty 
# 
# shit = [] 
# for i in range(len(fuck)):
#     E += 1
# while fuck[i] != "":
#         " ".join(i, )
#     if fuck[i] == "":
#         break
#     i += 1
# =============================================================================
        
# take some info from a webpage to get the list of state abbreviations
import html5lib
# take the list of 50 state abbreviations from a web page on wikipedia
state_abbreviations = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations')
# take out the complete data frame so that it is no longer a list
fs = state_abbreviations[0]
# reduce the series into desired components
states = fs.iloc[11:62,5]
#turn series into an array so can become dataframe
states = np.array(states)
#turn array into a dataframe
states = pd.DataFrame(states, columns=["Abbrv"])
# extract the 'DC' abbreviation from the dataframe
states = states.drop(8)
states_list = states.Abbrv.tolist()

["Hello MN"] in states_list
states.str.contains("m", regex=False)


# Do the same for street abbreviations 
otr = pd.read_html('https://wiki.acstechnologies.com/display/ACSDOC/Common+Approved+Address+Abbreviations')
otr = otr[1]
# turn it into an array
otr = np.array(otr)
pd_otr = pd.DataFrame(otr)
# separate the columns so that we have nx2 dataframes 
x = pd_otr.iloc[:,:2]
y = pd_otr.iloc[:,2:4]
z = pd_otr.iloc[:,4:6]
# prepare the dataframes to remove the Â newline input by making them nan
x = np.where(x=="Â", float("NaN"), x)
y = np.where(y=="Â", float("NaN"), y)
z = np.where(z == "Â", float("NaN"), z)
# create the dataframes and name the columns
x = pd.DataFrame(x, columns = ["Name", "Abbrv."])
y = pd.DataFrame(y, columns = ["Name", "Abbrv."])
z = pd.DataFrame(z, columns = ["Name", "Abbrv."])
# now combine the dataframes into one list of dataframes
street_DFlist = [x,y,z]
# concatenate the list into one dataframe
streets = pd.concat(street_DFlist)
# drop the nan values 
streets = streets.dropna()
streets.columns = ["Name", "Abbrv"]
'ave' in streets.Abbrv
"Avenue" in streets.Name
type(streets.Name[1])
street_list = streets.Abbrv.tolist()


# remove the empty strings in the list fuck
list2 = [x for x in fuck if x]
# write to dataframe so can write to csv to fix the BS
Addresses = pd.DataFrame(list2)
Addresses.to_csv("Addresses.csv")

# split all the words in the address list so we can parse out 
splitfuck = []
for s in range(len(list2)):
    split = list2[s].split()
    splitfuck.append(split)

adr_st = []
for s in range(len(splitfuck)):
    if any([i for i in splitfuck[s] if i in states_list]):
        adr_st.append(splitfuck[s])
words = ["hi", "hey", "hello"]
' '.join(words)

# Now with fixed addresses, try to separate zipcode and state
addresses = pd.read_csv("Addresses.csv")
a = addresses["0"]
a = a.dropna()
b = addresses["Unnamed: 2"]
b = b.dropna()
a = pd.DataFrame(a)
b = pd.DataFrame(b)
# combine the two dataframes 
address = pd.concat([a, b], axis=1)
address.columns = ["street", "city"]

# test geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1 RuxitSynthetic/1.0 v6110140250 t1099441676816697146 ath9b965f92 altpub")
location = geolocator.geocode(address.city[1])
print(location.address)
latlon = (location.latitude, location.longitude)
type(latlon)

address.city[123] = 'Kennesaw, GA 30144'

coords = []
for i in address.index: # had to write .index because index is not traditional 0-N
    try: # does the loop but will skip over errors, fits well with except which will catch the skip
        loc = geolocator.geocode(address.city[i])
        (x,y) = (loc.latitude, loc.longitude) # (x,y) form is for the tuple
        coords.append((x,y))
    except: # except is triggered when the loop fails somewhere 
        print('%s failed.'%(address.city[i] # this will print what has failed 
                            ))
        coords.append((np.nan,np.nan)) # this will fill in the failed in value with nan

# The values that failed and their specific coordinates found by google 
#8300 W Emerald St, Boise, ID, 83704
    (43.6117956,-116.287805)
# 161 Town Square Pl King of Prussia, PA   19406   
    (40.082691,-75.4074344)
# 1140 Woodruff Rd. Greenville, SC   29607
    (34.8255818,-82.3031981)

coords[58] = (43.6117956,-116.287805)
coords[121] = (40.082691,-75.4074344)
coords[126] = (34.8255818,-82.3031981)    
 
# split the tuple into two separate lists   
lat, long = map(list,zip(*coords))  
    
# turn lists into arrays to combine into a dataframe 
# transpose so they are column-wise
lat = np.array([lat]).transpose()
long = np.array([long]).transpose()
# combine the two columns
fc = np.concatenate((lat,long), axis=1)

# turn into dataframe to turn into csv
final_coords = pd.DataFrame(fc, columns = ['latitude', 'longitude'])    
  
# make csv
final_coords.to_csv("ReiCoords.csv")  

"""    
Now that the information is in R for the coordinates, let's gather other information about the 
landscape of the US and recreational activity.  
    
"""
    