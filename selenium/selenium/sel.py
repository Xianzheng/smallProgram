from selenium import webdriver
from selenium.webdriver.common.by import By

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Firefox()
browser.get("http://mozilla.com.cn/moz-portal.html")
element=browser.find_element(By.ID,"nv_plugin")

print(element)
time.sleep(3)
browser.close()