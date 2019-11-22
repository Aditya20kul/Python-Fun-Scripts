# Get the latest News From NDTV
# Requirements for running the script ->
# -> BeautifulSoup
# -> Requests
# For running the script -
#	python latestNews.py
# We can get the Big news as well as Top 10 news from www.ndtv.com
from selenium import webdriver 
import requests 
from bs4 import BeautifulSoup 
import random 
r = requests.get('https://www.ndtv.com/')
soup1 = BeautifulSoup(r.content,'html5lib')
a = soup1.findAll('div',class_='featured_desc')
print('\t\t\t######## BIG STORY #########\n\n')
for i in a:
    print('\t\t\t'+i.text)
print('\n\n\t\t\t ******************* Top 10 Stories ***************** \n\n')  
f_con = soup1.findAll('div',class_='featured_cont')
uls = f_con[0].findAll('ul')
lis = uls[0].findAll('li')
cnt = 0
headlines = []
for l in lis:
    headlines.append(l.text.strip())
for i in range(10):
    print('\n\t\t\t ############### News number ' + str(i+1)+' ##################\n')
    print('\t\t\t\n'+headlines[i]+"\n")
    
    