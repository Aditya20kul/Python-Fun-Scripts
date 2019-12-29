#Script that displays the useful information about the required user

######################### Created By - Aditya Kulkarni #####################
#																		   #
#	LinkedIn Profile Link - https://www.linkedin.com/in/adityakulkarni20/  #																	   #
#   																	   #
############################################################################

# Requirements for running the script ->
# 		-> BeautifulSoup
# 		-> Requests

# For running the script -
#		-> python github-stats.py
#		-> Enter the valid Username of the user

# The script scrapes the following data of the user -
# 1. Name
# 2. Number of followers
# 3. Number of following
# 4. Profile Link
# 5. Latest 5 Updated Repositories 
from selenium import webdriver 
import requests 
from bs4 import BeautifulSoup 
import random 

HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
userName = input('Please Enter the correct Username of Github profile - ')
#userName = 'Aditya20kul'
url = 'https://github.com/'+userName+'?tab=repositories'
#print(url)
r = requests.get(url,headers=HDR)  
soup1 = BeautifulSoup(r.content,'html5lib')
#print(soup1)
name = soup1.findAll('span',class_='vcard-fullname')
print('\n**********************************************************************************\n')
print('----> Name of the User - '+name[0].text)
followers = soup1.findAll('span',class_='Counter hide-lg hide-md hide-sm')
print('----> Number of Repositories - '+str(followers[0].text.strip()))
print('----> Number of Followers - '+str(followers[3].text.strip()))
print('----> Number of Following - '+str(followers[4].text.strip()))
print('----> Link to GitHub Profile - '+'https://github.com/'+userName)
print('----> Link to All the Repositories - '+url)
print('\n**********************************************************************************\n')
print("\n----> Displaying Latest Updated 5 Repositories - \n")
repo_list = soup1.findAll('div',id='user-repositories-list')
r_list = repo_list[0].findAll('ul')
r1 = r_list[0].findAll('li')
cnt = 0
for i in r1:
    div1 = i.findAll('div')
    div2 = div1[0].findAll('div')
    # for name and link of repo
    div3 = div2[0].findAll('a')
    repo_name = div3[0].text.strip()
    print("Title of the Repository - "+ repo_name)
    repo_link = "https://github.com/"+div3[0]['href']
    print("Link for the repo - "+ repo_link)
    r1 = requests.get(repo_link,headers=HDR)
    soup2 = BeautifulSoup(r1.content,'html5lib')
    #print(soup1)
    stars = soup2.findAll('a',class_='social-count js-social-count')
    print("Number of stars - "+str(stars[0].text.strip()))
    print('\n------------------------------------------\n')
    if cnt==4:
        break
    cnt+=1    
print('Total '+str(cnt+1)+' Repositories Displayed')   
