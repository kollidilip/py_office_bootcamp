#!/usr/bin/env python
# coding: utf-8

# 1 - Write a Regular Expression pattern to identify Date’s in a "Date_format.txt" file.
#     . Read file Date_format.txt
#     . Develop a regular Expression Pattern Using 're' library
# 
#     Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format

# #### Write a Regular Expression pattern to identify Date’s in a "Date_format.txt" file.

# In[83]:


import re
import sys
import datetime
from datetime import date,datetime


# ###### Read file Date_format.txt

# In[66]:


# load the "Date_format.txt" file
inputfile = open("E:\\Developer\\python\\tcs_py_bootcamp\\Practice 1\\Date_format.txt","r")

# read the lines and store as a list
lines_in_file = inputfile.readlines()
print(lines_in_file)


# ###### Develop a regular Expression Pattern Using 're' library

# In[67]:


def capturedates(lines_in_file,reg_ex):
    """match each line with the expression and capture the output"""
    dates_caputred = []
    for eachline in lines_in_file:
        x = re.findall(reg_ex,eachline)
        #print (x)
        if x != []:
            dates_caputred.append(x)
    return dates_caputred


# In[68]:


# declare a regular expressiom
reg_ex = r'[0-9]{1,2}-[a-zA-Z]{3}-[0-9]{4}'
dates = capturedates(lines_in_file,reg_ex)
print(dates)


# ##### Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format

# In[99]:


def changedate_format(date_input):
    """split the date to yyyy mm and dd parts and changes the format """
    splitdate = str(date_input).split('-')
    formatteddate = datetime.strptime(splitdate[2]+"-"+splitdate[1]+"-"+splitdate[0], '%d-%m-%Y').date()
    return formatteddate


# In[103]:


date_input = datetime.now().date()
formatteddate = changedate_format(date_input)
print (formatteddate)






