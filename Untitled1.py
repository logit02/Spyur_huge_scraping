#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup 
import pandas as pd
import time


# In[2]:


html = requests.get("https://www.spyur.am/am/home/search-1/?company_name=գործարան")

page = html.content 

page=BeautifulSoup(page,'html.parser')

zavod = []

base_link = 'https://www.spyur.am/am/home/search-'

all_link = [base_link + str(i) + '/?company_name=գործարան' for i in range(1,46)]


# In[3]:


for i in all_link:
    html = requests.get(i)
    page = html.content
    page=BeautifulSoup(page,'html.parser')
    for item in page.findAll('div', {'class':"current-company"}):
        for each in item.findAll('a'):
            zavod.append(each.get('href'))


# In[4]:


zavod = list(set(zavod))


# In[5]:


itemed_link  = ['https://www.spyur.am' + str(i) for i in zavod]


# In[6]:


names = []


# In[195]:


final=[]


# In[196]:



from tqdm import tqdm

for z in tqdm(itemed_link):
    web=[]
    html = requests.get(z)       
    page = html.content
    page=BeautifulSoup(page,'html.parser')
    for element in page.findAll('h2',{'class':'company_name'}):
        anun = element.text
    if(page.find(id='address')):
        for d in page.find(id='address'):
            for q in d.findAll('a'):
                if(q.text):
                    hamar = q.text
                else:
                    hamar = 'undefined'
            
    else:
        hamar = 'undeifned'
    if(page.find(id='otherData')):  
        for b in (page.find(id='otherData')):
            for r in b.findAll('a'):
            
                if (r.get('href')):
                    
             
                    link = r.get('href')
                  
                    
                    if link.startswith('http://') or link.startswith('https://'):
                        
                        web.append(link)
                        #print(web)
                
               # print(al)
                        
                    
               
    obj = {"Company_name":anun,
          'Phone':hamar,
          'url' : web}
    
    
        
    
    
    final.append(obj)
    #print("This is your object")
   
    
    
        


# In[198]:


columns = ['Company_name', 'Phone', 'url']


# In[201]:


df = pd.DataFrame(final, columns=columns)


# In[202]:


df


# In[205]:


df.to_excel('scraped_data.xlsx')


# In[ ]:




