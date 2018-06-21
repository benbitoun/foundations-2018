
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get('http://www.nytimes.com')
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


# ## What are the containers of the stories on the NYT website???
stories = doc.find_all(class_='story')
len(stories)


# In[4]:


# * 'story-heading' is the title
# * 'byline' is the byline
list_of_stories = []

for story in stories:
    story_dict = {}
    headline = story.find(class_='story-heading')
    byline = story.find(class_='byline')
    if headline:
        story_dict['headline'] = headline.text.strip()
    if byline:
        story_dict['byline'] = byline.text.strip()
    list_of_stories.append(story_dict)

list_of_stories


# In[5]:


df = pd.DataFrame(list_of_stories)
df.head()


# In[6]:


import datetime

right_now = datetime.datetime.now()
right_now


# In[7]:


right_now.strftime("%Y-%m-%d_%H_%M_%S")


# In[8]:


nyt_6pm_briefing = "nyt-" + right_now.strftime("%Y-%m-%d_%H_%M_%S") + ".csv"
df.to_csv(nyt_6pm_briefing, index=False)


# In[9]:


nyt_6pm_briefing


# In[10]:


requests.post(
        "https://api.mailgun.net/v3/sandboxe91bf6424a644a84a440f79b77cce655.mailgun.org/messages",
        auth=("api", "xxxxx"),
        files=[("attachment", open("nyt-2018-06-21_14_19_00.csv"))],
        data={"from": "Excited User <mailgun@sandboxe91bf6424a644a84a440f79b77cce655.mailgun.org>",
              "to": "Benjamin Bitoun <benjamin.bitoun@bernerzeitung.ch>",
              "subject": "NY Times scrape",
              "text": nyt_6pm_briefing}) 

