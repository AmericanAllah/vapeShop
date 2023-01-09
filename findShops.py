from selenium import webdriver
import time
import sys
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import threading
from selenium.common.exceptions import NoSuchElementException
import requests
import random
import datetime
import string
import os
from geopy import distance
from geopy.geocoders import Nominatim
import openpyxl

#start chrome
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/search/vape+shop/@30.2423978,-81.6037661,12z/data=!3m1!4b1")
i=3
running = True
addys = []
def getAddy(addys, driver, i, ix):
    try:
        driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div['+str(i)+']/div/a').click()
        print('clicked')
    except:
        print('cant click')
        ix=ix+1
        time.sleep(1)
        return 0, False
        getAddy(addys, driver, i, ix)
    if ix > 10:
        print('next i')
        i=i+1
        ix=0
    try:
        if driver.execute_script('return document.querySelector("#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div:nth-child(9) > div:nth-child(3) > button > div.AeaXub").innerText') in addys:
            print('already in list ix: '+str(ix)+' i: '+str(i))
            ix=ix+1
            time.sleep(3)
        addys.append(driver.execute_script('return document.querySelector("#QA0Szd > div > div > div.w6VYqd > div.bJzME.Hu9e2e.tTVLSc > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div:nth-child(9) > div:nth-child(3) > button > div.AeaXub").innerText'))
    except Exception as e:
        print('cant get addy')
        time.sleep(1)
        running = False
        getAddy(addys, driver, i, ix)
    return i, True

def runFunction(i, running, driver):
    try:
        element = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div['+str(i)+']/div/a')
        driver.execute_script("arguments[0].scrollIntoView();", element)
        print('scrolled')
        driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div['+str(i)+']/div/a').click()
        running = True
    except:
        running = False
        print('stopped running')
    i=i+2
    print('clicked')
    time.sleep(3)
    i, running = getAddy(addys, driver, i, 0)
    print(addys[-1])
    return(i,running)
while running:
    i, running = runFunction(i, running, driver)
    time.sleep(1)

#save addys to a file each addy on a new line
#open addys.txt in current directory

with open('addys.txt', 'w') as f:
    for item in addys:
        f.write("%s\n" % item)
    
