#!/usr/bin/python
import time
import sys       # python system module 
import os         
import os.path 
import time      # python time module
import subprocess 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest, time, re
# import pyautogui

print "****************************************************************************"
print "****************Collect phone units IP and MAC address***********************"
print "*****************************************************************************" 

#the IP address is saved in ipaddress.txt
#the MAC address is saved in macaddr.txt

ipaddress=[""]*50
macaddress=[""]*50
count=0 
controller="127.0.0.1:9443"

#print "The number of units is " +str(unitNum)+"\n" 

browser = webdriver.Firefox() # Get local session of firefox
browser.get("https://"+controller+"/manage/s/default/devices") # Load page
assert "Login" in browser.title
elem = browser.find_element_by_name("username") # Find the query box
elem.send_keys("admin" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
elem = browser.find_element_by_name("password") 
elem.send_keys("admin" + Keys.RETURN)
time.sleep(5) 
browser.find_element_by_css_selector("#navDevices > a > span.nav-text").click()
time.sleep(2)
#------Refresh key 1
browser.find_element_by_css_selector("div.refresh-status").click()
browser.find_element_by_css_selector("div.refresh-status.active").click()
time.sleep(2)

browser.find_element_by_css_selector("#navDevices > a > span.nav-text").click()
#browser.find_element_by_xpath("//div[@id='devicesIndex']/div/form/div/label[4]/span").click()
#browser.find_element_by_id("devicesFilterPhones").click()
time.sleep(2)

#-----Export phone IP Address----
file=open('ipaddress.txt', 'w')
print "The Phone IP are "
while count < 50:
    try:
        ipaddress[count]=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(count+1)+"]/td[4]").text
        print ipaddress[count]
        count = count+1
        
    except:
        print "The IP address searching is over"
        break
print "The number of phone device is", count
unitNum=count
time.sleep(2)

count=0
file.write(str(unitNum)+'\n')
while count < unitNum:
    try:
        file.write(ipaddress[count]+'\n')
        count = count+1
        
    except:
        print "Writing file Error!"
        break
file.close()

#-----Export phone MAC Address----
count=0
file=open('macaddr.txt', 'w')
while count < unitNum:
    try:
        macaddress[count]=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(count+1)+"]/td[2]").text
        print macaddress[count]
        count = count+1
        
    except:
        print "The MAC searching error"
        break
print "The MAC searching is over!!!"

count=0
file.write(str(unitNum)+"\n")
while count < unitNum:
    try:
        file.write(macaddress[count]+'\n')
        count = count+1
    
    except:
        print "writing file error"
        break
    
file.close()

time.sleep(2)

##########close the browser##########
browser.close()