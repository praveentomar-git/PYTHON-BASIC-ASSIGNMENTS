#!/usr/bin/env python
# coding: utf-8

# ## Q1. Add the current date to the text file today.txt as a string.

# In[8]:


from datetime import date


# In[11]:


file=open('today.txt',"w")
file.write(date.today().isoformat())
file.close()


# In[16]:


file=open('today.txt','r')
print(file.read())
file.close()


# ## Q2. Read the text file today.txt into the string today_string

# In[13]:


file=open('today.txt','r')
today_string=file.read()
today_string


# ## Q3. Parse the date from today_string.

# In[27]:


from datetime import datetime
date_obj=datetime.strptime(today_string, '%Y-%m-%d')
print(date_obj)


# In[28]:


# Extracting the date, month, and year
day = date_obj.day
month = date_obj.month
year = date_obj.year

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")


# ## Q4. List the files in your current directory

# In[40]:


import os
os.listdir(".")


# ## Q5. Create a list of all of the files in your parent directory (minimum five files should be available).

# In[39]:


os.listdir("..")


# ## Q6. Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between one and five, print the current time, and then exit.

# In[57]:


import multiprocessing
import time
import random
from datetime import datetime

def worker():
    sleep_time = random.randint(1, 5)
    current_time = datetime.now()
    print(f"Process {multiprocessing.current_process().name} - Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(sleep_time)
    current_time = datetime.now()
    print(f"Process {multiprocessing.current_process().name} - Current Time After Sleep: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    processes = [multiprocessing.Process(target=worker) for _ in range(3)]
 
    for process in processes:
        process.start()
    for process in processes:
        process.join()


# In[56]:


get_ipython().system('python mutly.py')


# ## Q7. Create a date object of your day of birth.

# In[59]:


from datetime import datetime
dob=datetime.strptime('05/10/1987', '%d/%m/%Y')
print(dob)


# ## Q8. What day of the week was your day of birth?

# In[61]:


dob.strftime('%A')


# ## Q9. When will you be (or when were you) 10,000 days old?

# In[65]:


from datetime import timedelta
dob+timedelta(10000)

