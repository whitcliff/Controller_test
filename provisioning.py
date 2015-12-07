#!/usr/bin/python
from selenium import webdriver
import time
import sys       # python system module
import os
import os.path
import time      # python time module
import subprocess
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

print "##################Provisioning phone units#######################"
controler="127.0.0.1:9443"

##Extract the number of units from the ipaddress.txt file####
file=open('ipaddress.txt','r')
number = file.readline()
print "There are "+number+"phone units !"
file.close()
number=int(number)


##Open the browser#############
browser = webdriver.Firefox() # Get local session of firefox
browser.implicitly_wait(10)
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

############Attributes string########
SIPServer=["1.1.1.1","","as.iop1.broadworks.com","10.1.0.1","192.168.1.1"]  ##define the server address
codec="9,0,8,111,108,3"
echocancell=random.randrange(0,2)
DNSService=random.randrange(0,2)
STUNServer="stun.test.com:19032"
HandsetLift=random.randrange(0,2)
DTMFType=random.randrange(0,3)
ImmersiveMode=random.randrange(0,2)
OutboundProxy=["2.2.2.2","","199.19.193.8","20.2.0.2","192.168.255.254"]
VoiceMail=["*97","","#12","1000"]
Exten=3004005000
AccountName="UBNT test account"
SIPUsername="SiPUserName"
SIPPassword="PassWord"
#AuthenticateMethod=random.randrange(0,2)
AuthorizationID="AuthoRizaTioN"
SIPRegistration=["30","60","90"]
DSCP=["0","18","30","46"]
#TCP=random.randrange(0,2)
#STUNSettings=random.randrange(0,3)
TurnServer=["turn1.test.com","turn2.test.com","turn3.test.com"]
TurnUsername=["turn1username","turn2username","turn3username"]
TurnPassword=["turn1password","turn2password","turn3password"]

######-----Provision global settings--############
#generate the global attributes
Global=[SIPServer[0], codec, echocancell,DNSService,STUNServer,HandsetLift,DTMFType,ImmersiveMode,OutboundProxy[0],VoiceMail[0]]
print Global
##--Refresh the key--###
browser.find_element_by_css_selector("div.refresh-status").click()
browser.find_element_by_css_selector("div.refresh-status.active").click()
time.sleep(2)
###provision global settings in VoIP tab#####
browser.find_element_by_css_selector("#navSettings > a > span.nav-text").click()
browser.find_element_by_link_text("VOIP").click()
####SIP Server####
browser.find_element_by_name("sip_server").click()
browser.find_element_by_name("sip_server").clear()
browser.find_element_by_name("sip_server").send_keys(Global[0])
####Codec####
browser.find_element_by_name("sip_codec_order").click()
browser.find_element_by_name("sip_codec_order").clear()
browser.find_element_by_name("sip_codec_order").send_keys(Global[1])
###Software Echo Cancellation###
if Global[2]==0:
    browser.find_element_by_id("G_SettingsSipSwEc").click()
else:
    browser.find_element_by_id("G_SettingsSipSwEc").click()
    browser.find_element_by_id("G_SettingsSipSwEc").click()
###DNS Server Option####
if Global[3]==0:
    browser.find_element_by_id("G_SettingsSipDnsSrv").click()
else:
    browser.find_element_by_id("G_SettingsSipDnsSrv").click()
    browser.find_element_by_id("G_SettingsSipDnsSrv").click()
###STUNServer Option###
browser.find_element_by_name("sip_stun_server").click()
browser.find_element_by_name("sip_stun_server").clear()
browser.find_element_by_name("sip_stun_server").send_keys(Global[4])
##Handset lift###
if Global[5]==0:
    browser.find_element_by_id("G_SettingsSipShowKeypadOnHook").click()
else:
    browser.find_element_by_id("G_SettingsSipShowKeypadOnHook").click()
    browser.find_element_by_id("G_SettingsSipShowKeypadOnHook").click()
###DTMF####
if Global[6]==0:
    browser.find_element_by_xpath("//div[@id='settingsVoip']/div/form/fieldset[2]/div/div[9]/div/label/span").click()
    browser.find_element_by_id("sipDtmfTypeInband").click()
elif Global[6]==1:
    browser.find_element_by_xpath("//div[@id='settingsVoip']/div/form/fieldset[2]/div/div[9]/div/label[2]/span").click()
    browser.find_element_by_id("sipDtmfTypeRFC2833").click()
else:
    browser.find_element_by_xpath("//div[@id='settingsVoip']/div/form/fieldset[2]/div/div[9]/div/label[3]/span").click()
    browser.find_element_by_id("sipDtmfTypeSipInfo").click()
###Immersive Mode####
if Global[7]==0:
    browser.find_element_by_id("G_SettingsSipImmersiveUi").click()
else:
    browser.find_element_by_id("G_SettingsSipImmersiveUi").click()
    browser.find_element_by_id("G_SettingsSipImmersiveUi").click()
