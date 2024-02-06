import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s = Service()
o = webdriver.EdgeOptions()

# to protect form closing the window automatically
o.add_experimental_option('detach', True)

#Create a WebDriver instance with ChromeDriverManager
driver = webdriver.Edge(options=o,)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()

# Scroll down using JavaScript
old_height = driver.execute_script("return document.body.scrollHeight;")
while True:
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)
    
    new_height = driver.execute_script("return document.body.scrollHeight;")
    print('Old Height :',old_height)
    print('New Height :',new_height)
    
    if new_height == old_height:
        break
    old_height = new_height 
    
smartprix_mobile_page = driver.page_source
with open('smartprix_mobiles.html', 'w', encoding='utf-8') as f:
    f.write(smartprix_mobile_page)