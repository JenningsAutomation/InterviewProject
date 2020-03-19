# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 21:46:04 2020

@author: demia
"""
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import csv

def productPriceList():
    # Start browser
    driver = webdriver.Chrome()  
    driver.get('http://eval.arborian.com/')

    # dwell time, for any js to load
    time.sleep(2)
    
    for i in range(34):
        pageSource = driver.page_source  # Copy page source
        bs = BeautifulSoup(pageSource,'html.parser')
        table = bs.find('div', id='root')
        item_data=table.find('div')
        for item in item_data:
            items=[i for i in [item.h3['id'],item.h3.text,item.b.text]]
            master_list.append(items)
            driver.find_element_by_xpath('//*[@id="root"]/div[2]/a[2]').click()
            time.sleep(2)  
    driver.quit()
    return
 
def writeToProductFile(csvFile):
    with open(csvFile, 'w',newline='') as f:
        fieldnames=['product_id','product_name','price']
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for row in master_list: 
            writer.writerow(row)
    return
        
master_list = []    
productPriceList()    
writeToProductFile('prices.csv')
    
    







    
