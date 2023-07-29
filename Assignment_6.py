#!/usr/bin/env python
# coding: utf-8

# ## Q1. What are escape characters, and how do you use them?

# ### ANS1. Escape sequences allow us to include special characters in strings. To do this, simply add a backslash \ before the character we want to escape.

# ## Q2. What do the escape characters n and t stand for?

# ### ANS2. 
# - \n (Adds Newline)
# - \t (Horizontal Tab)

# ## Q3. What is the way to include backslash characters in a string?

# ### ANS3.

# In[1]:


print("way to include \\ backslash characters in a string")


# ## Q4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?

# ### ANS4.

# In[2]:


print("Howl's Moving Castle")


# ### The string is correct because we've used double quotes to mark the beginning and end of the string,  like wise we can also use double quotes within single quotes & vice-versa.

# In[3]:


print("my name is 'praveen' tomar")


# In[4]:


print('my name is "praveen" tomar')


# ## Q5. How do you write a string of newlines if you don't want to use the n character?

# ### ANS5. Multiline strings allow us to use newlines in strings without the \n escape character.

# In[5]:


print("my name is praveen tomar")
print("newlines")


# ## Q6. What are the values of the given expressions?
# 'Hello, world!'[1]
# 
# 'Hello, world!'[0:5]
# 
# 'Hello, world!'[:5]
# 
# 'Hello, world!'[3:]

# ### ANS6.

# In[6]:


'Hello, world!'[1]


# In[7]:


'Hello, world!'[0:5]


# In[8]:


'Hello, world!'[:5]


# In[9]:


'Hello, world!'[3:]


# ## Q7. What are the values of the following expressions?
# 'Hello'.upper()
# 
# 'Hello'.upper().isupper()
# 
# 'Hello'.upper().lower()

# ### ANS7.

# In[10]:


'Hello'.upper()


# In[11]:


'Hello'.upper().isupper()


# In[12]:


'Hello'.upper().lower()


# ## Q8. What are the values of the following expressions?
# 'Remember, remember, the fifth of July.'.split()
# 
# '-'.join('There can only one.'.split())

# ### ANS8.

# In[13]:


'Remember, remember, the fifth of July.'.split()


# In[14]:


'-'.join('There can only one.'.split())


# ## Q9. What are the methods for right-justifying, left-justifying, and centering a string?

# ### ANS9.

# The following methods are used for justifying strings---
# - ljust()
# - rjust()
# - center()

# In[15]:


my_str="Praveen"
my_str.ljust(20,'-')


# In[16]:


my_str="Tomar"
my_str.rjust(20,'_')


# In[17]:


my_str="Praveen Tomar"
my_str.center(20,'*')


# ## Q10. What is the best way to remove whitespace characters from the start or end?

# ### ANS10.

# lstrip() # removes white spaces from left of the string
# 
# rstrip() # removes whitespaces from right of the string

# In[18]:


my_str="       Praveen"
my_str.lstrip()


# In[19]:


my_str="Praveen         "
my_str.rstrip()

