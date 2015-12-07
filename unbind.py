#!/usr/bin/python
from selenium import webdriver
import time
import sys       # python system module
import os
import os.path
import time      # python time module
import subprocess
from selenium.webdriver.common.keys import Keys


print "##################Unibnd the adopted device#######################"
controler="127.0.0.1:9443"

##Extract the number of units from the ipaddress.txt file####
file=open('ipaddress.txt','r')
number = file.readline()
print "There are "+number+"phone units !"
file.close()
number = int(number)


browser = webdriver.Firefox() # Get local session of firefox
browser.get("https://"+controler+"/manage/s/default/devices") # Load page
assert "Login" in browser.title
elem = browser.find_element_by_name("username") # Find the query box
elem.send_keys("admin" + Keys.RETURN)
time.sleep(0.2) # Let the page load, will be added to the API
elem = browser.find_element_by_name("password")
elem.send_keys("admin" + Keys.RETURN)
time.sleep(5)
browser.find_element_by_css_selector("#navDevices > a > span.nav-text").click()
time.sleep(2)
#------Refresh key #########
browser.find_element_by_css_selector("div.refresh-status").click()
browser.find_element_by_css_selector("div.refresh-status.active").click()
time.sleep(2)
browser.find_element_by_css_selector("#navDevices > a > span.nav-text").click()
time.sleep(2)


for i in range(number+1):
    browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr/td[2]").click()
    browser.find_element_by_xpath("//a[contains(text(),'Configuration')]").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div/div[2]/div/div[3]/div").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[2]/div/div[4]/button").click()
    browser.find_element_by_xpath("(//button[@type='button'])["+str(4+i*2)+"]").click()
    time.sleep(2)

browser.close()
