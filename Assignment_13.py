#!/usr/bin/env python
# coding: utf-8

# ## Q1. What advantages do Excel spreadsheets have over CSV spreadsheets?

# ### ANS1. Excel spreadsheets offer advantages over CSV files by providing data formatting, formulas, charts, data validation, multiple sheets, and advanced data analysis tools. These features make Excel more suitable for tasks involving data visualization, complex calculations, and structured data organization. CSV files, while simpler and widely compatible, lack these capabilities.

# ## Q2.What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

# In[24]:


import csv
with open('tips.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
        print(i)


# In[23]:


data_to_write = [
    ['Name', 'Tip'],
    ['Alice', 25],
    ['Bob', 30],
    ['Charlie', 22]]
with open('tips.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file, delimiter='\t', lineterminator='\n\n')
    csv_writer.writerows(data_to_write)


# ## Q3. What modes do File objects for reader and writer objects need to be opened in?

# ### ANS3. For `csv.reader()`: We pass an open file object in read mode (with 'r' or 'rb' for binary mode)  that contains the CSV data we want to read.
# ### For `csv.writer()`: We pass an open file object in write mode (with 'w' or 'wb' for binary mode) where we want to write the CSV data. Be cautious when opening a file in write mode, as it will overwrite the existing contents of the file if it already exists.

# ## Q4. What method takes a list argument and writes it to a CSV file?

# ### ANS4: csv.writer() class provides two methods for writing to CSV. They are `writerow()` and `writerows().` writerow() method writes a single row at a time. Whereas writerows() method is used to write multiple rows at a time.

# ## Q5. What do the keyword arguments delimiter and line terminator do?

# ### ANS5.  The delimiter argument changes the string used to separate cells in a row. 
# ### The lineterminator argument changes the string used to separate rows.

# ## Q6. What function takes a string of JSON data and returns a Python data structure?

# ### ANS6. `loads()` method takes a string of JSON data and returns a Python data structure.

# In[5]:


import json
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)

# Access and work with the Python data structure
print(data["name"])
print(data["age"])   
print(data["city"])


# In[7]:


type(data)


# ## Q7. What function takes a Python data structure and returns a string of JSON data?

# ### ANS7: `dumps()` method takes a python data structure and returns a string of JSON data

# In[2]:


import json
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
json_string = json.dumps(data)
print(json_string)


# In[4]:


type(json_string)

