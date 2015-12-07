#!/usr/bin/python
from selenium import webdriver
import time
import sys       # python system module
import os
import os.path
import time      # python time module
import subprocess
from selenium.webdriver.common.keys import Keys


print "##################Adopt, Locate, Reboot and Locate phone units#######################"
controller="127.0.0.1:9443"

##Extract the number of units from the ipaddress.txt file####
file=open('ipaddress.txt','r')
number = file.readline()
print "There are "+number+"phone units !"
file.close()

#############Open Browser and enter the device page##############

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
#------Refresh key #########
browser.find_element_by_css_selector("div.refresh-status").click()
browser.find_element_by_css_selector("div.refresh-status.active").click()
time.sleep(2)
browser.find_element_by_css_selector("#navDevices > a > span.nav-text").click()
time.sleep(2)

###---Adopt the phone units--####
try:
    browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr/td[24]/button").click()
    time.sleep(3)
except:
    ip=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr[1]/td[4]").text
    print "Locate error! The phone IP address is "+ip

number = int(number)

for i in range(2,number+1):
    try:
        browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[24]/button").click()
        time.sleep(3)
    except:
        ip=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[4]").text
        print "Adopt error! The phone IP address is "+ip
    continue


#------Refresh key #########
time.sleep(10)
browser.find_element_by_css_selector("div.refresh-status").click()
browser.find_element_by_css_selector("div.refresh-status.active").click()
time.sleep(2)

###---Locate the phone units--####
try:
    browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr/td[24]/button").click()
    time.sleep(3)
    browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr/td[24]/button").click()
except:
    ip=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr[1]/td[4]").text
    print "Locate error! The phone IP address is "+ip

for i in range(2,number+1):
    try:
        browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[24]/button").click()
        time.sleep(3)
        browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[24]/button").click()
        time.sleep(3)
    except:
        ip=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[4]").text
        print "Locate error! The phone IP address is "+ip
    continue

#------Refresh key #########
time.sleep(10)
browser.find_element_by_css_selector("div.refresh-status").click()
browser.find_element_by_css_selector("div.refresh-status.active").click()
time.sleep(2)

#------Reboot the phone #########
try:
    browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr/td[24]/button[2]").click()
    time.sleep(2)
except:
    ip=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr[1]/td[4]").text
    print "Reboot error! The phone IP address is "+ip

for i in range(2,number+1):
    try:
        browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[24]/button[2]").click()
        time.sleep(3)
    except:
        ip=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[4]").text
        print "Reboot error! The phone IP address is "+ip
    continue

time.sleep(150)

#------Refresh key #########
time.sleep(20)
browser.find_element_by_css_selector("div.refresh-status").click()
browser.find_element_by_css_selector("div.refresh-status.active").click()
time.sleep(2)

###---Locate the phone units--####
try:
    browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr/td[24]/button").click()
    time.sleep(3)
    browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr/td[24]/button").click()
except:
    ip=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr[1]/td[4]").text
    print "2nd time Locate error! The phone IP address is "+ip

for i in range(2,number+1):
    try:
        browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[24]/button").click()
        time.sleep(3)
        browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[24]/button").click()
        time.sleep(3)
    except:
        ip=browser.find_element_by_xpath("//div[@id='devicesIndex']/div/div[2]/table/tbody/tr["+str(i)+"]/td[4]").text
        print "2nd time Locate error! The phone IP address is "+ip
    continue

browser.close()