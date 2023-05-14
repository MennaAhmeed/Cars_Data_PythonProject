#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data=pd.read_csv(r'C:\Users\Dell\Downloads\cars.csv')


# In[4]:


data


# In[5]:


data.head()


# In[7]:


data.shape


# In[8]:


data.dtypes


# In[9]:


data.info()


# In[14]:


data.isnull().sum()


# In[48]:


#Q1.1)Remove all null values 


# In[49]:


data.dropna(inplace=True)  #answer 


# In[50]:


data.isnull().sum()   #check


# In[26]:


#Q2. 2)( Based on Value Counts )- Check what are the different types of Make are there in our dataset. 
# And, what is the count (occurrence)of each Make in the data ?


# In[28]:


data['Make'].value_counts()  #answer


# In[29]:


#Q. 3) Instruction ( Filtering ) - Show all the records where Origin is Asia or Europe.


# In[32]:


data.head(2)


# In[33]:


data[(data['Origin']=='Asia') | (data['Origin']=='Europe')]  #answer 1


# In[35]:


data[data['Origin'].isin(['Asia','Europe'])]  #answer 2


# In[36]:


#Q. 4) Instruction ( Removing unwanted records ) - Remove all the records (rows) where Weight is above 4000.


# In[44]:


data[~(data['Weight']>4000)]  #answer 


# In[ ]:


#Q. 5) Instruction ( Applying function on a column ) - Increase all the values of 'MPG_City' column by 3.


# In[56]:


data['MPG_City']=data['MPG_City'].apply(lambda x:x+3)  #answer 

