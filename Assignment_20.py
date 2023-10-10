#!/usr/bin/env python
# coding: utf-8

# ## Q1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.

# In[1]:


test1 = 'This is a test of the emergency text system'


# In[2]:


fileObj=open('test.txt','w')
fileObj.write(test1)
fileObj.close()


# In[3]:


get_ipython().system(' type test.txt')


# ## Q2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?

# In[4]:


fileObj2=open('test.txt',"r")
test2=fileObj2.read()
test2


# In[5]:


test1==test2


# ## Q3. Create a CSV file called books.csv by using these lines:
# title,author,year
# 
# The Weirdstone of Brisingamen,Alan Garner,1960
# 
# Perdido Street Station,China Miéville,2000
# 
# Thud!,Terry Pratchett,2005
# 
# The Spellman Files,Lisa Lutz,2007
# 
# Small Gods,Terry Pratchett,1992

# In[6]:


data = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

with open('books.csv', 'w') as file:
    file.write(data)
    file.close()


# In[7]:


get_ipython().system('type books.csv')


# ## Q4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).

# In[26]:


import sqlite3
db=sqlite3.connect('books.db')
cursor=db.cursor()
cursor.execute("create table books (title text, author text, year int)")
db.commit()
db.close()


# ## Q5. Read books.csv and insert its data into the book table.

# In[27]:


import pandas as pd
read_books=pd.read_csv('books.csv',encoding='unicode_escape')


# In[28]:


read_books


# In[29]:


db=sqlite3.connect('books.db')
read_books.to_sql('books',db,if_exists="append", index=False)


# ## Q6. Select and print the title column from the book table in alphabetical order.

# In[30]:


db=sqlite3.connect('books.db')
cursor=db.cursor()
cursor.execute('select title from books order by title asc')
print(cursor.fetchall())


# ## Q7. From the book table, select and print all columns in the order of publication.

# In[38]:


output=cursor.execute('select * from books order by year')
for i in output:
    print(i)


# ## Q8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.

# In[32]:


import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
conn


# In[40]:


data=conn.execute('select * from books')
for i in data:
    print(i)


# ## Q9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.

# In[2]:


#!pip install redis


# In[ ]:


import redis
conn=redis.Redis()
conn.hset('test',{
    'count':1,
    'name':'Fester Bestertester'
})
conn.hgetall('test')


# ## Q10. Increment the count field of test and print it.

# In[ ]:


conn.hincrby('test','count', 3)
conn.hget('test', 'count')

