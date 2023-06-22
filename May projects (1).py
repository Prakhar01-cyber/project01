#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[2]:


train_data = pd.read_csv('Flight data_Train.csv')
train_data.head()


# In[3]:


survey_data = pd.read_csv("Surveydata_Train.csv")
survey_data.head()


# In[4]:


train_data.shape


# ###Data Cleaning

# In[5]:


train_data.isnull().sum()


# In[6]:


survey_data.isnull().sum()


# In[7]:


train_data.drop('DepartureDelayin_Mins', axis =1, inplace = True)
train_data.head()


# In[8]:



train_data['TypeTravel'].value_counts()


# In[9]:


train_data['Class'].value_counts()


# In[10]:


train_data.info()


# In[11]:


survey_data.info()


# In[12]:


train_data.describe()


# In[13]:


survey_data.describe()


# ### combine two data sets

# In[14]:


merged_dataset=pd.concat([train_data,survey_data])
merged_dataset.head()


# In[15]:


merged_dataset.drop(['ArrivalDelayin_Mins','Satisfaction','Inflightwifi_service','Inflight_entertainment','Ease_of_Onlinebooking','Onboard_service','Baggage_handling','Gate_location','Food_drink','Departure.Arrival.time_convenient','Seat_comfort','Leg_room_service','Checkin_service','Online_boarding'],axis=1,inplace=True)
merged_dataset.head()


# ### univariate analysis

# In[16]:


merged_dataset.columns


# In[17]:


merged_dataset['CustomerType'].value_counts()


# In[18]:


sns.countplot(merged_dataset['CustomerType'])
plt.show()


# In[19]:


merged_dataset['Class'].value_counts()


# In[20]:


sns.countplot(merged_dataset['Class'])
plt.show()


# In[21]:


merged_dataset['Age'].describe()


# In[22]:


sns.distplot(merged_dataset['Age'])
plt.show()


# In[23]:


merged_dataset['Flight_Distance'].describe()


# In[24]:


sns.boxplot(merged_dataset['Flight_Distance'])
plt.show()


# In[25]:


sns.displot(merged_dataset['Flight_Distance'], kde = True, )
plt.show()


# ### Bivariate analysis

# In[26]:


merged_dataset.drop(['Cleanliness','Online_support','Id'],axis=1,inplace=True)
merged_dataset.head()


# In[27]:


sns.countplot(x =merged_dataset ['CustomerType'], hue = merged_dataset['Class'])
plt.show()


# In[28]:


merged_dataset[merged_dataset['Gender'] == 'Female']['CustomerType'].value_counts(normalize = True)


# In[29]:


merged_dataset[merged_dataset['Gender'] == 'Male']['CustomerType'].value_counts(normalize = True)


# In[30]:


sns.boxplot(x = merged_dataset['CustomerType'], y = merged_dataset['Age'], hue = merged_dataset['Gender'])
plt.show()


# In[31]:


sns.violinplot(x = merged_dataset['CustomerType'], y = merged_dataset['Age'])
plt.show()


# In[32]:


sns.boxplot(x = merged_dataset['CustomerType'], y = merged_dataset['Age'])
plt.show()


# ### Conclusion:- 
# 90% customer are belonging to the loyal type and most of the customer from Loyal type take Bussiness class ticket,and Disloyal type customer take Economy class ticket.
# 

# 
