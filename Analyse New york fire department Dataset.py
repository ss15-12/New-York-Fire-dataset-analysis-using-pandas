#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df_fndy_csv_data_raw=pd.read_csv('C:\\Users\\shash\\OneDrive\\Desktop\\FDNY.csv')


# In[4]:


df_fndy_csv_data_raw.describe


# In[5]:


df_fndy_csv_data_raw.head()


# In[6]:


df_fndy_csv_data=pd.read_csv('C:\\Users\\shash\\OneDrive\\Desktop\\FDNY.csv',skiprows=1)


# In[7]:


df_fndy_csv_data.head()


# In[8]:


df_fndy_csv_data.describe


# In[9]:


df_fndy_csv_data.columns


# In[10]:


df_fndy_csv_data.index


# In[11]:


df_fndy_csv_data.count()


# In[12]:


df_fndy_csv_data.dtypes


# In[13]:


groupby_borough=df_fndy_csv_data.groupby('Borough')


# In[15]:


groupby_borough.size()


# In[16]:


fndy_info_manhattan=groupby_borough.get_group('Manhattan')


# In[17]:


fndy_info_manhattan


# In[ ]:




