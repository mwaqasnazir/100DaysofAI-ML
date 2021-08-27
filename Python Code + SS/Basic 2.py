#!/usr/bin/env python
# coding: utf-8

# ## Python Basic 2

# In[2]:


num1= input("Enter First Number: ")
num2= input("Enter Second Number: ")

if(num1>num2):
    print("First Number is Greather")
else:
    print("Second Number is Greater")


# In[4]:


age= int (input("Enter Your Age: "))
def AgeCalc(age):
    if(age<13):
        print("You are a child")
    elif(age>13 and age<=19):
        print("You are a Teenager")
    else:
        print("You are a adult")
        
AgeCalc(age)


# In[5]:


import keyword
print("Python Keywords List")
print(keyword.kwlist)


# In[ ]:




