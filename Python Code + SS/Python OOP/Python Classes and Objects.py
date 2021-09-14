#!/usr/bin/env python
# coding: utf-8

# ## Python Classes and Objects

# In[8]:


class Mobile:
    
    def set_Name(self,name):
        self.name= name
    
    def get_Name(self):
        print(self.name)
    
    def make_Call(self):
        output = "Making a call from mobile"
        print(output.upper())
        
    def take_Photo(self):
        output = "Taking Photographs using mobile"
        print(output.upper())

    def play_Game(self):
        output = "Playing a game on mobile"
        print(output.upper())


# In[6]:


user1 = Mobile()

user1.set_Name(input("Enter The Name of Your Mobile :" ,))
user1.get_Name()


# In[7]:


user2 = Mobile()

user2.make_Call()


# In[ ]:




