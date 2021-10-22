#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[14]:


import requests

url = "https://en.wikipedia.org/wiki/Main_Page"

r = requests.get(url)

data = r.text

print(data)


# In[ ]:




