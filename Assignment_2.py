#!/usr/bin/env python
# coding: utf-8

# ## Q1.What are the two values of the Boolean data type? How do you write them?

# ### Ans1. 2 Values of the Boolean Data Type - True and False

# ### Firts letter capital and rest small

# In[1]:


1==1


# In[2]:


1>1


# ## Q2. What are the three different types of Boolean operators?

# ### Ans2. The logical operators ----
# 
# 1) AND - USED TO CHECK BOTH THE STATEMENTS ARE CORRECT
# 
# 2) OR - USED TO CHECK EITHER ONE OF THE STATEMENT IS TRUE
# 
# 3) NOT - REVISE THE RESULT BY USING NOT
# 
# are also referred to as boolean operators.

# ## Q3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

# ### Ans3. 

# In[3]:


# 0 is considered as False
# 1 is considered as True
andlist=[[0,0,0],[0,1,0],[1,1,1]]
print("\n AND operator's truth table ")
print (" a  b aANDb")
for i in andlist:
    print(i)


# In[4]:


orlist=[[0,0,0],[0,1,1],[1,1,1]]
print("\n OR operator's truth table ")
print (" a  b aORb")
for i in orlist:
    print(i)


# In[5]:


notlist=[[0,1],[1,0]]
print("\n NOT operator's truth table ")
print (" a  b aNOTb")
for i in notlist:
    print(i)


# ### EXAMPLES

# In[6]:


x=100
y=200
z=300


# In[7]:


x>y and y>z


# In[8]:


x>y and y<z


# In[9]:


x<y and y<z


# In[10]:


x>y or y>z


# In[11]:


x>y or y<z


# In[12]:


x<y or y<z


# In[13]:


not(x>y and y>z)


# In[14]:


not(x<y or y<z)


# ## Q4. What are the values of the following expressions?
# (5 > 4) and (3 == 5)
# 
# not (5 > 4)
# 
# (5 > 4) or (3 == 5)
# 
# not ((5 > 4) or (3 == 5))
# 
# (True and True) and (True == False)
# 
# (not False) or (not True)

# ### Ans4.

# In[15]:


(5 > 4) and (3 == 5)  # True and False output False


# In[16]:


not (5 > 4) # not (True) o/p False


# In[17]:


(5 > 4) or (3 == 5)  # True or False o/p True


# In[18]:


not ((5 > 4) or (3 == 5)) # not (True or False) --> not(True) o/p False


# In[19]:


(True and True) and (True == False) # True and False o/p False


# In[20]:


(not False) or (not True) # True or False o/p True


# ## Q5. What are the six comparison operators?

# ### Ans5. Six comparison operators---
# 
# 1. == (equal to)
# 
# 2. != (not Equal to)
# 
# 3.>  (greater than)
# 
# 4. <  (less than)
# 
# 5.>=  (greater than or equal to)
# 
# 6. <=  (less than or equal to)

# ## Q6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.

# ### Ans6. Assignment operator "=", it's used to assign the value to a variable.

# In[21]:


x=10


# In[22]:


x


# ### Comparison operator "==" (equal to), it's used to compare two values and returns True if both are same, otherwise False.

# In[23]:


100==100


# In[24]:


True==False


# ## Q7. Identify the three blocks in this code:
# spam = 0
# 
# if spam == 10:
# 
# print('eggs')
# 
# if spam > 5:
# 
# print('bacon')
# 
# else:
# 
# print('ham')
# 
# print('spam')
# 
# print('spam')

# ### Ans7.

# In[25]:


spam = 0  # 1st block
    
if spam == 10: # 2nd block
    print("eggs")  

if spam > 5: # 3rd block
    print("bacon")
else:
    print("ham")
    print("spam")
    print("spam")


# ## Q8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# ### Ans8.

# In[26]:


spam=int(input("Enter spam value : "))
if spam==1:
    print('Hello')
elif spam==2:
    print('Howdy')
else:
    print('Greetings!')


# ## Q9.If your programme is stuck in an endless loop, what keys you’ll press?

# ### Ans9. Ctrl+c (to exit from endless loop)

# ## Q10. How can you tell the difference between break and continue?

# ### Ans10. The main difference between both the statements is that when break keyword comes, it terminates the execution of the current loop and passes the control over the next loop or main body, whereas when continue keyword is encountered, it skips the current iteration and executes the very next iteration in the loop.

# In[27]:


# Break example
for letter in "string":
    if letter=="i":
        break
    print(letter)
print('The End')


# In[28]:


# Continue example
for letter in "string":
    if letter=='i':
        continue
    print(letter)
print('The End')


# ## Q11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# ### Ans11. There is no differnce in output, these are just the different ways of writting, it starts from 0 and goes upto 9 (0-9, 10 numbers) by taking the dafault increment 1.

# In[29]:


for i in range(10):
    print(i)


# In[30]:


for i in range(0,10):
    print(i)


# In[31]:


for i in range(0,10,1):
    print(i)


# ## Q12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# 

# ### Ans12.

# In[32]:


# for loop
for i in range (1,11):
    print(i)


# In[33]:


# while loop
num=1
while num<=10:
    print (num)
    num+=1


# ## Q13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

# ### Ans13.

# import spam
# 
# spm=spam.bacon()