######Advance Settting#######
browser.find_element_by_css_selector("legend.toggle").click()
####Outbound Proxy####
browser.find_element_by_name("sip_proxy").click()
browser.find_element_by_name("sip_proxy").clear()
browser.find_element_by_name("sip_proxy").send_keys(Global[8])
####SIP Voicemail####
browser.find_element_by_name("sip_voicemail").click()
browser.find_element_by_name("sip_voicemail").clear()
browser.find_element_by_name("sip_voicemail").send_keys(Global[9])
browser.find_element_by_xpath("(//button[@type='submit'])[2]").click()

##--Refresh the key--###
browser.find_element_by_css_selector("div.refresh-status").click()
browser.find_element_by_css_selector("div.refresh-status.active").click()
time.sleep(2)

#####Create arraies to save phone units information.
Extension=[[0 for col in range(5)]for row in range(number)]
array=[]
with open('ipaddress.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        array.append(line)
for i in range(number):
    Extension[i][0]=array[i+1]
    #print Extension[i][0]
print Extension

array=[]
with open ('macaddr.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        array.append(line)

for i in range(number):
    print array[i]
    Extension[i][1]=array[i+1]

print Extension
######-----Provision extension settings--############
##generate the attributes for each account and write it to the file attribute.txt####

file=open('attribute.txt','w')
for j in range(number):
    for i in range(3):
        newarray=[0]
        ct=j*3+i  #generate a number to increase in every loop
        ##Extension
        Ex= str(Exten+ct)
        newarray=[Ex]
        #account ID
        AccountID=i
        newarray.append(AccountID)
        #Account enable
        AccountEnable=random.randrange(0,2)
        newarray.append(AccountEnable)
        ##Account lock###
        AccountLock=random.randrange(0,2)
        newarray.append(AccountLock)
        ###Account name###
        AcctName=AccountName+str(ct)
        newarray.append(AcctName)
        ###SIP Username###
        SIPUName=SIPUsername+str(ct)
        newarray.append(SIPUName)
        ###SIP Password####
        SIPPW=SIPPassword+str(ct)
        newarray.append(SIPPW)
        ####SIP Server####
        SIPPBX=SIPServer[random.randrange(0,5)]
        newarray.append(SIPPBX)
        ####SIP Authentication Method####
        AuthenticateMethod=random.randrange(0,2)
        newarray.append(AuthenticateMethod)
        ####Authentication ID####
        AuthID=AuthorizationID+str(ct)
        newarray.append(AuthID)
        ###Outbound Proxy###
        Outpx=OutboundProxy[random.randrange(0,5)]
        newarray.append(Outpx)
        ##Voice Mail###
        VM=VoiceMail[random.randrange(0,4)]
        newarray.append(VM)
        ##SIP Registration Expirey###
        SRE=SIPRegistration[random.randrange(0,3)]
        newarray.append(SRE)
        ###DSCP###
        QOS=DSCP[random.randrange(0,4)]
        newarray.append(QOS)
        ###TCP over SIP###
        TCP=random.randrange(0,2)
        newarray.append(TCP)
        ###STUN Settings
        STUNSettings=random.randrange(0,4)
        STUN=0
        if STUNSettings!=3:
            STUN=STUNSettings
            newarray.append(STUN)
        else:
            STUN=3
            newarray.append(STUN)
            newarray.append(TurnServer[i])
            newarray.append(TurnUsername[i])
            newarray.append(TurnPassword[i])
        Extension[j][i+2]=newarray
    file.writelines(str(Extension[j])+'\n')
file.close()
print Extension

##Fill the attribute to the controller####

browser.find_element_by_link_text("Extensions").click()
####Ascending the extension####
browser.find_element_by_css_selector("#settingsExtensions > div.section.section-main > div.section-home > div.data-table.untitled > table.backgrid > thead > tr > th > a").click()

for j in range(0,number):
    for i in range(0,3):
        browser.find_element_by_xpath("//div[@id='settingsExtensions']/div/div/div[2]/button").click()
        browser.find_element_by_name("extension").clear()
        browser.find_element_by_name("extension").send_keys(str(Extension[j][i+2][0]))
        time.sleep(1)
        ##########Select the account ID address################
        browser.find_element_by_xpath('//div[2]/div/span/a/span[2]').click()
        browser.find_element_by_link_text(str(i+1)).click()
        ##########Type the name################
        browser.find_element_by_name("name").clear()
        browser.find_element_by_name("name").send_keys(str(Extension[j][i+2][2]))
        ##########Select the phone device by MAC address################
        browser.find_element_by_name("x_sip_username").clear()
        browser.find_element_by_name("x_sip_username").send_keys(str(Extension[j][i+2][5]))
        ##########Type the password################
        #browser.find_element_by_name("x_sip_password").clear()
        browser.find_element_by_name("x_sip_password").send_keys(str(Extension[j][i+2][6]))
        ##########Type the server address################
        browser.find_element_by_name("x_sip_server").clear()
        browser.find_element_by_name("x_sip_server").send_keys(str(Extension[j][i+2][7]))
        ##########Selected SIP Authentication Method################
        browser.find_element_by_xpath('//div[9]/div/span/a/span[2]').click()
        browser.find_element_by_xpath("//a[contains(text(),'User-based (most common)')]").click()
        ##########Select the phone device by MAC address################
        browser.find_element_by_xpath('//div[10]/div/span/a/span[2]').click()
        #browser.find_element_by_id('extensionDevice1-menu').find_element_by_link_text(Extension[5][1]).click()
        browser.find_element_by_xpath("//a[contains(text(),'"+Extension[j][1]+"')]").click()
        ##########Select the advanced options################
        browser.find_element_by_css_selector("fieldset.advanced > legend.toggle").click()
        ##########Input authentication name################
        browser.find_element_by_name("sip_authname").clear()
        browser.find_element_by_name("sip_authname").send_keys(str(Extension[j][i+2][9]))
        ##########Input the outbound proxy ################
        browser.find_element_by_id("sipProxy"+str(j*3+i+1)).send_keys(str(Extension[j][i+2][10]))
        #browser.find_element_by_xpath("//div[2]/div/form/fieldset[2]/div/div[2]/input").send_keys(str(Extension[0][2][10]))
        ##########Input the voicemail number ################
        browser.find_element_by_id("sipVoicemailURL"+str(j*3+i+1)).send_keys(str(Extension[j][i+2][11]))
        #browser.find_element_by_name("sip_voicemail").send_keys(Extension[0][2][11])
        ###########Submit the result#######################
        browser.find_element_by_xpath("(//button[@type='submit'])[3]").click()
        ###Re-enter the extension page to provisoin more setttings#####
        if i+j*3 == 0:
            browser.find_element_by_xpath("//div[@id='settingsExtensions']/div/div/div/table/tbody/tr/td[4]/button").click()
        else:
            browser.find_element_by_xpath("//div[@id='settingsExtensions']/div/div/div/table/tbody/tr["+str(j*3+i+1)+"]/td[4]/button").click()
        ####Select Account Enable###
        browser.find_element_by_xpath("//div[3]/div/span/a/span[2]").click()
        if Extension[j][2][2] == 1:
            browser.find_element_by_link_text("Yes").click()
        else:
            browser.find_element_by_link_text("No").click()
        ###Account Lock####
        if Extension[j][2][3] == 1:
            browser.find_element_by_name("sip_locked").click()
        ##########Select the advanced options################
        browser.find_element_by_css_selector("fieldset.advanced > legend.toggle").click()
        ####SIP Registration Expiry####
        browser.find_element_by_name("sip_reg_exp").clear()
        browser.find_element_by_name("sip_reg_exp").send_keys(str(Extension[j][i+2][12]))
        #browser.find_element_by_link_text("//div[2]/div/form/fieldset[2]/div/div[4]/input").send_keys(str(Extension[0][2][12]))
        ####DSCP for RTP#####
        browser.find_element_by_name("sip_rtp_dscp").clear()
        browser.find_element_by_name("sip_rtp_dscp").send_keys(str(Extension[j][i+2][13]))
        #browser.find_element_by_xpath("//div[2]/div/form/fieldset[2]/div/div[5]/input").send_keys(str(Extension[0][2][13]))
        ###TCP over SIP#####
        if int(Extension[j][i+2][14])==1:
            browser.find_element_by_name("sip_over_tcp").click()
        ##########Select the STUN options################
        browser.find_element_by_css_selector("fieldset.stun.multi-sip-support > legend.toggle").click()
        ####Select STUN Method####
        STUN=int(Extension[j][i+2][15])
        if STUN ==1:
            browser.find_element_by_name("sip_stun_enabled").click()
        elif STUN ==2:
            browser.find_element_by_name("sip_ice_enabled").click()
        elif STUN ==3:
            browser.find_element_by_name("sip_turn_enabled").click()
            browser.find_element_by_name("sip_turn_server").send_keys(str(Extension[j][i+2][16]))
            browser.find_element_by_name("sip_turn_username").send_keys(str(Extension[j][i+2][17]))
            browser.find_element_by_name("sip_turn_password").send_keys(str(Extension[j][i+2][18]))
        else:
            pass
        ###Submit and Save#####
        time.sleep(3)
        browser.find_element_by_xpath("(//button[@type='submit'])[3]").click()
        time.sleep(3)


browser.close()

# 0 Extension
# 1 Account ID
# 2 Account Enable
# 3 Account Lock
# 4 Account Name
# 5 SIP ID
# 6 SIP Password
# 7 SIP Server
# 8 SIP auth method
# 9 SIP auth ID
# 10 Outbound proxy
# 11 voicemail
# 12 SIP Register expiry
# 13 DSCP
# 14 TCP over SIP
# 15 STUN
# ------------------
# 16 TURN Server
# 17 TURN Username
# 18 TURN Password
