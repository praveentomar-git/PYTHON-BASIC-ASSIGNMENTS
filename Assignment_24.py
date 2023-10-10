#!/usr/bin/env python
# coding: utf-8

# ## Q1. What is the relationship between def statements and lambda expressions ?

# ### ANS1. `def` statements are used to create named functions with multiple statements, whereas `lambda` expressions create anonymous functions with a single expression, typically for short, inline operations. The main difference lies in their syntax and complexity.

# ## Q2. What is the benefit of lambda?

# ### ANS2. The primary benefit of lambda expressions in Python is their conciseness and ability to define small, simple functions inline. They are often used for short, one-off operations or as arguments to higher-order functions like map, filter, and sorted. 

# ## Q3. Compare and contrast map, filter, and reduce.

# ### ANS3. `map` transforms each element of an iterable and produces a new iterable of the same length.
# ### `filter`selects elements from an iterable based on a condition and produces a new iterable with a subset of elements.
# ### `reduce` accumulates values from an iterable to produce a single result. We need to import reduce from the functools module. 

# In[9]:


numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))


# In[11]:


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))


# In[14]:


from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
product


# ## Q4. What are function annotations, and how are they used?

# ### ANS4. Function annotations in Python allow us to attach metadata or type hints to function parameters and return values for documentation and type checking purposes. They are optional and do not affect the actual execution of the function. Annotations can be any object, but they are often used for type hints.

# In[18]:


def add(x: int, y: int) -> int:
    return x + y
result = add(3, 4)
result


# In[21]:


# Accessing Annotations
annotations = add.__annotations__
annotations


# ## Q5. What are recursive functions, and how are they used?

# ### ANS5. Recursive functions call themselves within their own definition to solve problems by breaking them down into smaller, similar sub-problems. They have a base case that specifies when recursion should stop and a recursive case that calls the function with a reduced problem. Recursive functions are used for problems with a natural recursive structure and can lead to concise and elegant code, but they require careful handling of the base case to avoid infinite recursion.

# In[22]:


def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


# In[24]:


factorial(5)


# ## Q6. What are some general design guidelines for coding functions?

# ### ANS6. General design guidelines for coding functions:
# 
# 1. Always use a docstring to explain the functionality of the function.
# 2. Avoid using or limited use of global variables.
# 3. Proper Identation to increase the code readability.
# 4. Try to follow a naming convention for function names (PascalCase, camelCase,snake_case) and stick with the same convention throughout the application.
# 5. Avoid using digits while choosing a variable name.
# 6. Try to use a name for the function which conveys the purpose of the function.
# 7. Local variables should be named using camelCase format `(ex: localVariable)` whereas Global variables names should be using PascalCase `(ex:GlobalVariable)`. 
# 8. Constant should be represented in allcaps `(ex:CONSTANT)`.
# 9. Don’t use non-ASCII characters in identifiers.
# 10. While naming of function of methods always use self for the first argument.

# ## Q7. Name three or more ways that functions can communicate results to a caller.

# ### ANS7. Functions can communicate results to a caller using `print` to display information, `return` to send values back, and `yield` to create iterable generators for multiple results
