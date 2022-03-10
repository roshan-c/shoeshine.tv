import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_firefox_session():
    service = FirefoxService(executable_path=GeckoDriverManager().install())

    driver = webdriver.Firefox(service=service)

    videokey = input(
        "Please enter the unique 5 character key from your Outplayed.tv link: "
    )
    videourl = "https://outplayed.tv/media/" + videokey
    time.sleep(1)
    print(videourl)

    driver.get(videourl)

    videolink = driver.find_element_by_name("og:video")
    print(videolink)

    import urllib.request

    url = videolink
    name = input("Enter the name for the video\n")
    name = name + ".mp4"
    try:
        print("Downloading starts...\n")
        urllib.request.urlretrieve(url, name)
        print("Download completed..!!")
    except Exception as e:
        print(e)
    
    driver.quit()



@pytest.mark.skip(reason="only runs on Windows")
def test_ie_session():
    service = IEService(executable_path=IEDriverManager().install())

    driver = webdriver.Ie(service=service)

    driver.quit()

test_firefox_session()
