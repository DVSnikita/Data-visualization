#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Required Libraies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Loddind datasets  (df1: Airbnb, df2: HR_dataset)
df1 = pd.read_csv("Airbnb_Dataset.csv")
df2 = pd.read_csv("HR_Dataset.csv")


# In[3]:


# Airbnb Dataset 
df1.head()


# In[4]:


# Hr Darataset
df2.head()


# In[5]:


# datasets shape
df1.shape


# In[6]:


df2.shape


# In[7]:


# Features data-type
df1.info()


# In[8]:


df2.info()


# In[9]:


# Count of null values
df1.isnull().sum()


# In[10]:


df2.isnull().sum()


# In[11]:


# Replacing zero values with NaN
df1[['number_of_reviews','availability_365']] = df1[['number_of_reviews', 'availability_365']].replace(0,np.NaN)


# In[12]:


# After replacing zero into NaN count of null values
df1.isnull().sum()


# In[13]:


# Replacing NaN with mean values
df1["number_of_reviews"].fillna(df1["number_of_reviews"].mean(), inplace = True)
df1["reviews_per_month"].fillna(df1["reviews_per_month"].mean(), inplace = True)
df1["availability_365"].fillna(df1["availability_365"].mean(), inplace = True)


# In[14]:


df1.isnull().sum()


# ## 10 diffrent Visualization and purpose of visualizations

# ## 1.Distribution of Prices (Histogram):
# 
# Purpose: Shows the range and frequency of listing prices.

# In[15]:


plt.figure(figsize=(10, 6))
sns.histplot(df1['price'], bins=30, kde=True)
plt.title('Distribution of Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()


# ## 2.Room Types by Neighborhood Group (Countplot):
# 
# Purpose: Compares the availability of different room types across various neighborhoods.

# In[16]:


plt.figure(figsize=(12, 8))
sns.countplot(data=df1, x='neighbourhood_group', hue='room_type')
plt.title('Room Types by Neighborhood Group')
plt.xlabel('Neighborhood Group')
plt.ylabel('Count')
plt.legend(title='Room Type')
plt.show()


# ## 3.Number of Reviews per Month (KDE Plot):
# 
# Purpose: Highlights listings' popularity based on review frequency.

# In[17]:


plt.figure(figsize=(10, 6))
sns.kdeplot(df1['reviews_per_month'], shade=True)
plt.title('Number of Reviews per Month')
plt.xlabel('Reviews per Month')
plt.ylabel('Density')
plt.show()


# ## 4.Availability by Room Type (Boxplot):
# 
# Purpose: Indicates how many days listings are available based on room type.

# In[18]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df1, x='room_type', y='availability_365')
plt.title('Availability by Room Type')
plt.xlabel('Room Type')
plt.ylabel('Availability (days)')
plt.show()


# ## 5.Number of Listings by Host (Histogram):
# 
# Purpose: Displays the distribution of the number of listings per host.

# In[19]:


plt.figure(figsize=(10, 6))
sns.histplot(df1['calculated_host_listings_count'], bins=30, kde=True)
plt.title('Number of Listings by Host')
plt.xlabel('Number of Listings')
plt.ylabel('Frequency')
plt.show()


# ## 6.Gender Distribution (Pie Chart):
# 
# Purpose: Provides an overview of the gender composition in the company.

# In[20]:


gender_counts = df2['Sex'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.show()


# ## 7.Average Salary by Department (Barplot):
# 
# Purpose: Shows salary variations across different departments.

# In[21]:


plt.figure(figsize=(12, 8))
sns.barplot(data=df2, x='Department', y='Salary')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.show()


# ## 8.Employee Satisfaction by Department (Boxplot):
# 
# Purpose: Illustrates employee satisfaction levels in each department.

# In[22]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=df2, x='Department', y='EmpSatisfaction')
plt.title('Employee Satisfaction by Department')
plt.xlabel('Department')
plt.ylabel('Satisfaction')
plt.xticks(rotation=45)
plt.show()


# ## 9.Performance Scores by Employment Status (Stacked Barplot):
# 
# Purpose: Compares performance scores across different employment statuses.

# In[23]:


performance_status = df2.pivot_table(index='EmploymentStatus', columns='PerformanceScore', aggfunc='size', fill_value=0)
performance_status.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Performance Scores by Employment Status')
plt.xlabel('Employment Status')
plt.ylabel('Count')
plt.legend(title='Performance Score')
plt.xticks(rotation=45)
plt.show()


# ## 10.Absences by State (Barplot):
# 
# Purpose: Highlights the number of absences in each state.

# In[24]:


plt.figure(figsize=(10, 6))
sns.barplot(data=df2, x='State', y='Absences')
plt.title('Absences by State')
plt.xlabel('State')
plt.ylabel('Number of Absences')
plt.xticks(rotation=45)
plt.show()


# In[ ]:





# In[ ]:




