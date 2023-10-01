#!/usr/bin/env python
# coding: utf-8

# ## Q1. Create an assert statement that throws an AssertionError if the variable spam is a negative integer.

# ### ANS1. The assert statement is used to continue the execution if the given condition evaluates to True. If the assert condition evaluates to False, then it raises the AssertionError exception with the specified error message.

# In[1]:


import pyinputplus as pyip

spam = pyip.inputNum(" Enter a positive number :")
assert spam > 0
print(spam,'is a positive number')


# ## Q2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, &#39;hello&#39; and &#39;hello&#39; are considered the same, and &#39;goodbye&#39; and &#39;GOODbye&#39; are also considered the same).

# In[11]:


eggs='hello'
bacon ='HELLO'

assert eggs.upper() != bacon.upper()
print('The eggs and bacon variables are not the same!')


# ## Q3. Create an assert statement that throws an AssertionError every time.

# In[15]:


def assert_always():
    assert False, 'Always Shows Assertion Error !'
assert_always()


# ## Q4. What are the two lines that must be present in your software in order to call logging.debug()?

# In[17]:


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# ## Q5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

# In[18]:


import logging 
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


# ## Q6. What are the five levels of logging?

# ### Ans6: The Five levels of Logging provided by python's logging module are 
#     
#     logging.debug() - variable's state and small details
#     
#     logging.info() - general events, confirm a program is working
#     
#     logging.warning() - potiental problem to work on in the future
#     
#     logging.error() - record an error that caused program to fail to do something
#     
#     logging.critical() - fatal error that has caused

# ## Q7. What line of code would you add to your software to disable all logging messages?

# ###   ANS7. logging.disable(level) -> Disables all logging calls of severity 'level' and below. set level = logging.CRITICAL 
# ### since CRITICAL being the highest level , every other level loggings will be disabled.

# In[21]:


import logging
logging.disable(logging.CRITICAL)


# ## Q8.Why is using logging messages better than using print() to display the same message?

# ### ANS8. Logging offers granular control, flexibility, and integration with other tools, while print() is basic and lacks these features, making it unsuitable for larger or production-ready applications.

# ## Q9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

# ### ANS9. `Step Over:` Executes the current line of code and moves to the next line in the current function, without diving into function calls.
# 
# ### `Step In:` Steps into (enters) a function or method call, allowing us to debug within that function.
# 
# ### `Step Out:` Continues execution until the current function returns and then stops, moving the debugger to the line immediately after the function call.

# ## Q10.After you click Continue, when will the debugger stop ?

# ### ANS10. After clicking the "Continue" button in a debugger, it will stop when it reaches the next breakpoint, an exception is raised, or the program completes its execution.

# ## Q11. What is the concept of a breakpoint?

# ### ANS11. A breakpoint is a debugging tool that pauses program execution at a specified line of code for inspection and analysis.
