#!/usr/bin/env python
# coding: utf-8

# ## Q1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.

# In[8]:


get_ipython().run_cell_magic('writefile', 'zoo.py', "def hours():\n    print('Open 9-5 daily')\n")


# In[9]:


import zoo
zoo.hours()


# ## Q2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.

# In[10]:


import zoo as menagerie
menagerie.hours()


# ## Q3. Using the interpreter, explicitly import and call the hours() function from zoo.

# In[12]:


from zoo import hours
hours()


# ## Q4. Import the hours() function as info and call it.

# In[13]:


from zoo import hours as info
info()


# ## Q5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.

# In[18]:


plain=dict([('a', 1), ('b', 2),('c', 3)])


# In[19]:


plain


# ## Q6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?

# In[22]:


from collections import OrderedDict
fancy=OrderedDict([('a', 1), ('b', 2),('c', 3)])
fancy


# ## Q7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

# In[23]:


from collections import defaultdict
dict_of_lists=defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])

