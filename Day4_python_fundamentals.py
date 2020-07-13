#!/usr/bin/env python
# coding: utf-8

# In[61]:


students =('sai','dattu','kiran','kartik','murthy',)
print(students)


# In[62]:


print(students[2])


# In[63]:


print(students[2].title())


# In[51]:


#req: replace kiran with sajid


# In[69]:


students[2] = 'raju'


# In[70]:


print(students)


# In[71]:


#req to add baby to thge list of the above


# In[74]:


students.append('baby')
print(students)


# In[75]:


#req to add laxmi at the  index position


# In[79]:


students.insert(3,'laxmi')
print(students)


# In[80]:


#req: sai from the list


# In[81]:


del students[0]
print (students)


# In[87]:


x =students.pop()
print(students)


# In[88]:


print(x)


# In[89]:


y =students .pop (3)
print(students)


# In[90]:


print(y)


# In[ ]:




