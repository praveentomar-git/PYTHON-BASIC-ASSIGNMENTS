#!/usr/bin/env python
# coding: utf-8

# ## Q1.How many seconds are in an hour? Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of minutes in an hour (also 60). sol. 60

# In[1]:


print(60*60)


# ## Q2. Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.

# In[2]:


seconds_per_hour=60*60
print(seconds_per_hour)


# ## Q3. How many seconds do you think there are in a day? Make use of the variables seconds per hour and minutes per hour.

# In[5]:


hours_in_a_day=24
minutes_per_hour=60
seconds_per_minute=60
seconds_in_a_day=hours_in_a_day*minutes_per_hour*seconds_per_minute
print(seconds_in_a_day)


# ## Q4. Calculate seconds per day again, but this time save the result in a variable called seconds_per_day

# In[7]:


seconds_per_day=24*seconds_per_hour
print(seconds_per_day)


# ## Q5. Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.

# In[8]:


print(seconds_per_day/seconds_per_hour)


# ## Q6. Divide seconds_per_day by seconds_per_hour, using integer (//) division. Did this number agree with the floating-point value from the previous question, aside from the final .0?

# In[9]:


print(seconds_per_day//seconds_per_hour)


# ### Yes this number agrees with the floating-point value from the previous question, aside from the final .0

# ## Q7. Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

# In[55]:


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def genPrimes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

primes_generator = genPrimes()

print(next(primes_generator))

