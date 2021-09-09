#!/usr/bin/env python
# coding: utf-8

# ## Generator Functions :

# In[13]:


# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)


# In[14]:


# A generator function
def simpleGeneratorFun():
    yield 'A'
    yield 'B'
    yield 'C'

# x is a generator object
x = simpleGeneratorFun()
  
# Iterating generator using next()
print(next(x))
print(next(x))
print(next(x))


# In[ ]:




