#!/usr/bin/env python
# coding: utf-8

# ## First Class Functions in Python

# In[19]:


# Python program to illustrate functions can be treated as objects
def fun1(text):
    return text.upper()

print (fun1('Muhammad Waqas Nazir'))

output = fun1

print (output("Hy, It's me Wicky"))


# In[18]:


# Python program to illustrate functions can be passed as arguments to other functions
def fun1(text):
    return text.upper()

def fun2(text):
    return text.lower()

def result(func):
    # storing the function in a variable
    output = func("""Hi, I am created by a function
                                passed as an argument.""")
    print (output)

result(fun1)
result(fun2)


# In[ ]:





# In[ ]:




