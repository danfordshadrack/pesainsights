import pandas as pd
import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests


#source = requests.get('https://www.airtel.co.tz/tarrifs_tz').text
driver = webdriver.Chrome()
url= "https://www.tigo.co.tz/tigo-pesa-tariffs"
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")
#table = soup.findAll('table', {'class': 'table'}).text


for tr in soup.find_all('tr'):
    #for td in tr.find_all('td'):
        #print(td.text)
    values = [td.text for td in tr.find_all('td')]
    print(values)

#print(table)
driver.quit()
