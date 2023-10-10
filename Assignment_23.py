#!/usr/bin/env python
# coding: utf-8
Q1. What is the result of the code, and why?
>>> def func(a, b=6, c=8):
print(a, b, c)
>>> func(1, 2)
# In[1]:


def func(a, b=6, c=8):
    print(a, b, c)
func(1, 2)


# ### ANS1. The result of the above code is `1 2 8` because the function uses the default value of c i.e. 8 which  is provided at the time of declaration.
Q2. What is the result of this code, and why?
>>> def func(a, b, c=5):
print(a, b, c)
>>> func(1, c=3, b=2)
# In[2]:


def func(a, b, c=5):
    print(a, b, c)
func(1, c=3, b=2)


# ### ANS2. When we make function call, order will be the positional argument and then keywords arguments. We can pass the keyword arguments in any order we want  but the solution will be 1,2,3.
Q3. How about this code: what is its result, and why?
>>> def func(a, *pargs):
print(a, pargs)
>>> func(1, 2, 3)
# In[3]:


def func(a, *pargs):
    print(a, pargs)
func(1, 2, 3)


# ### ANS3. `a` is assigned the value 1 (the first positional argument).
# ### The *pargs parameter collects any additional positional arguments beyond the first one and stores them in a tuple. In this case, it collects the values 2 and 3 and stores them in the pargs tuple and returns `1 (2, 3)`.
Q4. What does this code print, and why?
>>> def func(a, **kargs):
print(a, kargs)
>>> func(a=1, c=3, b=2)
# In[4]:


def func(a, **kargs):
    print(a, kargs)
func(a=1, c=3, b=2)


# ### ANS4. `a` is explicitly assigned the value 1 using the keyword argument a=1.
# ### The **kargs parameter collects any additional keyword arguments and stores them in a dictionary. In this case, it collects the keyword arguments c=3 and b=2 and stores them in the kargs dictionary.
Q5. What gets printed by this, and explain?
>>> def func(a, b, c=8, d=5): print(a, b, c, d)
>>> func(1, *(5, 6))
# In[5]:


def func(a, b, c=8, d=5): 
    print(a, b, c, d)
func(1, *(5, 6))


# ### ANS5.  `*` is the unpacking operator and are operators that unpack the values from iterable objects in Python. The single asterisk operator * can be used on any iterable that Python provides, while the double asterisk operator `**` can only be used on dictionaries.
# ### a is assigned the value 1 (the first positional argument).
# ### b is assigned the value 5 (the second positional argument).
# ### c is assigned the value 6 (the third positional argument).
# ### d is not explicitly provided, so it takes its default value of 5
Q6. what is the result of this, and explain?
>>> def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'
>>> l=1; m=[1]; n={'a':0}
>>> func(l, m, n)
>>> l, m, n
# In[13]:


def func(a, b, c):a = 2; b[0] = 'x'; c['a'] = 'y'
l=1; m=[1]; n={'a':0}
func(l, m, n)
l, m, n


# ### ANS6. In this code, the list and dict are passed as argument, and these are mutable. Here the list l and parametr b point to the same list in the memeory location where as dict n and c point to the same memory location. Any updates to this list will update in the memory location l = 1 , integer values, immutable, m is list, mutable, n is dict, mutable. Output will be = 1,['x'],{'a':'y'}
