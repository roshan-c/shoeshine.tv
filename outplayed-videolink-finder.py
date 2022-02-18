from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
videokey = input("Please enter the unique 5 character key from your Outplayed.tv link: ")
videourl = "https://outplayed.tv/media/" + videokey
time.sleep(1)
print (videourl)


driver.get("https://outplayed.tv/media/35N3y")

assert "outplayed" in driver.title

videolink = driver.find_element_by_name('og:video')
print(videolink)
