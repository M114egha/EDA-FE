#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df= pd.read_csv("zomato.csv", encoding ='latin- 1')


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df.info()


# In[6]:


df.describe()


# ##  Data Analysis
# 1. Missing values
# 2. Explore about numerical values
# 3. EXplore about categorical values
# 4. Finding relationship between features
# 

# In[7]:


df.isnull().sum()


# In[8]:


[features  for features in df.columns if df[features].isnull().sum()>0]  


# In[9]:


sns.heatmap(df.isnull() )


# In[10]:


df_country= pd.read_excel("Country-Code.xlsx")
df_country.head()


# In[11]:


df_country.shape


# In[12]:


df.columns


# ##### Combining column[Country-code] of df and df_country 

# In[13]:


final_df =pd.merge(df,df_country,on='Country Code', how='left')


# In[14]:


final_df.head(2)


# #### To chcek data types

# In[15]:


final_df.dtypes


# In[16]:


final_df.Country.value_counts()


# ###### To get the names of the country with the index

# In[17]:


country_names=final_df.Country.value_counts().index


# In[18]:


country_names


# In[19]:


country_values=final_df.Country.value_counts().values


# In[20]:


country_values


# ###### PLotting piechart for the top 3 countries

# In[21]:


plt.pie(country_values[:3],labels=country_names[:3],autopct="%1.1f%%")


# Obversation:Zomato max recors are from India

# #### Exploring relationship between features

# In[22]:


final_df.columns


# In[23]:


final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size()


# In[24]:


final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index()


# In[25]:


final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[26]:


ratings=final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[27]:


ratings


# #### Observations: 
# 1. When rating is between  4.5-4.9 ----> Excellent
# 2. When ratings are between  4.0-3.4 ----> Very good
# 3. When ratings are between  3.5-3.9 -----> Good
# 4. When rating is between  3.0-3.4 ----> Average
# 5. When rating is between  2.5-2.9 ----> Poor
# 6. When rating is between  2.0-2.4 ----> Excellent 

# In[34]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x="Aggregate rating", y="Rating Count", data= ratings)


# ###### In order to get the data as per the  above mentioned color

# In[40]:


sns.barplot(x="Aggregate rating", y="Rating Count", hue="Rating color", data= ratings,palette=['blue','red','orange','yellow','green','green'])


#  Obversation:
# 1. Not rated count is very high
# 2. Max no of rating is between 2.5 to3.4

# In[41]:


#Count plot
sns.countplot(x="Rating color",data=ratings , palette=['blue','red','orange','yellow','green','green'])


# In[42]:


# fnd the countries that has given 0 rating
final_df.head()


# In[53]:


final_df[final_df["Rating color"]=='White']


# In[56]:


final_df[final_df["Rating color"]=='White'].groupby(['Country']).size().reset_index()


# In[58]:


#Find out which currency is using which country
final_df.columns


# In[59]:


final_df['Currency']


# In[65]:


final_df.groupby(['Country','Currency']).size().reset_index()


# In[66]:


#Which countries do have online delivery option.
final_df.head()


# In[73]:


final_df[final_df["Has Online delivery"] =='Yes']


# In[76]:


final_df[final_df["Has Online delivery"] =='Yes'].groupby(['Country','Has Online delivery']).size().reset_index()


# Observations:
#  India & UAE has online delivery

# In[94]:


#Crete a piechart for the city
city_values=final_df['City'].value_counts().values


# In[95]:


city_values


# In[96]:


city_labels=final_df['City'].value_counts().index


# In[97]:


city_labels


# In[102]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct="%1.2f%%")


# In[105]:


#Find the top 10 Cuisines
final_df.groupby(['Country','Cuisines']).size().reset_index()

