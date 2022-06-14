# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:33:40 2021

@author: hp
"""

#new selenium project
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from lxml import html
from time import sleep
from selenium.webdriver.common.keys import Keys


#installing the chrome driver

count = 1
page = 1
pageIncrement = 10
maxRetrieves = 200
        
options = Options()
options.headless = False
options.add_experimental_option("detach" , True)
        
url = "https://www.voylla.com/collections/women-ring" 
        
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
browser.get(url)
browser.set_page_load_timeout(10)
#creatinng the list 
title = []
price = []
image = []

sleep(1) 
element = browser.find_element_by_tag_name('body')
previous_height = browser.execute_script('return document.body.scrollHeight')

#starting a loop 
while True:
    element.send_keys(Keys.PAGE_DOWN)
    sleep(.5)
    
    
    
    
    
    
    #get title
   
    xpathTitle = '//*[@id="main-div"]/div[9]/section/div[1]/ul/li['+ str(count) +']/div/div[3]/div[2]/span'
    Title = browser.find_element_by_xpath(xpathTitle)
    titleText = Title.get_attribute('innerHTML').splitlines()[0]
    title.append(titleText)
    
    # get price
    xpathPrice = '//*[@id="main-div"]/div[9]/section/div[1]/ul/li['+ str(count) +']/div/div[3]/div[3]/div[1]/span[1]'
    Price = browser.find_element_by_xpath(xpathPrice)
    priceText = Price.get_attribute('innerHTML')
    price.append(priceText)
    
    
    xpathLink = '//*[@id="main-div"]/div[9]/section/div[1]/ul/li['+ str(count) +']/div/a'
    Link = browser.find_element_by_xpath(xpathLink)
    linkText = Link.get_attribute('innerHTML'.splitlines()[0])
    image.append(linkText)
    
    count += 1 
    if count == 150:
        break
import pandas as pd
df = pd.DataFrame()
df['TITLE'] = title
df['PRICE'] = price
df['LINK'] = image

df.to_csv("voyalla.csv" , index = False)

    