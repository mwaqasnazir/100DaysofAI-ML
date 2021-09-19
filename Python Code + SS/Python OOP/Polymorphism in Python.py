#!/usr/bin/env python
# coding: utf-8

# ## Polymorphism in Python

# In[4]:


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    #Overriding the flight function of parent class
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):
    #Overriding the flight function of parent class
    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

print("Orignal Function Output\n")
obj_bird.intro()
obj_bird.flight()


# In[5]:


print("Result after overriding the function\n")
obj_spr.intro()
obj_spr.flight()


# In[6]:


print("Result after overriding the function\n")
obj_ost.intro()
obj_ost.flight()


# In[ ]:




