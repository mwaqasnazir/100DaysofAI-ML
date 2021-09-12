#!/usr/bin/env python
# coding: utf-8

# ## Python Lambda Function

# In[22]:


# As we already know that def keyword is used to define the normal functions and the lambda keyword
# is used to create anonymous functions. It has the following syntax:

# Syntax:
#  lambda arguments : expression


# In[23]:


#Use of Lembda function    
g = lambda x: x*x*x 
print(g(5)) 


# ## Use of Filter & Map Function 

# In[24]:


a = [10, 2, 8, 60, 5, 4, 30, 31, 10, 11]
  
# in filter either we use assignment or conditional operator, the pass actual 
# parameter will get return
filtered = filter (lambda x: x % 2 == 0, a) 
print(list(filtered))
  
# in map either we use assignment or conditional operator, the result of 
# the value will get returned
maped = map (lambda x: x % 2 == 0, a) 
print(list(maped))


# In[ ]:




