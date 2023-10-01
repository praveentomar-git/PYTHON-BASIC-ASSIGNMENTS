#!/usr/bin/env python
# coding: utf-8

# ## Q1. What is the name of the feature responsible for generating Regex objects?

# ### ANS1. re.compile() is the feature responsible for generation of Regex objects.

# In[8]:


import re
a=re.compile("string")
print(a)


# In[9]:


type(a)


# ## Q2. Why do raw strings often appear in Regex objects?

# ### ANS2. Raw strings are used so that backslashes (' \ ') do not have to be escaped.

# ## Q3. What is the return value of the search() method?

# ### ANS3. The re.search() function will search the regular expression pattern and return the first occurrence. If the pattern is found, the match object will be returned, otherwise “None” is returned.

# In[1]:


import re
search=re.search('M','Praveen Kumar Tomar',re.IGNORECASE)
print('output1 :', search)
search1=re.search('MO','Praveen Kumar Tomar',re.IGNORECASE)
print('output2 :', search1)


# ## Q4. From a Match item, how do you get the actual strings that match the pattern?

# ### ANS4. group() method will return the actual strings that match the pattern

# In[2]:


import re
match_pattern=re.search('ineuron', "Ineuron's Full Stack Data Science Program", re.IGNORECASE)
print(match_pattern.group())


# ## Q5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?

# ### ANS5. Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.

# In[7]:


import re
a=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
b=a.search('my number is 123-567-9101')


# In[8]:


b.group()


# In[9]:


b.group(0)


# In[10]:


b.group(1)


# In[12]:


b.group(2)


# ## Q6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?
ANS6. Periods and parentheses can be escaped with a backslash: \., \(, and \)
# ## Q7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?

# ### ANS7. If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.

# ## Q8. In standard expressions, what does the | character mean?

# ### ANS8. The | character signifies matching “either, or” between two groups.

# In[13]:


import re
fruits = re.compile (r'Banana|Apple Fruit')
a = fruits.search('Banana and Apple Fruit')
a.group()


# In[14]:


b=fruits.search('Apple Fruit and Banana')
b.group()


# ### When both Banana and Apple Fruit occur in the searched string, the first occurrence of matching text will be returned as the Match object.

# ## Q9. In regular expressions, what does the ?character stand for?

# ### ANS9. In regular expressions, the "?" character signifies that the preceding element is optional, matching zero or one occurrence.

# In[16]:


import re
regex = re.compile(r'Bat(wo)?man')
mo = regex.search('The Adventures of Batman')
mo.group()


# In[18]:


mo1 = regex.search('The Adventures of Batwoman')
mo1.group()


# ### Sometimes there is a pattern that you want to match only optionally. That is, the regex should find a match regardless of whether that bit of text is there. The ? character flags the group that precedes it as an optional part of the pattern.

# ## Q10.In regular expressions, what is the difference between the + and * characters?

# ### ANS10. The + matches one or more. The * matches zero or more

# ## Q11. What is the difference between {4} and {4,5} in regular expression?

# ### ANS11. The {4} matches exactly four instances of the preceding group. 
# ### The {4,5} matches between four and five instances.

# ## Q12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?

# ### ANS12. The \d, stands for single digit, Any numeric digit from 0 to 9. It is equivalent to the character range [0-9]. 
# ### \w, stands for single word, Any letter, numeric digit, or the underscore character. It is equivalent to the character range [A-Za-z0-9_].
# ### \s stands for single space character, Any space, tab, or newline character. It is commonly used to match spaces and other whitespace characters in text.
# 

# ## Q13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?

# ### ANS13.  \D - > Any character that is not a numeric digit from 0 to 9.
# ### \W - > Any character that is not a letter, numeric digit, or the underscore character.
# ### \S - > Any character that is not a space, tab, or newline.

# ## Q14. What is the difference between .*? and .* ?

# ### ANS14. The .* performs a greedy match, and the .*? performs a nongreedy match.

