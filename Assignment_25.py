#!/usr/bin/env python
# coding: utf-8

# ## Q1) What is the difference between enclosing a list comprehension in square brackets and parentheses?

# ### ANS1.
# * List Comprehension with square brackets produces list.
# * List Comprehension with parentheses creates generators.

# In[1]:


a = [ele for ele in range(10)]
print(a, type(a))
b = (ele for ele in range(10))
print(b, type(b))


# In[2]:


list(b)


# ## Q2) What is the relationship between generators and iterators?

# ### ANS2. The relationship between generators and iterators can be summarized as follows:
# 
# * Generators are a type of iterator, which means they are iterable objects.
# * Generators simplify the creation of iterators by allowing us to define them using functions with yield statements.
# * When we iterate over a generator, it executes the function until it encounters a yield statement, returns the yielded value, and then pauses the function's execution. It resumes execution from where it left off when we request the next value.
# * Iterators, on the other hand, are more general and can be implemented without using generators. They require the manual implementation of the __iter__() and __next__() methods.
# ### In summary, generators are a convenient and memory-efficient way to create iterators in Python, but all generators are iterators, while not all iterators are generators.

# In[5]:


# Iterator
iter_list = iter(['Apple', 'Orange', 'Banana'])
print(type(iter_list))
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))


# In[7]:


# Generator
def cube_number(num):
    for ele in range(num):
        yield ele**3

out_num = cube_number(4)
print(next(out_num))
print(next(out_num))
print(next(out_num))
print(next(out_num))


# ## Q3) What are the signs that a function is a generator function?

# ### ANS3. A function is recognized as a generator function if it contains atleast one yield keyword (it may contain other yiels and return statements). A generator function will always return an iterable object called generator.

# ## Q4) What is the purpose of a yield statement?

# ### ANS4. The purpose of a yield statement in Python is to produce a value from a function and temporarily pause the function's execution. This allows values to be generated lazily and efficiently one at a time, making it useful for creating iterators and generators.

# ## Q5) What is the relationship between map calls and list comprehensions? Make a comparison and contrast between the two.

# ### ANS5.
# * Map returns a map object, which needs to be converted to a list or another iterable to access the result, whereas list comprehensions directly create a list.
# * List comprehensions provide a more compact and readable syntax, especially for complex transformations and filtering.
# * Map calls may be more suitable when we want to apply the same function to multiple iterables simultaneously using multiple arguments.
# ### In short, map calls are suitable for simple element-wise transformations, while list comprehensions offer more flexibility and are often preferred for their concise and expressive syntax, especially when dealing with complex operations and conditions. The choice between the two depends on the specific use case and the desired level of readability and expressiveness.

# In[9]:


# Using map to double each element in a list
numbers = [1, 2, 3, 4, 5]
sqr_numbers = list(map(lambda x: x * 2, numbers))
print(sqr_numbers)

