#!/usr/bin/env python
# coding: utf-8

# ## Q1. Why are functions advantageous to have in your programs?

# ### ANS1. Advantages of functions to have in our programs-
# ### 1. We can avoid rewriting the same logic/code again and again. (AVOID REPETATION)
# ### 2. We can call Python functions multiple times in a program.(REUSABILITY)
# ### 3. We can track a large Python program easily when it is divided into multiple functions. (MODULARITY)

# ## Q2. When does the code in a function run: when it's specified or when it's called?

# ### ANS2. The code in a function runs when it's called.

# ## Q3. What statement creates a function?

# ### ANS3. def function_name (arguments):                    #Creates a new function
# ### return arguments                              #Function Body (code to execute)
#     

# ## Q4. What is the difference between a function and a function call?

# ### ANS4. A function is a piece of code which enhanced the reusability and modularity of your program. It means that piece of code need not be written again.
# 
# ### A function call means invoking or calling that function. Unless a function is called there is no use of that function.

# ## Q5. How many global scopes are there in a Python program? How many local scopes?

# ### ANS5. One Global scope and a local scope is created whenever a function is called.

# ## Q6. What happens to variables in a local scope when the function call returns?
# 

# ### ANS6. When the function returns, the local variables are destroyed and all the variables in it are forgotten, we'll not not be able to access these outside the function.

# ## Q7. What is the concept of a return value? Is it possible to have a return value in an expression?

# ### ANS7. A function takes arguments, performs some operations and returns a value. The value that a function returns to the caller is generally known as the function's return value. A return value can be used as a part of an expression.

# ## Q8. If a function does not have a return statement, what is the return value of a call to that function?

# ### ANS8. If there is no return statement in a function, the return value of a call to that function is None.

# ## Q9. How do you make a function variable refer to the global variable?
# 

# ### ANS9. We'll use the global keyword to declare which variable is global. Example:- global a

# ## Q10. What is the data type of None?

# ### ANS10. The data type of None is NoneType.

# ## Q11. What does the sentence import areallyourpetsnamederic do?
# 

# ### ANS11. It'll throw an errror (ModuleNotFoundError) because it's not a Python module:-

# In[1]:


import areallyourpetsnamederic


# ## Q12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

# ### ANS12. We'll call it with spam.bacon()
# import spam
# 
# spam.bacon()

# ## Q13. What can you do to save a programme from crashing if it encounters an error?

# ### ANS13. We'll write our programme in try-except clause to save it from crashing if it encounters an error.

# ## Q14. What is the purpose of the try clause? What is the purpose of the except clause?

# ### ANS14. Try Clause : The code that could potentially cause an error goes in the try clause.
# ### Except Clause : The code that executes if an error happens goes in the except clause.
