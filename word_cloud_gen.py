from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



#Global Variables############################################################################################
# Path to the chrome driver
driver_path = "/media/paarthurnax/Main_Storage/Linux_Storage/Projects/Selenium/chromedriver"
website = 'https://scholar.google.com/'
search = 'space x'


#This function up the web-driver as well as specifies location of all downloaded csv files.
def web_driver_setup():
    chromeOptions = webdriver.ChromeOptions()
    chromedriver = driver_path
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
    return driver



# This code will be run multiple times, it is set up in a specific sequence so that the correct
# options are chosen to allow the download to commence.
def Text_Collector(driver,search, website):
    # Try catch is needed due to the fact that some records do not prompt a option to show which crashes the
    #script when the non-existent button is pushed.
    try:
        driver.get(website)
        time.sleep(1)
        #inputs text into search
        driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]').send_keys(search)
        time.sleep(1)
        #Clicks the search button
        driver.find_element_by_xpath('//*[@id="gs_hdr_tsb"]').click()
        #Selects text box to fill in with text

        time.sleep(5)
    except Exception:
        print('Something went wrong :(')
        
        
        
###########################################################################################################################
# Main

# Defines and set the web driver. 
driver = web_driver_setup()

# Opens the web browser to collect text data and save it. 
Text_Collector(driver ,search ,website)






















