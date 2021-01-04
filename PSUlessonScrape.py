# This is an exercise in scraping the lesson list and objectives off of a Penn State University online statistics course
# A dataframe is created with the lesson numbers and corresponding objectives 


import requests # for making standard html requests
from bs4 import BeautifulSoup # magical tool for parsing html data
import json # for parsing data
from pandas import DataFrame as df # premier library for data organization

page = requests.get("https://online.stat.psu.edu/stat509/")
page.encoding = 'ISO-885901'
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

# this gives the main list of covered topics at the beginning of the page
# refer to this to finda shortcut to li handling later!
for tag in soup.ul.find_all("li", recursive=False): 
    print(tag.text)
# notice the information we want, the hrefs for the lessons, are in the tag 'li class'
# extract the li class information for the lessons specifically
li_class = soup.find_all('li', class_=True)

# check the length and type to see what you're working with
type(li_class) # it is a resultset. good! we can extract it like a dictionary
len(li_class) # there are 32 objects
li_class # print and see where our lessons are

lessons = li_class[12:31] # extract the important information

example = lessons[1] # create an example 
example_content = example.contents[0] # iset it in an index format
example_content.attrs # look at the attributes and see the dictionary format
example_href = example_content.attrs['href'] # extract the href

# create an empty list
lesson_hrefs = []

# begin loop to get all the hrefs for the lessons 
for i in lessons:
    con = i.contents[0]
    href = con['href']
    lesson_hrefs.append(href)
    
# we have to add in the remaining part of the hyperlink because node/*/ isn't a viable link
# create the remaining part of the link as a string
add_string = "https://online.stat.psu.edu/stat509/"
# copy the hrefs list
lesson_urls = lesson_hrefs.copy()
# use List Comprehension expression to combine two pieces of list information
final_urls = [add_string + s for s in lesson_urls]

# BTW, this is one way to combine strings, but creating a for loop implementing this is difficult   
add_string += old_string

# go into one of the href links directly as an example
page2 = requests.get(final_urls[2])
soup2 = BeautifulSoup(page2.text, 'html.parser')

#use the for loop we used before for the <ul>
# <ul> is an unordered list, the objectives at the beginning of each lesson happens to be unordered
for tag in soup2.find_all("li", class_=False): 
    print(tag.text)

lesson_objectives = soup2.find_all("li", class_=False)
len(lesson_objectives)
example2 = lesson_objectives[1]
example2_content = example2.contents[0]

# what needs to be done is to add each string per lesson together and into one cell of the list
# make a for loop that connects each string for the length of the lesson objectives

len(string1)
t = [string1]
len(t)
# Co-opt this for loop as follows...

objectives = [] # create empty list
lessons_list = []
lesson_info_list = []

for i in range(len(final_urls)): # loop through the lesson urls 
    npage = requests.get(final_urls[i])
    nsoup = BeautifulSoup(npage.text, 'html.parser')  
    for tag in nsoup.find_all("li", class_=False): 
        obj=str(tag.text)
        objectives.append(obj)
        #lessons_list.append(lessons[i])
        lesson_info_list.append(i+1) #counter 
    
#\/\/007!

import numpy as np
# convert lists to arrays
objectivesA = np.array(objectives).reshape(len(objectives),1)
lessonA = np.array(lesson_info_list).reshape(len(lesson_info_list),1)
complete = np.concatenate((lessonA, objectivesA), axis=1)
import pandas as pd
Final = pd.DataFrame(complete)
Final.columns = ("lesson", "objectives")

test[1] = Final.objectives[34] + Final.objectives[35]


type(Final.objectives[35])

np.arange(6,10)

















