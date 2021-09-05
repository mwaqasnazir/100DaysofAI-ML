#!/usr/bin/env python
# coding: utf-8

# ## Break statement

# In[3]:


w = 'mwaqasnazir'
for letter in s:
  
    print(letter)
    # break the loop as soon it sees 's' or 'n'
    if letter == 's' or letter == 'n':
        break
  
print("Out of for loop")
print()


# ## Continue statement

# In[7]:


# loop from 1 to 10
for i in range(1, 11):
 
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 2 or i == 4:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")


# ## Pass statement

# In[8]:


a = 10
b = 20
 
if(a<b):
  pass
else:
  print("b<a")


# In[ ]:




