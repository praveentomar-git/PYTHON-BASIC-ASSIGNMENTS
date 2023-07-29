#!/usr/bin/env python
# coding: utf-8

# ## Q1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# ' * 
#   
# 'hello'
# 
# -87.8
# 
# -
# 
# /
# 
# ' +	
# 
# 6 

# ### Ans1. Values are as follows:-
# 
# ### 'hello', -87.8 , 6
# 
# ### Expressions are as follows:-
# 
# ### *, -, /, +

# ## Q2. What is the difference between string and variable?

# ### Ans2. String is the sequence of characters, also called object. String literals in Python are surrounded by either single quotation mark or double quotation mark. Ex. a="Python is a programming language"
# V/S
# ### Variable is a characteristic of any entity that is capable of taking different values. In Python- Variable is a name given to the memory location where the value is stored in the memory. Ex. X=1 or X=2 or X=3, etc. X is variable.

# In[1]:


a="Python is a programming language"


# In[2]:


a


# In the above given example-
# 
# STRING is 'Python is a programming language'
# 
# &
# VARIABLE is a

# ## Q3. Describe three different data types.

# ### Ans3. 3 Different data types in Python-
# 1) NUMERIC DATA TYPES:-
# 
# a) Integer - Whole number, positive or negative without decimals of unlimited length. Ex. 1,2,4,6666,-4555,9999999, etc.
# 
# b) Float - A number, positive or negative, containing one or more decimals. Ex. 1.o, 1.45, -1.98765, 7.0987, etc.
# 
# 2) STRING DATA TYPES - Sequence of characters, also called object. String literals in Python are surrounded by either single quotation mark or double quotation marks. Ex. "Hello", "Python", "Pkt123", etc.
# 
# 3) BOOLEAN DATA TYPES - There can only be 2 values of such data type. Ex -  True or False. 

# ## Q4. What is an expression made up of? What do all expressions do?

# ### Ans4. An Expression is a sequence or combination of values, variables, operators and function calls that always produces or returns a result value.
# 
# Example: x = 5, y = 3, z = x + y
# 
# In the above example x, y and z are variables, 5 and 3 are values, = and + are operators.
# 
# So, the first combination x = 5 is an expression, the second combination y = 3 is an another expression and at last, z = x + y is also an expression.
# 
# ### An Expression always evaluates (calculate) to itself.

# ## Q5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# ### Ans5. Any Instruction (command) that a Python interpreter can execute (carry out) is called a statement.
# 
# Each and every line of code that we write in any programming language is called a statement.
# 
# Because, all the lines are executable by the interpreter or the compiler of that programming language.
# 
# ### The assignment statement assign a value to the variable.
# 
# ### spam=10, here we have created a varibale which name is spam and we have given/assigned a value to spam i.e. 10.
# 
# print(spam) - It's a print statement that displays the value of spam.
# 
# ### Difference b/w Expression and Statement:-
#  1) An expression evaluates to a value	while a statement executes something
#  
# 2) Evaluation of an expression always produces or returns a result value while execution of a statement may or may not produces or displays a result value, it only does whatever the statement says.
# 
# 3) Every expression can’t be a statement while every statement can be an expression.

# ## Q6. After running the following code, what does the variable bacon contain?
# 
# bacon = 22
# 
# bacon + 1

# ### Ans6. 22

# ### bacon is assigned 22 but bacon+1 is not assigned, so it would contain the same value i.e. 22

# In[3]:


bacon = 22
bacon + 1


# In[4]:


bacon


# ## Q7. What should the values of the following two terms be?
# 
# 'spam' + 'spamspam'
# 
# 'spam' * 3

# ### Ans7. 'spamspamspam' 
# 
# ### 'spamspamspam'

# In[5]:


'spam' + 'spamspam'


# In[6]:


'spam' * 3


# ## Q8. Why is eggs a valid variable name while 100 is invalid?

# ### Ans8. Variable can not start with a number, It can only contains alpha-numeric characteristics and underscore, resreved words should not be used, it's case sensitive. That's why eggs is valid variable name but 100 is invalid.

# ## Q9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# ### Ans9. int(), float(), str()

# In[7]:


a=100


# In[8]:


type(a)


# In[9]:


b=float(a)


# In[10]:


b


# In[11]:


type(b)


# In[12]:


c=str(a)


# In[13]:


c


# In[14]:


type(c)


# ## Q10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'

# ### Ans10. This expression causes an error because we are trying to concatenate string & integer.
# 
# ### It can be fixed by converting the 99 from integer to string using single/double quote/str().

# In[15]:


'I have eaten ' +str(99) + ' burritos.'


# In[16]:


'I have eaten ' + "99" + ' burritos.'


# In[17]:


'I have eaten ' + '99' + ' burritos.'

