#!/usr/bin/env python
# coding: utf-8

# ## Q1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.

# In[9]:


guess_me=int(input("enter any number :"))


# In[10]:


if guess_me<7:
    print("too low")
elif guess_me>7:
    print("too high")
else:
    print("just right")


# ## Q2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while loop that compares start with guess_me. Print too low if start is less than guess me. If start equals guess_me, print 'found it!' and exit the loop. If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.

# In[14]:


guess_me=7
start=1
while True:
    if start<guess_me:
        print("too low")
    elif start==guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    start+=1


# ## Q3. Print the following values of the list [3, 2, 1, 0] using a for loop.

# In[24]:


[i for i in range(3,-1,-1)]


# ## Q4. Use a list comprehension to make a list of the even numbers in range(10)

# In[25]:


even_numbers=[i for i in range(10) if i%2==0]
even_numbers


# ## Q5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.

# In[23]:


squares={i:i*i for i in range(10)}
squares


# ## Q6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

# In[26]:


odd_numbers={i for i in range(10) if i%2!=0}


# In[27]:


odd_numbers


# ## Q7. Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10). Iterate through this by using a for loop.

# In[45]:


generator_comprehension=('Got' + str(i) for i in range(10))


# In[46]:


for i in generator_comprehension:
    print(i, end=' ')


# ## Q8. Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].

# In[48]:


def good():
    lst=['Harry', 'Ron', 'Hermione']
    return lst
print(good())


# ## Q9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

# In[22]:


def get_odds():
    for number in range(1, 10, 2):
         yield number


# In[26]:


count = 1
for number in get_odds():
    if count == 3:
        print(number)
        break
    count += 1   


# ## Q10. Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print 'Caught an oops'.

# In[36]:


class OopsException(Exception):
    pass
def test(num):
    if num<0:
        raise OopsException('less than zero')
try:
    test(-10)
except Exception as e:
    print('Caught an oops ->', e)


# ## Q11. Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit', 'Crewel Fate'] and plots = ['A nun turns into a monster', 'A haunted yarn shop'].

# In[37]:


titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']


# In[38]:


movies=dict(zip(titles,plots))


# In[39]:


print(movies)

