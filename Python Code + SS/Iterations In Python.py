#!/usr/bin/env python
# coding: utf-8

# ## Iterations In Python

# ## While Loop

# In[20]:


i = 1
while (i < 4):
    print("Num", i)
    i += 1


# In[6]:


#Iteration by while loop for a condition
# Guessing Game

i=0  #its just like chances
n=5
while (i<3):
    n2= int (input("Guess a Number: "))
    if(n2 == n):
        i=3
        print("You Guess the Number !")
    else:
        i +=1
if(i==3 and n==n2):
    print("Yow Win !")
else:
    print("Game is over!")


# ## For Loop

# In[13]:


# Iteration by for loop on strings
name = input("Enter Your Name: ")
for i in name :
    print (i)


# In[14]:


# Iteration by for loop on list
even_num = [2, 4, 6, 8, 10]
for  i in even_num:
    print (i)


# In[10]:


#Iteration by For loop for a condition
# Guessing Game

i=0  #its just like chances
n=5

for i in range(3):
    
    n2= int (input("Guess a Number: "))
    if(n2 == n):
        i=3
        print("You Guess the Number !")
    else:
        i +=1
        
if(i==3 and n==n2):
    print("Yow Win !")
else:
    print("Game is over!")
    


# In[ ]:




