#!/usr/bin/env python
# coding: utf-8

# ## Q1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].

# In[1]:


years_list=list(range(1987,1987+6))


# In[2]:


years_list


# ## Q2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.

# In[3]:


years_list[3]


# ## Q3.In the years list, which year were you the oldest?

# In[4]:


years_list[-1]


# In[15]:


max(years_list)


# ## Q4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".

# In[16]:


things=[ele for ele in ["mozzarella", "cinderella", "salmonella"]]


# In[19]:


things


# ## Q5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?

# In[13]:


for ele in range(len(things)):
    if things[ele] == 'cinderella':
        things[ele]=things[ele].capitalize()
print(things)


# ## Q6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."

# In[27]:


surprise_list=["Groucho","Chico","Harpo"]


# In[28]:


surprise_list


# ## Q7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.

# In[29]:


surprise_list[-1].lower()


# In[30]:


surprise_list[-1]=surprise_list[-1].lower()[::-1]


# In[32]:


surprise_list[-1]


# In[31]:


surprise_list[-1].upper()


# ## Q8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.

# In[36]:


e2f={'dog':'chien', 'cat':'chat', 'walrus': 'morse'}


# In[37]:


e2f


# ## Q9. Write the French word for walrus in your three-word dictionary e2f.

# In[39]:


e2f['walrus']


# ## Q10. Make a French-to-English dictionary called f2e from e2f. Use the items method.

# In[69]:


dict([i[::-1] for i in e2f.items()])


# In[64]:


f2e=dict((key,value) for value,key in e2f.items())


# In[65]:


f2e


# ## Q11. Print the English version of the French word chien using f2e.

# In[70]:


f2e.get('chien')


# ## Q12. Make and print a set of English words from the keys in e2f.

# In[73]:


list(e2f.keys())


# ## Q13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.

# In[85]:


life={
    "animals":{
        "cats":['Henri', 'Grumpy','Lucy'],
        "octopi":{},
        "emus":{}
    },
    "plants":{},
    "others":{}
}


# In[86]:


life


# ## Q14. Print the top-level keys of life.

# In[87]:


life.keys()


# ## Q15. Print the keys for life['animals'].

# In[88]:


life['animals'].keys()


# ## Q16. Print the values for life['animals']['cats'].

# In[90]:


life['animals']['cats']

