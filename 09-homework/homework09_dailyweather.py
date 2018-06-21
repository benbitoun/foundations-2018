
# coding: utf-8

# In[1]:


import requests
import time


# In[2]:


response = requests.get('https://api.darksky.net/forecast/xxxx/46.9582,007.4277')


# In[3]:


data = response.json()


# In[4]:


data


# In[5]:


# Generate a sentence that describes the weather that day.
#Right now it is TEMPERATURE degrees out and SUMMARY. 
#Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.


# In[5]:


data.keys()


# In[6]:


temperature = data['currently']['temperature']
temperature


# In[7]:


summary = data['currently']['summary'].lower()
summary


# In[9]:


data['daily'].keys()


# In[10]:


daily_fore = data['daily']['data']
daily_fore


# In[11]:


daily_fore[0]['temperatureHigh']


# In[12]:


daily_fore[0].keys()


# In[13]:


temp_feeling = "today it's gonna be cold"
if daily_fore[0]['temperatureHigh'] > 77:
    temp_feeling = "Today it's getting hot"

elif daily_fore[0]['temperatureHigh'] > 70:
    #print("Today it's getting warm.")
    temp_feeling = "Today it's getting warm"
    
#temp_feeling


# In[14]:


rain_warning = "It's not gonna rain today. Leave your umbrella at home."

if daily_fore[0]['precipProbability'] > 0.5:
    #print("Don't forget your umbrella.")
    rain_warning = "Looks like it's gonna rain today. Don't forget your umbrella."

#rain_warning


# In[15]:


high_temp = daily_fore[0]['temperatureHigh']
high_temp


# In[16]:


low_temp = daily_fore[0]['temperatureLow']
low_temp


# In[17]:



daily_weather = "Right now it is", temperature, "Fahrenheit and", summary,".", temp_feeling, "with a high of", high_temp, "Fahrenheit and a low of", low_temp, "Fahrenheit.", rain_warning


# In[18]:


#Mailgun

requests.post(
        "https://api.mailgun.net/v3/sandboxe91bf6424a644a84a440f79b77cce655.mailgun.org/messages", #my domain name, as well
        auth=("api", "xxxx"),#same here
        data={"from": "Excited User <mailgun@sandboxe91bf6424a644a84a440f79b77cce655.mailgun.org>", #same here
              "to": "Benjamin Bitoun <benjamin.bitoun@bernerzeitung.ch>", #same here
              "subject": "Daily weather in Berne",
              "text": daily_weather}) 

