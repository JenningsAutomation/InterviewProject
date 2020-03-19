# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:51:21 2020

@author: Demian Jennings
"""


from bs4 import BeautifulSoup
import time
from selenium import webdriver
import csv

def getInventoryList():
    # Start browser
    driver = webdriver.Chrome()  
    driver.get('http://eval.arborian.com/')

    # dwell time, for any js to load
    time.sleep(2)    
    inventoryList=['296804','198765','750518','688028','127853','261549','382587','389471','251184','601484']
    for i in range(34):
        pageSource = driver.page_source  # Copy page source
        bs = BeautifulSoup(pageSource,'html.parser')
        table = bs.find('div', id='root')
        item_data=table.find('div')
        for item in item_data:
            small_=item.find_all("small")
            quant_group= small_[1].text
            inventory, availability = quant_group.split(' ')
            if item.h3['id'] in inventoryList and availability=='Available':
                master_list.append((item.h3['id'],inventory))        
        driver.find_element_by_xpath('//*[@id="root"]/div[2]/a[2]').click()
        time.sleep(2) 
    driver.quit()
    return
    

def writeInventoryList(csvFile):    
    with open(csvFile, 'w',newline='') as f:
        fieldnames=['product_id','inventory']
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for row in master_list: 
            writer.writerow(row)
    return



master_list = []
getInventoryList()
writeInventoryList('inventory.csv')



    
