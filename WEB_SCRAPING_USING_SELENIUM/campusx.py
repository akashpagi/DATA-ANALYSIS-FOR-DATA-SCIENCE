
# officail documentation : https://selenium-python.readthedocs.io/index.html
# article link : https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# options = Options()
# options.binary_location = r"C:\\Program Files (x86)\\Microsoft\\Edge\Application\\msedge.exe"
# driver = webdriver.Edge(options = options)
# driver.get('https://www.python.org/')
# # print('driver url:', driver.current_url)
# # print('driver title:', driver.title)
# # print('driver name:', driver.name)


s = Service()
o = webdriver.EdgeOptions()

# # Create a WebDriver instance with ChromeDriverManager
driver = webdriver.Edge(options=o,)
driver.get('https://www.google.com/')

# XPath is a Selenium technique to navigate through a page's HTML structure. It enables testers to navigate any document's XML structure, which can be used on both HTML and XML documents.
# Locating the search bar using its name attribute
search_bar = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')

# Sending the search query and submitting the form
search_bar.send_keys('campusx')
time.sleep(1)

search_bar.send_keys(Keys.ENTER)
time.sleep(1)

search_link = driver.find_element(by=By.XPATH, value='/html/body/div[5]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
search_link.click()

time.sleep(1)

join_program = driver.find_element(by=By.XPATH, value='//*[@id="1668425005116"]/span[2]/a')
join_program.click()