# In[3]:


import re

# Input string
input_string = "abc def ghi,"

# Using .*? pattern (non-greedy)
match_result = re.search(r'.*? ', input_string)
if match_result:
    print("Match using .*?:", match_result.group())

# Using .* pattern (greedy mode, it'll always try to match as much text as possible)
match_result_space = re.search(r'.*', input_string)
if match_result_space:
    print("Match using .*:", match_result_space.group())


# ## Q15. What is the syntax for matching both numbers and lowercase letters with a character class?

# ### ANS15. Either [0-9a-z] or [a-z0-9]

# In[5]:


import re
reg1 = re.compile(r'[0-9a-z]')
reg2 = re.compile(r'[a-z0-9]')

mo = reg1.search('100 times I am Reading  this for 100th time')
mo1 = reg2.search('times I am Reading  this for 100th time')
print(mo.group())
print(mo1.group())


# ## Q16. What is the procedure for making a normal expression in regax case insensitive?

# ### ANS16. Passing re.I or re.IGNORECASE as the second argument to re.compile() will make the matching case insensitive

# In[7]:


import re
case = re.compile(r'machine', re.I)
case.search('Machine learning is a part of data science').group()


# In[8]:


case.search('MACHINE learning.').group()


# ## Q17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?

# ### ANS17. The . character normally matches any character except the newline character. 
# ### If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters.

# ## Q18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?

# In[9]:


import re
numReg= re.compile(r'\d+')
match = numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')
match


# ## Q19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?

# ### ANS19. The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile()

# In[16]:


import re
# Without Using VERBOSE
regex_email = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2, 6})$', re.IGNORECASE)
 
# Using VERBOSE
regex_email = re.compile(r"""
                            ^([a-z0-9_\.-]+)              # local Part like username
                            @                             # single @ sign 
                            ([0-9a-z\.-]+)                # Domain name like google
                            \.                            # single Dot .
                            ([a-z]{2,6})$                 # Top level Domain  like com/in/org
                         """,re.VERBOSE | re.IGNORECASE)   


# ## Q20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
# '42'
# 
# '1,234'
# 
# '6,368,745'
# 
# but not the following:
# 
# '12,34,567' (which has only two digits between the commas)
# 
# '1234' (which lacks commas)

# In[18]:


import re
regex = re.compile(r'^\d{1,3}(,\d{3})*$')
for ele in ['42','1,234', '6,368,745','12,34,567','1234']:
    print('Output:',ele, '->', regex.search(ele))


# ## Q21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
# 'Haruto Watanabe'
# 
# 'Alice Watanabe'
# 
# 'RoboCop Watanabe'
# 
# but not the following:
# 
# 'haruto Watanabe' (where the first name is not capitalized)
# 
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 
# 'Watanabe' (which has no first name)
# 
# 'Haruto watanabe' (where Watanabe is not capitalized)

# In[21]:


import re
pattern = r'[A-Z]{1}[a-z]*\sWatanabe'
name = re.compile(pattern)
for i in ['Haruto Watanabe','Alice Watanabe','RoboCop Watanabe','haruto Watanabe','Mr. Watanabe','Watanabe','Haruto watanabe']:
    print('Output: ',i,'->',name.search(i))


# ## Q22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
# 'Alice eats apples.'
# 
# 'Bob pets cats.'
# 
# 'Carol throws baseballs.'
# 
# 'Alice throws Apples.'
# 
# 'BOB EATS CATS.'
# 
# but not the following:
# 
# 'RoboCop eats apples.'
# 
# 'ALICE THROWS FOOTBALLS.'
# 
# 'Carol eats 7 cats.'

# In[22]:


import re
pattern = r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'
case = re.compile(pattern,re.IGNORECASE)
for i in ['Alice eats apples.','Bob pets cats.','Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.','RoboCop eats apples.'
,'ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']:
    print('Output: ',i,'->',case.search(i))

