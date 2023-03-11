#!/usr/bin/env python
# coding: utf-8

# In[1]:


#oops concept


# In[2]:


#inheritance   single


# In[3]:


class calc():
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)


# In[4]:


class calc1(calc):
    def mul(self,a,b):
        print(a*b)


# In[7]:


a = calc1()


# In[8]:


a.add(5,4)
a.sub(5,4)
a.mul(5,4)


# In[9]:


#multilevel


# In[10]:


class calc():
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)


# In[11]:


class calc1(calc):
    def mul(self,a,b):
        print(a*b)


# In[12]:


class calc2(calc1):
    def div(self,a,b):
        print(a/b)


# In[14]:


a = calc2()
a.add(5,4)
a.mul(5,4)
a.div(5,4)


# In[15]:


#multiple


# In[16]:


class calc():
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)


# In[17]:


class calc1(calc):
    def mul(self,a,b):
        print(a*b)


# In[20]:


class calc2(calc1,calc):
    
    def div(self,a,b):
        print(a/b)


# In[22]:


a = calc2()
a.add(5,4)
a.mul(5,4)
a.div(5,4)


# In[23]:


#hirearchical


# In[24]:


class calc():
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)


# In[25]:


class calc1(calc):
    def mul(self,a,b):
        print(a*b)


# In[30]:


class calc2(calc):
    
    def div(self,a,b):
        print(a/b)


# In[31]:


a = calc2()
a.add(5,4)
a.mul(5,4)
a.div(5,4)


# In[32]:


#abstract


# In[33]:


from abc import ABC,abstractmethod           #abc is said to be abstractclass


# In[35]:


class calc(ABC):
    
    @abstractmethod                  #decorater
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass


# In[36]:


class calc1(calc):
    
    def add(self,a,b):
        print(a+b)                             #inthis abstractmethod object and class name should return as same
    def sub(self,a,b):
        print(a-b)                                         
    def mul(self,a,b):
        print(a*b)


# In[37]:


a = calc1()
a.add(5,4)


# In[38]:





# In[43]:



    
from abc import ABC, abstractmethod
class employe(ABC):
    
    
    
    @abstractmethod
    def total(self):
        
        pass
    
class totalsalary(employe):
    
    def _init_(self):
        
        self.sal=int(input('enter salary = '))
        print('_____')
        self.tax=(30*self.sal)/100
        self.det=(25*self.sal)/100
        print(self.sal,'=total salary')
        print(self.tax,'=tax')
        print(self.det,"=det")
    def total(self,a):
        print(self.sal - (self.tax+self.det))
        
a=totalsalary()
a.total(a)


# In[47]:





# In[ ]:





# In[46]:


from collections import Counter

a = ["apple", "apple", "mango", "mango", "orange", "orange", "lemon", "apple"]

# Count the occurrences of each element in the list
counts = Counter(a)

# Print the counts as a dictionary
print(dict(counts)) 

# Get the elements with a count greater than 1
out = [elem for elem, count in counts.items() if count > 1]
print(out) 

# Get all the unique elements in the list
unique_elements = set(a)
print(list(unique_elements)) 


# In[ ]:




