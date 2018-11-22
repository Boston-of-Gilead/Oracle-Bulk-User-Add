import arrow #loads time feature
import csv #loads csv reading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions() #these three lines get rid of the alert in Chrome about being controlled by automated test software
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("<url>") # Opens webpage

f = open('Oracle_Bulk_Add.csv') # assigns variable to the csv
reader = csv.DictReader(f) #tells python to read that variable

for row in reader: #for loop

	driver.find_element_by_id("lnkCreateNew").click() #tells Selenium to click on the "create new instance" link

	sel1 = Select(driver.find_element_by_id("control_1")) #Login Request For = id control_1		M
	sel1.select_by_visible_text(row['RequestFor'])   # Drop down. 2 choices. This works! However some if/else statements will be needed for the script to select correctly off the CSV

	sel2 = Select(driver.find_element_by_id("control_2")) #New User or Change Access = id control_2	M
	sel2.select_by_visible_text(row['NewOrChg'])   #  Drop down. 2 choices. This works! However some if/else statements will be needed for the script to select correctly off the CSV

	sel3 = Select(driver.find_element_by_id("control_3")) #Offshore access = id control_3
	sel3.select_by_visible_text(row['Offshore'])   # Drop down. 2 choices. This works! However some if/else statements will be needed for the script to select correctly off the CSV

	sel4 = Select(driver.find_element_by_id("control_4")) #Location change = id control_4
	sel4.select_by_visible_text(row['LocationChg'])   # Drop down. 2 choices. This works! However some if/else statements will be needed for the script to select correctly off the CSV

	sel5 = driver.find_element_by_id("control_5") #Date = id control_5				M
	sel5.send_keys(arrow.now().format('MM/DD/YYYY'))

	sel6 = driver.find_element_by_id("control_6") #Requested By (Manager's Name) = id control_6	M
	sel6.send_keys(row['ReqBy'])

	sel7 = driver.find_element_by_id("control_7") #First Name: = id control_7			M
	sel7.send_keys(row['FName'])

	sel8 = driver.find_element_by_id("control_8") #Middle Initial	= id control_8
	sel8.send_keys(row['MidIni'])

	sel9 = driver.find_element_by_id("control_9") #Last Name: = id control_9			M
	sel9.send_keys(row['LName'])

	sel10 = driver.find_element_by_id("control_10") #Windows NT or VPN ID = id control_10		M
	sel10.send_keys(row['NTorVPN'])

	sel11 = driver.find_element_by_id("control_11") #White Cap Location number = id control_11	M
	sel11.send_keys(row['LocNum'])

	sel12 = driver.find_element_by_id("control_12") #Loc./ Cost Center City = id control_12		M
	sel12.send_keys(row['CCC'])

	sel13 = Select(driver.find_element_by_id("control_13")) #Temporary Account = id control_13		M
	sel13.select_by_visible_text(row['TempAcct'])   # Drop down. 2 choices. This works! However some if/else statements will be needed for the script to select correctly off the CSV

	sel14 = driver.find_element_by_id("control_14") #Temporary Account End Date = id control_14
	sel14.send_keys(row['TempEndDate'])

	sel15 = driver.find_element_by_id("control_15") #Roles. Use the option number, 3 digits. = id control_15
	sel15.send_keys(row['RoleNum'])

	#sel16 = driver.find_element_by_id("control_16") # not needed

	#sel17 = driver.find_element_by_id("control_17") # not needed

	sel18 = Select(driver.find_element_by_id("control_18")) #Remove Buyer Access = id control_18
	sel18.select_by_visible_text(row['RemBuyerAcc'])   # Drop down. 2 choices. This works! However some if/else statements will be needed for the script to select correctly off the CSV

	sel19 = Select(driver.find_element_by_id("control_19")) #Buyer Job Position = id control_19
	sel19.select_by_visible_text(row['BuyerJobPos'])   # Drop down. 5 choices. This works! However some if/else statements will be needed for the script to select correctly off the CSV

	sel20 = driver.find_element_by_id("control_20") #What branches is the Buyer approved for? = id control_20
	sel20.send_keys(row['WhatBrch'])

	sel21 = Select(driver.find_element_by_id("control_21")) #Region = id control_21
	sel21.select_by_visible_text(row['Region'])   # Drop down. 6 choices. This works! However some if/else statements will be needed for the script to select correctly off the CSV

	driver.find_element_by_name("btnSubmit").click() # submits the completed form

#This works!
#elem.clear()
#sel5.send_keys("ChrisWasHere")
#elem.send_keys(Keys.RETURN)

#time.sleep(10)