#!/usr/bin/env python
# coding: utf-8

# ## Q1. Is the Python Standard Library included with PyInputPlus?

# ### Ans1: No, `PyInputPlus` is not a part of Python Standard Library, it needs to be installed explicitly using the command `!pip install pyinputplus`

# In[6]:


get_ipython().system('pip install pyinputplus')


# ## Q2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?

# **Ans2:**  pypi is alias of PyInputPlus.
# 
# The as **pyip** code in the import statement saves us from typing pyinputplus each time we want to call a PyInputPlus function. Instead we can use the shorter pyip name

# In[9]:


import pyinputplus as pyip


# ## Q3. How do you distinguish between inputInt() and inputFloat()?

# ### ANS3. inputInt() : Accepts an integer value, and returns int value
# ### inputFloat() : Accepts integer/floating point value and returns float value
# ### Both takes additional parameters ‘min’, ‘max’, ‘greaterThan’ and ‘lessThan’  for bounds

# In[14]:


import pyinputplus as pyip
pyip.inputInt()


# In[15]:


pyip.inputFloat()


# ## Q4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

# ### ANS4. In the inputint function we can set the min = 0 and max =99 to ensure user enters number between 0 and 99

# In[12]:


import pyinputplus as pyip
pyip.inputInt(min = 0, max =99)


# ## Q5. What is transferred to the keyword arguments allowRegexes and blockRegexes?

# **Ans5:** we can use **`allowRegexes`** and **`blockRegexes`** keyword arguments to take list of regular expression strings to determine what the pyinputplus function will reject or accept valid input.

# In[16]:


a = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero']) # it allows roman letters as numbers too


# In[17]:


b = pyip.inputNum(blockRegexes=[r'[02468]$'])# blocks the even numbers


# ## Q6. If a blank input is entered three times, what does inputStr(limit=3) do?

# ### ANS6. It raises an eception `RetryLimitException`

# In[20]:


pyip.inputStr(limit=3)


# ## Q7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?

# ### ANS7. When we use limit keyword arguments and also pass a default keyword argument, the function returns the default value instead of raising an exception.

# In[21]:


pyip.inputStr(limit=3, default='hello') 

