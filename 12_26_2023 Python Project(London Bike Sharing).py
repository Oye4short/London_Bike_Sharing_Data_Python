#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Uncomment- the pip install code below if you haven't installed these libraries yet
get_ipython().system('pip install pandas')
get_ipython().system('pip install zipfile')
get_ipython().system('pip install kaggle')

# import the pandas library
import pandas as pd

# import zipfile library (we will use this to extract the file downloaded from Kaggle)
import zipfile

# import kaggle library (we will use this to download the dataset programatically from Kaggle)
import kaggle



# In[2]:


# download dataset from kaggle using the Kaggle API
get_ipython().system('kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset')


# In[6]:


# extract the file from the downloaded zip file
zipfile_name = 'london-bike-sharing-dataset.zip'
with zipfile.ZipFile(zipfile_name, 'r') as file:
    file.extractall()


# In[7]:


# read in the csv file as a pandas dataframe
bikes = pd.read_csv("london_merged.csv")


# In[8]:


bikes.info()


# In[9]:


bikes.shape


# In[10]:


bikes


# In[11]:


# count the unique values in the weather_code column
bikes.weather_code.value_counts()


# In[12]:


# count the unique values in the season column
bikes.season.value_counts()


# In[13]:


# specifying the column names that I want to use
new_cols_dict ={
    'timestamp':'time',
    'cnt':'count', 
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# Renaming the columns to the specified column names
bikes.rename(new_cols_dict, axis=1, inplace=True)


# In[14]:


# changing the humidity values to percentage (i.e. a value between 0 and 1)
bikes.humidity_percent = bikes.humidity_percent / 100


# In[15]:


# creating a season dictionary so that we can map the integers 0-3 to the actual written values
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
}

# changing the seasons column data type to string
bikes.season = bikes.season.astype('str')
# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

# changing the weather column data type to string
bikes.weather = bikes.weather.astype('str')
# mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dict)


# In[16]:


# checking our dataframe to see if the mappings have worked
bikes.head()


# In[17]:


# writing the final dataframe to an excel file that we will use in our Tableau visualisations. The file will be the 'london_bikes_final.xlsx' file and the sheet name is 'Data'
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')


# In[ ]:




