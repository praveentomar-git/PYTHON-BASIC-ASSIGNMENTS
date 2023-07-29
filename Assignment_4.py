#!/usr/bin/env python
# coding: utf-8

# ## Q1. What exactly is []?

# ### ANS1. [] is an empty list which contains no item.

# ## Q2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
# 
# 

# ### ANS2.

# In[1]:


spam=[2,4,6,8,10]
print(spam)
spam[2]='hello' # using indexing
print(spam)


# In[2]:


spam=[2,4,6,8,10]
print(spam)
spam.insert(2,'hello') # using insert
print(spam)


# ### Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

# ## Q3. What is the value of spam[int(int('3' * 2) / 11)]?
# 

# ### ANS3.

# In[3]:


spam=['a', 'b', 'c', 'd'] 
spam[int(int('3' * 2) / 11)]


# ### STEP BY STEP CLARIFICATION:-

# In[4]:


('3'* 2)  #repeating the string 3 twice


# In[5]:


(int('3' * 2)) #converting it into the integer


# In[6]:


int(int('3' * 2) / 11) # deviding 33 by 11 and converting into integer


# In[7]:


spam[int(int('3' * 2) / 11)] #spam[3] we are searching the item at 3rd index, also note that indexing starts from zero


# ## Q4. What is the value of spam[-1]?
# 

# ### ANS4.

# In[8]:


spam[-1]  # It returns last item from the list


# ## Q5. What is the value of spam[:2]?

# ### ANS5.

# In[9]:


spam[:2] # : selects all items and 2 returns the items which are on index- 0 to 2 where 0 inclusive and 2 exclusive 


# ### Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

# ## Q6. What is the value of bacon.index('cat')?
# 

# ### ANS6.

# In[10]:


bacon=[3.14, 'cat', 11, 'cat', True] 
bacon.index('cat')    #It returns the first matching index 


# ## Q7. How does bacon.append(99) change the look of the list value in bacon?
# 

# ### ANS7.

# In[11]:


bacon.append(99)
print(bacon)  # it appends 99 at the end of the list


# ## Q8. How does bacon.remove('cat') change the look of the list in bacon?
# 

# ### ANS8.

# In[12]:


bacon.remove('cat')
print(bacon) # it removes first matching element from the list


# ## Q9. What are the list concatenation and list replication operators?
# 

# ### ANS9. For concatination we use + and for replication we use *

# In[13]:


list1=['a','b','c','d']
list2=[1,2,3,4]
print(list1+list2)
print(list1*2)


# ## Q10. What is difference between the list methods append() and insert()?
# 

# ### ANS10. append adds the element at the end of the list whie insert adds at desired index

# In[14]:


list1=['a','b','c','d']
list2=[1,2,3,4]
list1.append('praveen')
list2.insert(2,'tomar')
print(list1)
print(list2)


# ## Q11. What are the two methods for removing items from a list?
# 

# ### ANS11. pop(), remove()

# In[15]:


list1.pop()


# In[16]:


list2.remove(1)


# In[17]:


list2


# ## Q12. Describe how list values and string values are identical.
# 

# ### ANS12. 1. Both are sequences, can be passed to len(), have indexes and slices, can be used in for loops, can be concatenated or replicated, can be used with the in and not in operators.

# ## Q13. What's the difference between tuples and lists?

# ### ANS13. Lists are mutable, square brackets [ ] are used to create the lists .
# 
# ### Tuples are immutable, they cannot be changed at all, we use the parentheses / round brackets ( ) for tuples.

# ## Q14. How do you type a tuple value that only contains the integer 42?

# ### ANS14.

# In[18]:


a=(42)
b=(42,) # comma is mendatory otherwise it will create an integer


# In[19]:


print(a)
print(b)


# In[20]:


print(type(a))
print(type(b))


# ## Q15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# 

# ### ANS15.

# In[21]:


c=(2,'abc',4)
print(c)
print(type(c))


# In[22]:


d=list(c) # list() function is used to convert from tuple to list
print(d)
print(type(d))


# In[23]:


e=tuple(d) #tuple() function is used to convert from list to tuple
print(e)
print(type(e))


# ## Q16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# 

# ### ANS16. They contain reference of list values.

# ## Q17. How do you distinguish between copy.copy() and copy.deepcopy()?

# ### ANS17. copy.copy() function will create a shallow copy while copy.deepcopy() function will create a deep copy.

# In[24]:


import copy
list1=[1,2,3]
tup1=('tuple is immutable',list1)
tup2=copy.copy(tup1)      #shallow copy
print(tup2)
list1.append('list is mutable')
print(tup2)


# ### To avoid this behaviour we'll use deep copy

# In[25]:


list1=[1,2,3]
tup1=('tuple is immutable',list1)
tup2=copy.deepcopy(tup1)  # deepcopy
print(tup2)
list1.append('list is mutable')
print(tup2)

