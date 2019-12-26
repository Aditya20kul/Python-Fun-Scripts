############ Created By - Aditya Kulkarni ##############

# Requirements for running the script ->
# 		-> BeautifulSoup
# 		-> Requests

# For running the script -
#		-> python codechef_contests.py

# Getting information of all the live contests of Codechef.

from selenium import webdriver 
import requests 
from bs4 import BeautifulSoup 
import random 
r = requests.get('https://www.codechef.com/contests')
soup1 = BeautifulSoup(r.content,'html5lib')
a = soup1.findAll('table',class_='dataTable')
info = a[0].findAll('tbody')
#print(info)
contests = info[0].findAll('tr')
if not contests:
    print('No live contests available.')
else:
	print("--------------------------------------------------------------")
    for c in contests:
        #print(c)
        c_info = c.findAll('td')
        it = 0;
        for ci in c_info:
            if it==0:
                print('Contest Code - ' + str(ci.text))
            elif it==1:
                print('Contest Name - ' + str(ci.text))
                print('Contest Link - ',end='')
                urls = ci.findAll('a')

                for u in urls:
                    print('https://www.codechef.com/'+u['href'])
            elif it==2:
                print('Start Date and Time - ' + str(ci.text))
            elif it==3:
                print('End Date and Time - ' + str(ci.text)) 
            it+=1    
        print("--------------------------------------------------------------")
