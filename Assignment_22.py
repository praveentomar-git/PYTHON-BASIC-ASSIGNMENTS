#!/usr/bin/env python
# coding: utf-8
Q1. What is the result of the code, and explain?


>>> X = 'iNeuron'
>>> def func():
print(X)


>>> func()
# ### ANS1. There is a global variable X defined with the string value 'iNeuron', and a function func defined. Inside the func function, it attempts to print the value of the variable X.
# 
# ### When we call the func() function at the end of the code, it will execute the function and the print(X) statement inside the function will print the value of the global variable X. 

# In[2]:


X = 'iNeuron'
def func():
    print(X)

func()

Q2. What is the result of the code, and explain?


>>> X = 'iNeuron'
>>> def func():
X = 'NI!'


>>> func()
>>> print(X)

# ### ANS2. We define a global variable X with the value 'iNeuron'.
# 
# ### We define a function func, but inside this function, we also define a local variable X with the value 'NI!'. This local variable shadows (hides) the global variable X within the function's scope.
# 
# ### When we call the func() function, it doesn't return or print anything, but it does create and use the local variable X with the value 'NI!'.
# 
# ### After calling the function, we print the value of the global variable X using print(X). Since the global variable X was not modified inside the function and the local variable inside the function doesn't affect the global scope, this will print the global variable's value.

# In[2]:


X = 'iNeuron'
def func():
    X = 'NI!'

func()
print(X)

Q3. What does this code print, and why?


>>> X = 'iNeuron'
>>> def func():
X = 'NI'
print(X)


>>> func()
>>> print(X)

# ### ANS3. We define a global variable `X` with the value `iNeuron`.
# ### We define a function `func`, but inside this function, we also define a local variable `X` with the value `NI!`. 
# ### When we call the `func()` function, It prints the value of the local variable `X` inside the function, which is `NI!`.
# ### After calling the function, we print the value of the global variable `X` using `print(X)`. This will print the global variable's value.

# In[3]:


X = 'iNeuron'
def func():
    X = 'NI'
    print(X)

func()
print(X)

Q4. What output does this code produce? Why?


>>> X = 'iNeuron'
>>> def func():
global X
X = 'NI'


>>> func()
>>> print(X)
# ### ANS4. We define a global variable X with the value iNeuron.
# ### We define a function func, inside this function, we declare X as  a global variable using the global keyword, which means that we are telling Python to refer to the global variable X within the function.
# ### When we call the func() function, It sets the global variable X to NI.
# ### After calling the function, we print the value of the global variable X using print(X). Since the func function modified the global variable X to 'NI', the value of X has changed, and it will print 'NI'.

# In[7]:


X = 'iNeuron'
def func():
    global X
    X = 'NI'

func()
print(X)

Q5. What about this code—what’s the output, and why?


>>> X = 'iNeuron'
>>> def func():
X = 'NI'
def nested():
print(X)
nested()


>>> func()
>>> X
# ### ANS5. We define a global variable X with the value 'iNeuron'.
# 
# ### We define a function func. Inside the func function and define a local variable X with the value 'NI'.
# 
# ### Inside the func function, we define another nested function nested. This nested function attempts to print the value of the variable X.
# 
# ### When we call the func() function, it first sets the local variable X within its own scope to 'NI'.
# 
# ### Inside the func function, we call the nested() function, which prints the value of the local variable X within its own scope. Since there is a local variable X defined in the func function's scope, this print(X) statement inside the nested function will print 'NI'.
# 
# ### After calling the func function, we have an expression X that gives output as iNeuron.

# In[4]:


X = 'iNeuron'
def func():
    X = 'NI'

    def nested():
        print(X)
    nested()
func()
X

Q6. How about this code: what is its output in Python 3, and explain?

>>> def func():
X = 'NI'
def nested():
nonlocal X
X = 'Spam'
nested()
print(X)


>>> func()  
# ### ANS6. When we call the func() function, it sets the local variable X within its own scope to 'NI'.
# 
# ### Inside the func function, we call the nested() function. Within the nested function, we use the nonlocal keyword to indicate that we want to modify the nearest enclosing variable named X. This means that the X in the func function's scope is modified, and it becomes 'Spam'.
# 
# ### After calling the nested function, we print the value of the variable X within the func function's scope using print(X). Since X was modified with the nonlocal keyword inside the nested function, it will print 'Spam'.

# In[13]:


def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)

func()

