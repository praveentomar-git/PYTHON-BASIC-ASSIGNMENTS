#!/usr/bin/env python
# coding: utf-8

# ## Q1. What does an empty dictionary's code look like?

# ### ANS1.

# In[1]:


dic={}  # empty dictionary


# In[2]:


print(dic)
print(type(dic))


# ###### or

# In[3]:


d=dict()
print(d)
print(type(d))


# ## Q2. What is the value of a dictionary value with the key 'foo' and the value 42?

# ### ANS2.

# In[4]:


dic_2={'foo':42}
dic_2


# ## Q3. What is the most significant distinction between a dictionary and a list?

# ### ANS3. Dictionary holds keys and values pairs while list holds objects of differnt types. List is ordered while dictionary is unordered collection of items.

# ## Q4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

# ### ANS4.

# In[5]:


spam={'bar':100}


# In[6]:


spam['foo']


# ### It'll throw a KeyError:    'foo'

# ## Q5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 

# ### ANS5. There is no difference because in operator checks whether a value exists as a key in the dictionary.

# In[7]:


spam2={'cat':44}


# In[8]:


'cat' in spam2


# In[9]:


'cat' in spam2.keys()


# ## Q6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 

# ### ANS6. 'cat' in spam checks whether there is a 'cat' key in the dictionary while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

# In[10]:


spam3={44:'cat'}


# In[11]:


'cat' in spam3  


# ### It will check in keys only, so it's showing False

# In[12]:


'cat' in spam3.values()


# ### It will check in values only, so it's showing True

# ## Q7. What is a shortcut for the following code?
# ## if 'color' not in spam:
# ## spam['color'] = 'black'
# 
# 

# ### ANS7. 

# In[13]:


# if 'color' not in spam:spam['color'] = 'black'
# shortcut code
spam.setdefault('color','black')
print(spam)


# ## Q8. How do you "pretty print" dictionary values using which module and function?

# ### ANS8. We'll print the pretty print using pprint() function of pprint module but it'll not prettify nested dictionaries then we'll use dump() function of yaml module.

# In[14]:


dict_1 = [{'Name': 'Praveen', 'Age': '30', 'Residence': {'Country':'India', 'City': 'Gurgaon'}},
          {'Name': 'Sachin', 'Age': '27', 'Residence': {'Country':'Spain', 'City': 'Madrid'}}]


# In[15]:


print('using print function:\n', dict_1)


# In[16]:


import pprint
print('using pprint function of pprint module:')
pprint.pprint(dict_1)


# In[17]:


dict_2 = {'Name': ['Praveen', 'Sachin'], 'Age': [30, 27], 'Residence': [{'Country':'India', 'City': 'Gurgaon'},{'Country':'Spain', 'City': 'Madrid'}]}
print('using print function:\n', dict_2)


# In[18]:


import yaml
dump=yaml.dump(dict_2)
print('using dump function of yaml module:\n',dump)

